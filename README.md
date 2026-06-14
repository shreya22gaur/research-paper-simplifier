# 📚 AI Research Paper Simplifier

🚀 Live Demo: https://research-paper-simplifier-1.onrender.com

An AI-powered web application that simplifies research papers by generating concise summaries, extracting key contributions, explaining methodologies, identifying limitations, suggesting future work, and generating interview questions.

Built using **Streamlit**, **Groq API**, and **PyPDF**.

## 🚀 Features

* Upload research papers in PDF format
* Generate an executive summary
* Extract key contributions and findings
* Explain methodology in simple language
* Identify limitations and future scope
* Generate interview questions based on the paper
* User-friendly Streamlit interface
* Deployable on Render

## 🛠️ Tech Stack

* Python
* Streamlit
* Groq API (Llama Models)
* PyPDF
* Python Dotenv

## 📂 Project Structure

```text
research-paper-simplifier/
│
├── app.py
├── requirements.txt
├── render.yaml
├── .env
└── README.md
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/research-paper-simplifier.git
cd research-paper-simplifier
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

## ▶️ Run Locally

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

## 📖 How It Works

1. Upload a research paper PDF.
2. The application extracts text from the document.
3. The extracted content is sent to a Large Language Model via the Groq API.
4. The model generates:

   * Executive Summary
   * Key Contributions
   * Methodology Explanation
   * Main Findings
   * Limitations
   * Future Scope
   * Interview Questions

## 🎯 Use Cases

* Students studying research papers
* Researchers reviewing literature
* Interview preparation
* Academic project analysis
* Quick understanding of complex publications

## 📸 Future Improvements

* Flashcard Generation
* MCQ Generation
* PDF Report Export
* Citation Extraction
* Multi-Paper Comparison
* Research Trend Analysis

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.


This project is open-source and available under the MIT License.
