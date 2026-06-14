import streamlit as st

from pypdf import PdfReader
import os

from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

st.set_page_config(
    page_title="Research Paper Simplifier",
    page_icon="📚"
)

st.title("📚 AI Research Paper Simplifier")

uploaded_file = st.file_uploader(
    "Upload Research Paper PDF",
    type=["pdf"]
)

if uploaded_file:

    reader = PdfReader(uploaded_file)

    paper_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            paper_text += text

    st.success("Paper Uploaded Successfully!")

    if st.button("Analyze Paper"):

        with st.spinner("Analyzing..."):

            prompt = f"""
You are a research assistant.

Analyze this research paper.

Provide:

1. Executive Summary (200 words)
2. Key Contributions
3. Methodology Explained Simply
4. Main Findings
5. Limitations
6. Future Scope
7. 5 Interview Questions Based on Paper

Research Paper:
{paper_text[:15000]}
"""

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3
            )

            st.markdown(response.choices[0].message.content)