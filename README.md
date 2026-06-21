# 🤖 Resume-Based AI Assistant (RAG)

A personalized AI-powered chatbot that can answer questions about my skills, education, projects, experience, and achievements by reading and understanding my resume.

---

# 📌 Project Overview

Traditional AI chatbots are trained on large amounts of public data but do not know anything about a specific individual. If someone asks:

* What are your technical skills?
* What projects have you completed?
* What is your educational background?
* What experience do you have with AI?

A normal chatbot cannot answer accurately because it has never seen your resume.

This project solves that problem by creating a personalized AI assistant that uses my resume as its knowledge source.

The system reads my resume, stores its information in a searchable format, and retrieves the most relevant content whenever a question is asked. It then uses a Large Language Model (LLM) to generate an accurate response based only on the information found in the resume.

---

# 🎯 Problem Statement

Most chatbots have no knowledge about an individual's:

* Skills
* Education
* Projects
* Experience
* Certifications
* Achievements

As a result, they either:

* Provide incorrect answers
* Generate generic responses
* Hallucinate information

This project addresses this limitation by implementing a Retrieval-Augmented Generation (RAG) pipeline that grounds responses in resume data.

---

# 💡 What is RAG?

RAG stands for:

**Retrieval-Augmented Generation**

It combines:

### Retrieval

Finding the most relevant information from a document.

### Generation

Using an AI model to generate an answer based on that retrieved information.

Instead of relying solely on the AI model's memory, the model first looks up relevant resume content and then answers.

This significantly improves accuracy and reduces hallucinations.

---

# 🧠 How the System Works

The workflow of the application is shown below:

```text
Resume PDF
     │
     ▼
Document Loader
     │
     ▼
Text Splitter
     │
     ▼
Embeddings
     │
     ▼
FAISS Vector Database
     │
     ▼
Retriever
     │
     ▼
Large Language Model (Gemini)
     │
     ▼
Generated Answer
```

---

# 🔄 Step-by-Step Working

## Step 1: Upload Resume

The application loads a resume in PDF format.

Example:

```text
resume.pdf
```

---

## Step 2: Extract Text

The PDF content is extracted using LangChain document loaders.

Example:

```text
Education
Skills
Projects
Experience
Achievements
```

---

## Step 3: Split Text into Chunks

Large documents are divided into smaller sections called chunks.

Example:

```text
Chunk 1 → Education

Chunk 2 → Skills

Chunk 3 → Projects

Chunk 4 → Experience
```

This helps retrieve relevant information efficiently.

---

## Step 4: Generate Embeddings

Each chunk is converted into a numerical representation called an embedding.

Embeddings allow the system to understand the meaning of text rather than just matching keywords.

Example:

```text
Python Developer
        ↓
[0.23, 0.71, -0.11, ...]
```

---

## Step 5: Store in FAISS

The embeddings are stored in a vector database called FAISS.

FAISS enables extremely fast similarity search.

---

## Step 6: User Asks a Question

Example:

```text
What machine learning projects have you completed?
```

---

## Step 7: Retrieve Relevant Information

The retriever searches the vector database and finds the most relevant resume sections.

Example:

```text
Projects Section
Machine Learning Project
AI Project
```

---

## Step 8: Generate Final Answer

The retrieved content is sent to the Gemini LLM.

The model generates an answer using only the retrieved information.

Example:

```text
You have completed InstaMed, a medicine recommendation and information retrieval system that utilizes machine learning concepts.
```

---

# ✨ Features

### Resume-Aware Chatbot

Answers questions based only on resume content.

### Semantic Search

Understands meaning rather than matching exact keywords.

### AI-Powered Responses

Uses Google's Gemini model for intelligent answers.

### Fast Retrieval

FAISS enables rapid document search.

### Modern Dashboard

Built with Streamlit.

### Hallucination Reduction

Answers are grounded in retrieved resume content.

### Chat Interface

Users can interact naturally like ChatGPT.

### Source Retrieval

Shows the resume sections used to generate answers.

---

# 🛠️ Technology Stack

| Technology        | Purpose                   |
| ----------------- | ------------------------- |
| Python            | Core Programming Language |
| LangChain         | RAG Pipeline              |
| Gemini            | Large Language Model      |
| Google Embeddings | Text Vectorization        |
| FAISS             | Vector Database           |
| Streamlit         | Dashboard Interface       |
| PDF Loader        | Resume Extraction         |

---

# 📂 Project Structure

```text
Resume-AI-Assistant/
│
├── data/
│   └── resume.pdf
│
├── faiss_db/
│
├── app.py
│
├── resume_rag.ipynb
│
├── requirements.txt
│
├── .env
│
└── README.md
```

---

# 🚀 Installation Guide

## Clone Repository

```bash
git clone https://github.com/yourusername/resume-ai-assistant.git
```

```bash
cd resume-ai-assistant
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv myvenv
```

Activate:

```bash
myvenv\Scripts\activate
```

---

### Linux / Mac

```bash
python3 -m venv myvenv
```

Activate:

```bash
source myvenv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
```

Never upload your API key to GitHub.

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 💬 Example Questions

### Skills

```text
What are my technical skills?
```

### Education

```text
Summarize my educational background.
```

### Projects

```text
Tell me about my projects.
```

### Programming Languages

```text
What programming languages do I know?
```

### AI Experience

```text
What experience do I have with Generative AI?
```

---

# 📸 Dashboard Features

The dashboard includes:

* Interactive chat interface
* Sidebar navigation
* Suggested questions
* Resume source display
* Modern UI design
* Real-time responses

---

# 🎓 Learning Outcomes

Through this project, I learned:

### Retrieval-Augmented Generation (RAG)

How AI systems combine retrieval and generation.

### LangChain

Building end-to-end LLM applications.

### Vector Databases

Using FAISS for semantic search.

### Embeddings

Representing text numerically.

### Prompt Engineering

Designing effective prompts.

### Streamlit

Developing interactive AI dashboards.

### Generative AI

Integrating Large Language Models into real-world applications.

---

# 🔥 Future Improvements

### Resume Upload Feature

Allow users to upload any resume dynamically.

### Conversation Memory

Remember previous questions.

### Multi-PDF Support

Answer questions across multiple documents.

### Voice Assistant

Speech-to-text interaction.

### Authentication

User login and profile management.

### Cloud Deployment

Deploy on Streamlit Cloud, AWS, or Render.

---

# 📊 Key Highlights

✅ Personalized AI Assistant

✅ Resume-Based Question Answering

✅ Retrieval-Augmented Generation (RAG)

✅ LangChain Implementation

✅ Gemini Integration

✅ FAISS Vector Database

✅ Streamlit Dashboard

✅ Semantic Search

✅ Reduced Hallucinations

✅ Real-World Generative AI Application

---

# 👨‍💻 Author

Mohar Mukherjee

Aspiring AI/ML Engineer passionate about Artificial Intelligence, Machine Learning, Generative AI, and building practical AI-powered applications.

Demo Link - https://personal-profile-rag.streamlit.app/

---

# ⭐ If you found this project helpful, consider giving it a star!
