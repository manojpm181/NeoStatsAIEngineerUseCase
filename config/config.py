import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# API KEYS
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
SERPAPI_API_KEY = st.secrets.get("SERPAPI_API_KEY") or os.getenv("SERPAPI_API_KEY")

# MODELS
GROQ_MODEL = "llama3-8b-8192"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
