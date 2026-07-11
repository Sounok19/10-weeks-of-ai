# Day 3 - Understanding Token Usage and Response Limits

## Overview

This project explores how Large Language Models (LLMs) use tokens and how the `max_tokens` parameter affects the generated response.

Multiple prompts of varying lengths are sent to the Groq API, and the program analyzes the token usage returned by the model.

---

## Concepts Learned

- Prompt Tokens
- Completion Tokens
- Total Tokens
- `max_tokens` parameter
- Finish Reasons
- Iterating through multiple prompts

---

## Project

The application sends three different prompts to the Llama 3.3 70B Versatile model:

1. A simple greeting
2. A short explanatory question
3. A long essay request

For each prompt, it displays:

- Prompt Tokens
- Completion Tokens
- Total Tokens
- Finish Reason

This helps understand how different prompts consume tokens and how response generation is affected by token limits.

---

## Tech Stack

- Python
- Groq API
- python-dotenv

---

## Run

Install dependencies:

```bash
pip install groq python-dotenv
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Run the program:

```bash
python tokens.py
```

---

## Sample Output

```text
Prompt: Hi!
Prompt Tokens: 9
Completion Tokens: 8
Total Tokens: 17
Finish Reason: stop
```

---

## Learning Outcome

- Learned how LLMs count tokens.
- Understood the relationship between prompt length and token usage.
- Explored the effect of the `max_tokens` parameter.
- Learned how to inspect API usage statistics using the Groq SDK.