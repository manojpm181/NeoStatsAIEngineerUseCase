import streamlit as st
from models.llm import get_chatgroq_model
from utils.document_loader import load_documents
from utils.rag_utils import create_vector_store, retrieve_documents
from utils.web_search import search_web
from utils.prompt_utils import build_prompt

st.set_page_config(
    page_title="AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Knowledge Assistant")

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.header("Settings")

    mode = st.radio(
        "Response Mode",
        ["Concise", "Detailed"]
    )

    uploaded_file = st.file_uploader(
        "Upload a PDF",
        type="pdf"
    )

# ---------------- Initialize Model ---------------- #

chat_model = get_chatgroq_model()

# ---------------- Vector Store Initialization ---------------- #

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

# ---------------- PDF Upload Handling ---------------- #

if uploaded_file is not None and st.session_state.vectorstore is None:

    try:

        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        docs = load_documents("temp.pdf")

        vectorstore = create_vector_store(docs)

        st.session_state.vectorstore = vectorstore

        st.sidebar.success("PDF processed successfully!")

    except Exception as e:

        st.sidebar.error(f"PDF processing failed: {e}")

vectorstore = st.session_state.vectorstore

# ---------------- Chat History ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- Chat Input ---------------- #

prompt = st.chat_input("Ask anything...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            context = ""

            # Try RAG first
            if vectorstore:

                docs = retrieve_documents(
                    vectorstore,
                    prompt
                )

                if docs:
                    context = "\n".join(
                        [doc.page_content for doc in docs]
                    )

            # If no RAG result → Web search
            if context == "":

                context = search_web(prompt)

            final_prompt = build_prompt(
                context,
                prompt,
                mode
            )

            response = chat_model.invoke(final_prompt)

            answer = response.content

            st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )