from langchain.chains import LLMChain, SequentialChain
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
import streamlit as st


st.title("Restaurant Application")
# Initialize the Groq model

cuisines = [
    "African",
    "American",
    "Asian",
    "Caribbean",
    "Central American",
    "Chinese",
    "Eastern European",
    "French",
    "Indian",
    "Italian",
    "Japanese",
    "Korean",
    "Latin American",
    "Mediterranean",
    "Mexican",
    "Middle Eastern",
    "North African",
    "Scandinavian",
    "South American",
    "Southeast Asian",
    "Spanish",
    "Thai",
    "Vietnamese",
]

dietaries = ["vegetarian","Non-vegetarian", "Vegan","Pescatarian"]
with st.sidebar:
    Groq_api_key = st.text_input("Enter Groq API",type="password")
    cuisine_name = st.selectbox("Select a cuisine",options=cuisines)
    dietary_type = st.radio("Select a cuisine",options=dietaries)
    suggest = st.button("Suggest")


if suggest:
    try:
        llm = ChatGroq(
            temperature=0.6,  # Adjust temperature as needed
            model_name="llama-3.3-70b-versatile",  # Specify the desired Groq model
            api_key=Groq_api_key
        )

        prompt1 = PromptTemplate(
            input_variables=["cuisine","dietary"],
            template="Suggest me only one restruant name for {dietary} cuisine: {cuisine} with any additional words"
        )
        chain1 = LLMChain(llm=llm, prompt=prompt1, output_key="name")

        # Step 2: Define the second prompt
        prompt2 = PromptTemplate(
            input_variables=["name","dietary"],
            template="suggest me 10 {dietary} menu items for: {name} with comma seperated. No extra phrases/words"
        )
        chain2 = LLMChain(llm=llm, prompt=prompt2, output_key="items")

        # Create the sequential chain
        sequential_chain = SequentialChain(
            chains=[chain1, chain2],
            input_variables=["cuisine","dietary"],  # Input variable for the entire chain
            output_variables=["name","items"]  # Output variable of the last chain
        )
        input_dict = {"cuisine": cuisine_name, "dietary": dietary_type}
        output = sequential_chain(input_dict)

        st.header(f"Name suggestion for {cuisine_name} cuisines is {output['name']}")
        st.write("Few menu items are:")
        for i in output['items'].split(','):
            st.write(i.strip())
    except Exception as e:
        st.write("Pass valid Groq API key without single/double quotes")
        st.write(f"GroqError encountered: {e}")
