import os
from openai import OpenAI
import pandas as pd

# ✅ Job matching function
def get_match_score(job_desc, resume):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"""
    Compare the resume and job description.
    Return only a number from 1-10.

    Resume:
    {resume}

    Job:
    {job_desc}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()


# ✅ Application tracker function
def save_application(data):
    df = pd.DataFrame([data])

    try:
        existing = pd.read_csv("outputs/applications.csv")
        df = pd.concat([existing, df], ignore_index=True)
    except FileNotFoundError:
        # File doesn't exist yet → first save
        pass

    df.to_csv("outputs/applications.csv", index=False)
