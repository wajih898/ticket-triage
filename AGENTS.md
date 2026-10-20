Project: AI Support Ticket Triage
What this is
A Python app that triages support tickets with an LLM: redact PII,
classify, summarize, draft a reply, store, and show on a dashboard
for human approval.

Stack
Python 3.11, uv, Pydantic v2, FastAPI, SQLAlchemy + SQLite,
Streamlit, pytest, ruff, mypy.

Rules
Never hardcode secrets. Read config only from app/config.py,
which loads .env.

Never send raw ticket text to the LLM. Always call
app.redact.redact() first.

Never log ticket text or PII. Log ticket IDs only.
All LLM output must be parsed into a Pydantic model. Never trust
raw LLM text.

Prompts live in app/prompts/ as versioned .md files, not inline
strings.

Type hints on every function. Small functions, clear names.
Every new module gets tests in tests/. Mock the LLM in unit tests.
Before finishing a task, run: ruff check . && mypy app && pytest
Working style
For any task bigger than one function: propose a plan first and
wait for approval.

Do not add new dependencies without asking.
Do not modify files outside the task's scope.