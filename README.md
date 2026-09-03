  AI Job Resume Matcher

An AI-powered FastAPI application that compares a resume with a job description and explains how well they match.

The application combines traditional NLP, machine learning, semantic embeddings, skill matching, PostgreSQL, JWT authentication, and an optional OpenRouter LLM explanation layer.

Features

Upload and extract text from PDF resumes.

Clean and normalize resume and job-description text.

Calculate TF-IDF similarity.

Calculate semantic similarity using Sentence Transformers.

Extract resume and job skills using keyword aliases and regular expressions.

Show matched and missing skills.

Calculate a weighted overall match score.

Generate AI-based strengths, recommendations, and interview questions.

Register and authenticate users with JWT.

Store analysis results in PostgreSQL.

View analysis history for the authenticated user.

Simple Jinja2, CSS, and vanilla JavaScript frontend.

Interactive API documentation through Swagger UI.

How matching works

The analysis pipeline is:

Resume PDF + Job Description
              |
              v
       PDF text extraction
              |
              v
        Text preprocessing
              |
      +-------+--------+
      |                |
      v                v
   TF-IDF       Semantic embeddings
      |                |
      +-------+--------+
              v
        Skill matching
              |
              v
      Weighted overall score
              |
              v
       Optional LLM insights

The overall score uses the following initial weights:

Overall score = (TF-IDF score × 0.20)
              + (Semantic score × 0.40)
              + (Skill score × 0.40)

The numerical score is calculated by Python. The LLM is used to explain the result and provide recommendations.

Technology stack

Python 3.12+

FastAPI and Uvicorn

PostgreSQL, SQLAlchemy, and Psycopg

PyMuPDF

scikit-learn

Sentence Transformers

Pydantic and pydantic-settings

JWT with PyJWT

Password hashing with pwdlib and Argon2

OpenRouter-compatible LLM API

Jinja2

HTML, CSS, and vanilla JavaScript

uv for dependency management

Project structure

app/
├── api/
│   ├── analysis_routes.py
│   ├── auth_routes.py
│   ├── dependencies.py
│   ├── job_routes.py
│   ├── match_routes.py
│   └── resume_routes.py
│
├── core/
│   ├── config.py
│   └── security.py
│
├── models/
│   ├── __init__.py
│   ├── analysis.py
│   └── user.py
│
├── schemas/
│   ├── analysis_history_schema.py
│   ├── analysis_schema.py
│   ├── job_schema.py
│   ├── token_schema.py
│   └── user_schema.py
│
├── services/
│   ├── llm_service.py
│   ├── matching_service.py
│   ├── pdf_service.py
│   ├── preprocessing_service.py
│   ├── scoring_service.py
│   ├── semantic_matching_service.py
│   ├── skill_matching_service.py
│   └── skill_service.py
│
├── static/
│   ├── css/
│   │   ├── auth.css
│   │   ├── common.css
│   │   └── dashboard.css
│   └── js/
│       ├── api.js
│       ├── auth.js
│       └── dashboard.js
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── login.html
│   └── register.html
│
├── database.py
├── init_db.py
└── main.py

Prerequisites

Install:

Python 3.12 or newer

PostgreSQL

uv

An OpenRouter API key for AI insights

Check the installations:

python3 --version
psql --version
uv --version

Installation

git clone <your-repository-url>
cd job-resume-matcher
uv sync

PostgreSQL setup

Start PostgreSQL:

sudo systemctl enable --now postgresql

Open the PostgreSQL shell:

sudo -u postgres psql

Create the database and set a password:

ALTER USER postgres WITH PASSWORD 'your_password';
CREATE DATABASE job_resume_matcher;
\q

Environment variables

Create a .env file in the project root, beside pyproject.toml:

DATABASE_URL=postgresql+psycopg://postgres:your_password@127.0.0.1:5432/job_resume_matcher

SECRET_KEY=replace-with-a-long-random-secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
LLM_MODEL=provider/model-name
LLM_TIMEOUT_SECONDS=60

Never commit .env or expose the API key publicly.

Create database tables

uv run python -m app.init_db

This creates the users and analyses tables.

Run the application

uv run uvicorn app.main:app --reload

Open the application at:

http://127.0.0.1:8000/

Swagger documentation is available at:

http://127.0.0.1:8000/docs

Application routes

Web pages

Method

Path

Purpose

GET

/

Login page

GET

/register

Registration page

GET

/dashboard

Resume analysis dashboard

GET

/health

Application health check

Authentication API

Method

Path

Purpose

POST

/api/v1/auth/register

Create a user account

POST

/api/v1/auth/login

Login and receive a JWT

The login endpoint uses OAuth2 form fields:

username = user email
password = user password

Resume and matching API

Method

Path

Authentication

Purpose

POST

/api/v1/resumes/extract-text

Not required

Extract text from a PDF

POST

/api/v1/matches/analyze

Bearer token

Analyze a resume against a job description

The matching request uses multipart form data:

file            = resume PDF
job_description = job description text

Analysis history API

Method

Path

Authentication

Purpose

GET

/api/v1/analyses/history

Bearer token

List the current user's analyses

GET

/api/v1/analyses/{analysis_id}

Bearer token

View one analysis

Example:

GET /api/v1/analyses/history?skip=0&limit=10

Authentication flow

Register → Login → Receive JWT → Send Bearer token → Use protected APIs

Each analysis is associated with the authenticated user's ID. History and detail queries are filtered by that user ID.

LLM behavior

The LLM receives:

Cleaned resume text

Cleaned job description

TF-IDF score

Semantic score

Skill analysis

It returns:

A short summary

Resume strengths

Recommendations

Interview questions

The LLM integration is fail-safe. If the API key is missing, the model is invalid, or the request fails, the core ML scores are still returned.

Limitations and future improvements

LLM insights are currently returned in the analysis response but are not stored in the analyses table.

Base.metadata.create_all() is used for initial table creation; Alembic migrations should be added for production.

The frontend stores the JWT in browser storage for learning purposes. Production systems should consider secure HttpOnly cookies.

The first Sentence Transformer request may download the model and take longer.

Score weights should be evaluated with real labelled resume-job data.

File-size validation, rate limiting, background processing, and automated tests can be added.

Security notes

Do not commit .env.

Do not log API keys or passwords.

Store password hashes, never plain-text passwords.

Use a strong SECRET_KEY outside local development.

Validate uploaded files and limit upload sizes in production.

Keep analysis-history queries scoped to the authenticated user.

License

This project is currently for learning and portfolio purposes. Add a license before distributing it publicly.
