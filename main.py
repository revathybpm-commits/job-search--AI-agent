from dotenv import load_dotenv
load_dotenv()   # MUST be first

from agents.job_matcher import get_match_score
from agents.resume_tailor import tailor_resume
from agents.cover_letter import generate_cover_letter
from agents.tracker import save_application

# Load resume
with open("resumes/resume.txt", "r") as f:
    resume = f.read()

# Example job description
job_description = """
Looking for a Python developer with experience in AI, automation, and data processing.
"""

score = get_match_score(job_description, resume)
tailored_resume = tailor_resume(job_description, resume)
cover_letter = generate_cover_letter(job_description, resume)

# Save outputs
with open("outputs/tailored_resume.txt", "w") as f:
    f.write(tailored_resume)

with open("outputs/cover_letter.txt", "w") as f:
    f.write(cover_letter)

save_application({
    "role": "Python Developer",
    "company": "Example कंपनी",
    "score": score
})

print("✅ Application processed!")
print("Match Score:", score)
