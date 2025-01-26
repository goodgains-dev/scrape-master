import streamlit as st
import os
import google.generativeai as genai

def get_api_key(api_key_name):
    # Check if the API key from the sidebar is present, else fallback to the .env file
    if api_key_name == 'OPENAI_API_KEY':
        return st.session_state['openai_api_key'] or os.getenv(api_key_name)
    elif api_key_name == 'GOOGLE_API_KEY':
        google_api_key = st.session_state['google_api_key'] or os.getenv(api_key_name)
        genai.configure(api_key=google_api_key)
        return google_api_key
    elif api_key_name == 'GROQ_API_KEY':
        return st.session_state['groq_api_key'] or os.getenv(api_key_name)
    else:
        return os.getenv(api_key_name)
