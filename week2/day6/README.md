# Day 6 - Prompt Engineering

## Overview

This project classifies a customer support complaint into a predefined category using a structured prompt and the Groq API.

## Workflow

User Complaint  
↓  
Structured Prompt (Role, Task, Constraints, Output Format)  
↓  
Groq API (Llama 3.3 70B Versatile)  
↓  
Predicted Category

## Categories

- Billing
- Technical
- Return
- Other

## Tech Stack

- Python
- Groq API
- python-dotenv

## Run

```bash
python main.py
```

## Learning

- Structured Prompting
- Role Prompting
- Prompt Constraints
- Text Classification