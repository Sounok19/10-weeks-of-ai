import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Error")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"

def llm_ans(prompt):
    message={
        "role":"user",
        "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model,messages=messages)
    ans=response.choices[0].message.content
    return ans

bad_prompt="""
#Role:
You are a support assisstant at a mobile/laptop company
#TASK:
You have to classify the issue in a category
#CONSTRAINT:
You have to classify the issue in one of the three categories namely billing,technical,return
#OUTPUT FORMAT:
Your answer should be in one word only.The one word should be one of the categories given in constraints
#Example:
For instance if a user complain says he wants a refund then the category is Refund
#FALLBACK:
If the issue is unrelated to any of the categories mentioned in constraints,then the answer should be OTHER
This is a user complaint:
My laptop is not working
"""

print(llm_ans(bad_prompt))