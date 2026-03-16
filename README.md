# Agentic Business Intelligence System

AI system that automatically analyzes datasets and generates business insights using LLM agents.

Upload a CSV → the system cleans the data, performs analysis, builds charts, and explains insights in plain English.

🚀 Features

Upload any CSV dataset

Automatic data cleaning

Statistical analysis and trend detection

AI-generated business insights

Interactive dashboards with charts

Natural language Q&A on data (RAG)

PDF report export

🛠 Tech Stack

Python

Streamlit – UI dashboard

LangChain – agent orchestration

LLMs – Gemini / Groq / Ollama

ChromaDB – vector database for RAG

Pandas & NumPy – data processing

Plotly – visualizations

📁 Project Structure
Agentic_BI/
│
├── app.py
├── agents/
│   ├── orchestrator.py
│   ├── cleaner_agent.py
│   ├── analyst_agent.py
│   ├── insight_agent.py
│   └── visualizer_agent.py
│
├── rag/
│   └── vector_store.py
│
├── utils/
│   └── llm_factory.py
│
├── requirements.txt
└── README.md
⚡ Run Locally

Clone the repository

git clone https://github.com/Ahana19/AI_Analyst_Agent.git
cd AI_Analyst_Agent

Install dependencies

pip install -r requirements.txt

Run the app

streamlit run app.py

Open in browser:

http://localhost:8501
🎯 How It Works

Upload a dataset (CSV)

The system cleans and analyzes the data

AI generates business insights

Charts and dashboard are created automatically

Users can ask questions about the data

t pipeline orchestrated by LangChain:
![Dashboard]("C:\Users\KIIT\OneDrive\Desktop\Agentic_BI\agentic_bi_architecture.png")
