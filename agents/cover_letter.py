from openai import OpenAI
import os

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


def generate_cover_letter(job_desc, resume):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # ✅ FIXED

    prompt = f"""
    Write a short professional cover letter.

    Resume:
    {resume}

    Job:
    {job_desc}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
