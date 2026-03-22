import streamlit as st
import os
from dotenv import load_dotenv

from agents.job_matcher import get_match_score
from agents.resume_tailor import tailor_resume
from agents.cover_letter import generate_cover_letter

# ✅ Load environment variables
load_dotenv()

# Optional: Debug (remove later)
if not os.getenv("OPENAI_API_KEY"):
    st.error("❌ OPENAI_API_KEY is not set. Please check your .env file.")

st.set_page_config(page_title="AI Job Search Copilot", layout="wide")

st.title("🚀 AI Job Search Copilot")
st.write("Automate your job applications with AI")

# Inputs
st.header("📄 Input")

resume = st.text_area("Paste your Resume", height=200)
job_desc = st.text_area("Paste Job Description", height=200)

if st.button("✨ Generate Application Materials"):

    if resume and job_desc:

        with st.spinner("Processing..."):

            try:
                score = get_match_score(job_desc, resume)
                tailored_resume = tailor_resume(job_desc, resume)
                cover_letter = generate_cover_letter(job_desc, resume)

                st.success("Done!")

                # Output
                st.header("📊 Results")

                st.subheader("Match Score")
                st.write(score)

                st.subheader("Tailored Resume")
                st.text_area("", tailored_resume, height=300)

                st.subheader("Cover Letter")
                st.text_area("", cover_letter, height=300)

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

    else:
        st.warning("Please provide both resume and job description.")
