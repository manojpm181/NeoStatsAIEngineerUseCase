from langchain_groq import ChatGroq
from config.config import GROQ_API_KEY, GROQ_MODEL


def get_chatgroq_model():
    try:
        chat = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name=GROQ_MODEL,
            temperature=0.3
        )
        return chat

    except Exception as e:
        raise RuntimeError(f"Groq model error: {str(e)}")
