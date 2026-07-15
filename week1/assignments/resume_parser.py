import os
import json
from dotenv import load_dotenv
from groq import Groq
from pypdf import PdfReader
from pydantic import BaseModel

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found!")

client = Groq(api_key=api_key)

reader = PdfReader("resume (4).pdf")

resume_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        resume_text += text + "\n"


class Resume(BaseModel):
    name: str
    email: str
    skills: list[str]
    experience: int
    internships: int
    projects: list[str]
    achievements: list[str]


schema = Resume.model_json_schema()

system_prompt = f"""
You are an expert resume parser.

Extract the following information from the resume.

- name
- email
- skills
- experience
- internships
- projects
- achievements

Return ONLY a valid JSON object matching this schema.

{schema}
"""

messages = [
    {
        "role": "system",
        "content": system_prompt
    },
    {
        "role": "user",
        "content": f"""
Extract the required information from this resume.

Resume:

{resume_text}
"""
    }
]

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages,
    response_format={"type": "json_object"},
    temperature=0
)

answer = response.choices[0].message.content

print(answer)

data = json.loads(answer)

resume = Resume(**data)

print(resume.name)
print(resume.email)
print(resume.skills)
print(resume.experience)
print(resume.internships)
print(resume.projects)
print(resume.achievements)