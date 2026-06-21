# ==================================================
# IMPORTS
# ==================================================

import streamlit as st

from langchain_community.vectorstores import FAISS
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI
)
from langchain_core.prompts import PromptTemplate


# ==================================================
# API KEY
# ==================================================

from dotenv import load_dotenv
import os

load_dotenv()

google_api_key = os.getenv("GEMINI_API_KEY")

print(google_api_key)


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Mohar's Assistant",
    page_icon="🤖",
    layout="wide"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1 {
    text-align: center;
    color: #00E5FF;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #CCCCCC;
    margin-top: -10px;
    margin-bottom: 30px;
}

.stChatMessage {
    border-radius: 15px;
    padding: 10px;
}

.answer-box {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #00E5FF;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# HEADER
# ==================================================

st.title("Get to Know Mohar Mukherjee")

st.markdown("""
<div class="subtitle">
    Ask questions about my skills, projects, education, and experience.
</div>
""", unsafe_allow_html=True)

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("Mohar's Assistant")

    st.markdown("---")

    st.subheader("Tech Stack")

    st.markdown("""
    - LangChain
    - Gemini
    - FAISS
    - Streamlit
    - Google Embeddings
    """)

    st.markdown("---")

    st.subheader("Example Questions")

    st.write("• What are my skills?")
    st.write("• Tell me about my projects")
    st.write("• Summarize my education")


# ==================================================
# CHAT HISTORY
# ==================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ==================================================
# LOAD EMBEDDINGS
# ==================================================

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-2",
    google_api_key=google_api_key
)


# ==================================================
# LOAD VECTOR DB
# ==================================================

vectorstore = FAISS.load_local(
    "faiss_db",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)


# ==================================================
# LOAD LLM
# ==================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    google_api_key=google_api_key,
    temperature=0
)


# ==================================================
# PROMPT TEMPLATE
# ==================================================

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a resume assistant.

Answer ONLY from the provided context.

If the answer is not present,
say:
"Information not available. Sorry"

Context:
{context}

Question:
{question}

Answer:
"""
)


# ==================================================
# USER INPUT
# ==================================================

question = st.chat_input(
    "Ask a question about the resume"
)


# ==================================================
# MAIN RAG PIPELINE
# ==================================================

if question and question.strip():

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("Thinking..."):

        # Retrieve documents
        docs = retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        # Create prompt
        final_prompt = prompt.format(
            context=context,
            question=question
        )

        # Generate response
        response = llm.invoke(final_prompt)

        # Extract answer
        if isinstance(response.content, list):

            answer = ""

            for item in response.content:

                if (
                    isinstance(item, dict)
                    and item.get("type") == "text"
                ):
                    answer += item.get("text", "")

        else:
            answer = response.content

    # Display assistant response
    with st.chat_message("assistant"):

        st.markdown(
            f"""
            <div class="answer-box">
                {answer}
            </div>
            """,
            unsafe_allow_html=True
        )

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
