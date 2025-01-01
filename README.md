# SimpleLangchainFile - Restaurant Application

This is a Streamlit-based application that integrates with the LangChain framework and Groq AI models to provide restaurant suggestions and menu items based on the selected cuisine and dietary preferences.

## Features

- Allows users to select cuisines from a predefined list.
- Supports dietary preferences such as Vegetarian, Non-Vegetarian, Vegan, and Pescatarian.
- Suggests restaurant names and menu items using Groq AI models.
- Simple and interactive user interface powered by Streamlit.

## Installation

1. Clone the repository:
   ```bash
     git clone <repository_url>
     cd <repository_folder>```
2. Install dependencies:

   ```pip install -r requirements.txt```



**Usage**  

Run the Streamlit application:

   ```streamlit run app.py```  
Open the app in your browser using the URL provided by Streamlit (e.g., http://localhost:8501).

Enter your Groq API key in the sidebar, select the desired cuisine and dietary preference, and click the Suggest button to get recommendations.

**Input Options**  
1. Groq Api  
   Enter your API Key  
  
2. Cuisines  
    African  
    American  
    Asian  
    Caribbean  
    Central American  
    Chinese  
    Eastern European  
    French  
    Indian  
    Italian  
    Japanese  
    Korean  
    Latin American  
    Mediterranean  
    Mexican  
    Middle Eastern  
    North African  
    Scandinavian  
    South American  
    Southeast Asian  
    Spanish  
    Thai  
    Vietnamese  
  
3. Dietary Preferences  
    Vegetarian  
    Non-Vegetarian  
    Vegan  
    Pescatarian  
  
**Error Handling**  
  Ensure you input a valid Groq API key (without quotes).  
  If the API key is invalid or there is a connectivity issue, the app will display an error message.  

**Requirements**  
  Python 3.8 or higher  
  
**Dependencies**  
  
The application uses the following libraries:  
  *  streamlit: For building the interactive UI.  
  *  langchain: For handling LLM chains and prompts.  
  *  langchain-groq: For integrating with the Groq API.  
  *  python-dotenv: For managing API keys via .env files.  
  
**Contributing**  
If you'd like to contribute to this project, please fork the repository and submit a pull request.  
  
**License**  
This project is licensed under the MIT License.  
  
**Acknowledgements**  
Special thanks to the developers of LangChain, Groq, and Streamlit for their powerful tools and frameworks.  
