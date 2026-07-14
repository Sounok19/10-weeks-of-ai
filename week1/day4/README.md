# Day 4 - Structured JSON Output with Pydantic

## 📌 Overview

Today I learned how to generate structured JSON responses from a Large Language Model (LLM) and validate them using **Pydantic**.

Instead of working with plain text responses, I instructed the model to return JSON objects that match a predefined schema. I then parsed and validated the response before using it in my application.

---

## 🚀 Topics Covered

* Structured JSON generation
* JSON response formatting
* Pydantic models
* Schema generation using `model_json_schema()`
* Parsing JSON with Python
* Validating LLM outputs
* Error handling with Pydantic
* Working with the Groq Chat Completions API

---

## 🛠️ Technologies Used

* Python
* Groq API
* Pydantic
* JSON
* python-dotenv

---

## 📂 Project

### Customer Support Ticket Extraction

Created a simple AI-powered information extraction system that converts an unstructured customer support ticket into a structured JSON object.

### Input

```text
Hello, my name is Pratyush.
My iPhone is not working at all.
My email is abc@gmail.com.
```

### Expected Output

```json
{
  "name": "Pratyush",
  "email": "abc@gmail.com",
  "issue": "iPhone is not working at all"
}
```

---

## 📋 Pydantic Schema

```python
from pydantic import BaseModel

class Ticket(BaseModel):
    name: str
    email: str
    issue: str
```

---

## 🔄 Workflow

1. Create a Pydantic model.
2. Generate a JSON schema from the model.
3. Send the schema to the LLM through a system prompt.
4. Receive a JSON response.
5. Parse the JSON using Python.
6. Validate it using Pydantic.
7. Use the validated data safely in the application.

---

## 💡 Key Learnings

* LLMs can generate structured data instead of plain text.
* `response_format={"type": "json_object"}` ensures valid JSON but does not guarantee every required field is present.
* Pydantic validates whether the returned JSON matches the expected schema.
* If required fields are missing, Pydantic raises a `ValidationError`, helping catch incomplete model outputs early.

---

## 📚 Future Improvements

* Extract data from PDF and Word resumes.
* Compare extracted skills with a job description.
* Calculate a resume-to-job match percentage.
* Explore stricter structured output techniques such as JSON Schema support.

---

## 👨‍💻 Author

**Sounok Ghosh**
