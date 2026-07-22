import os
import json
from dotenv import load_dotenv
from groq import Groq
from pypdf import PdfReader
from pydantic import BaseModel,Field
from pathlib import Path

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found!")

client = Groq(api_key=api_key)

job_description="""
If you are interested in this position, please apply on Twitch's Career site https://www.twitch.tv/jobs/en/

About Us:

Twitch is the world’s biggest live streaming service, with global communities built around gaming, entertainment, music, sports, cooking, and more. It is where thousands of communities come together for whatever, every day.
We’re about community, inside and out. You’ll find coworkers who are eager to team up, collaborate, and smash (or elegantly solve) problems together. We’re on a quest to empower live communities, so if this sounds good to you, see what we’re up to on LinkedIn and X,  and discover the projects we’re solving on our Blog. Be sure to explore our Interviewing Guide to learn how to ace our interview process.

About the Role

Join Twitch's Commerce Engineering organization, where we're revolutionizing how viewers engage with their favorite creators. We are the teams behind Subscriptions, Gifting, Bits, Hype Train and Turbo products. From experimental features to established systems used by millions, we're constantly pushing the boundaries of what's possible in live streaming.

This position and team are based in Seattle, WA and San Francisco, CA

You Will
- Craft immersive, interactive experiences that keep viewers supporting creators while engaging with the Twitch Community.
- Architect and build robust, scalable applications that can handle millions of concurrent users
- Collaborate across teams to create cohesive solutions that drive business impact
- Transform customer feedback into innovative features that enhance the Twitch experience
Perks
- Medical, Dental, Vision & Disability Insurance
- 401(k)
- Maternity & Parental Leave
- Flexible PTO
- Amazon Employee Discount

Basic Qualifications
- 1+ years of non-internship professional software development experience
- 0-2 years of professional software development experience
- Excellent verbal and written communication skills; Ability to effectively collaborate with teammates is critical to success.
- A track record of building consumer-facing products that users love
- Demonstrable experience of modern programming languages and frameworks
- Sharp problem-solving skills with a focus on algorithms, data structures, and schema design
- Bachelor's degree in Computer Science or equivalent real-world experience

Preferred Qualifications
- Bachelor's degree in computer science or equivalent
- Experience with mobile development, either native or hybrid
- Familiarity with AWS infrastructure
- Experience with email / notifications technologies
- Experience writing Go in production systems

Twitch is an equal opportunity employer and does not discriminate on the basis of protected veteran status, disability, or other legally protected status.

Los Angeles County applicants: Job duties for this position include: work safely and cooperatively with other employees, supervisors, and staff; adhere to standards of excellence despite stressful conditions; communicate effectively and respectfully with employees, supervisors, and staff to ensure exceptional customer service; and follow all federal, state, and local laws and Company policies. Criminal history may have a direct, adverse, and negative relationship with some of the material job duties of this position. These include the duties and responsibilities listed above, as well as the abilities to adhere to company policies, exercise sound judgment, effectively manage stress and work safely and respectfully with others, exhibit trustworthiness and professionalism, and safeguard business operations and the Company’s reputation. Pursuant to the Los Angeles County Fair Chance Ordinance, we will consider for employment qualified applicants with arrest and conviction records.

Pursuant to the San Francisco Fair Chance Ordinance, we will consider for employment qualified applicants with arrest and conviction records.

Our inclusive culture empowers Amazonians to deliver the best results for our customers. If you have a disability and need a workplace accommodation or adjustment during the application and hiring process, including support for the interview or onboarding process, please visit https://amazon.jobs/content/en/how-we-hire/accommodations for more information. If the country/region you’re applying in isn’t listed, please contact your Recruiting Partner.


The base salary range for this position is listed below. Your Amazon package will include sign-on payments and restricted stock units (RSUs). Final compensation will be determined based on factors including experience, qualifications, and location. Amazon also offers comprehensive benefits including health insurance (medical, dental, vision, prescription, Basic Life & AD&D insurance and option for Supplemental life plans, EAP, Mental Health Support, Medical Advice Line, Flexible Spending Accounts, Adoption and Surrogacy Reimbursement coverage), 401(k) matching, paid time off, and parental leave. Learn more about our benefits at https://amazon.jobs/en/benefits.


"""
class jobD(BaseModel):
    role:str
    required_skills:list[str]
    preferred_skills:list[str]
    minimum_experience:float|None
    education_requirements:list[str]
    responsibilities:list[str]
jobd_schema:jobD.model_json_schema
system_prompt=f"""
You are an expert HR assistant.

Your job is to analyze job descriptions and extract
structured information from them.

Return ONLY valid JSON matching this schema:

{jobd_schema}
IMPORTANT:
Do NOT return the schema itself.
Do NOT return fields like "properties", "title" or "type".
Fill the schema with actual information extracted from the job description.

If minimum experience is not mentioned, return null.
If information for a list is missing, return an empty list.
Do not invent information.
"""

user_prompt = f"""
Analyze the following job description:

{job_description}
"""
message_system={
    "role" : "system",
    "content" : system_prompt
}
message_user={
    "role" : "user",
    "content" : user_prompt
}
response_format={
    "type" : "json_object"
}
messages=[message_system, message_user]

response=client.chat.completions.create(model=model, messages=messages, response_format=response_format)
answer=response.choices[0].message.content

raw_json=answer

job_data=json.loads(raw_json)

job = jobD(**job_data)

print(job.minimum_experience)
print(job.education_requirements)

answer=response.choices[0].message.content

raw_json=answer

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