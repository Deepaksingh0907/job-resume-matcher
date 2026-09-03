# 🤖 AI Job Resume Matcher

An intelligent, AI-powered FastAPI application that analyzes and compares resumes with job descriptions using advanced NLP, machine learning, semantic embeddings, and generative AI insights.

**Get instant match scores, identify skill gaps, and receive AI-generated recommendations to improve your candidacy.**

---

## 📋 Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Technology Stack](#technology-stack)
- [Language Composition](#language-composition)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Usage Examples](#usage-examples)
- [Architecture](#architecture)
- [Known Limitations](#known-limitations)
- [Security Considerations](#security-considerations)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

### Core Analysis Capabilities
- 📄 **PDF Resume Upload**: Extract and analyze text from PDF resumes using PyMuPDF
- 📝 **Job Description Matching**: Compare resumes against job descriptions
- 🎯 **Multi-Factor Scoring**: Calculate match scores using three complementary algorithms:
  - **TF-IDF Similarity** (20% weight): Traditional text-based similarity
  - **Semantic Similarity** (40% weight): Deep learning-based contextual matching using Sentence Transformers
  - **Skill Matching** (40% weight): Precise extraction and matching of technical and soft skills

### Intelligent Insights
- 🧠 **AI-Generated Recommendations**: LLM-powered analysis providing actionable feedback
- 📊 **Skill Gap Analysis**: Identifies missing skills and strengths
- 🎤 **Interview Questions**: AI-generated practice questions tailored to the job
- 🔍 **RAG-Enhanced Context**: Retrieval-augmented generation for contextual insights

### User Management & History
- 👤 **User Authentication**: JWT-based OAuth2 authentication system
- 📚 **Analysis History**: Track all past resume-job matching analyses
- 📑 **Pagination Support**: Efficiently retrieve paginated analysis history
- 🔐 **Secure Storage**: PostgreSQL database with encrypted passwords

### User Interface
- 🎨 **Interactive Dashboard**: Modern, responsive web interface
- 🔑 **Authentication Pages**: Intuitive login and registration
- 📱 **Mobile-Friendly Design**: CSS-based responsive layout
- 🚀 **Vanilla JavaScript**: Client-side logic without heavy dependencies

### Developer Experience
- 📚 **Swagger UI**: Interactive API documentation at `/docs`
- 🔌 **RESTful API**: Clean, well-documented endpoints
- 🧪 **Health Check**: Application status monitoring

---

## 🔄 How It Works

### Resume-Job Matching Pipeline

```
┌─────────────────────────────────────────┐
│  Resume PDF + Job Description Text      │
└──────────────────┬──────────────────────┘
                   │
                   ▼
         ┌─────────────────────┐
         │  PDF Text Extraction │
         └──────────┬──────────┘
                    │
                    ▼
          ┌──────────────────────┐
          │  Text Preprocessing   │
          │  (Cleaning, stemming) │
          └──────────┬───────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
   ┌────────┐  ┌──────────┐  ┌──────────┐
   │ TF-IDF │  │ Semantic │  │  Skill   │
   │ Score  │  │ Embeddings│  │ Matching │
   └────┬───┘  └────┬─────┘  └────┬─────┘
        │           │             │
        └───────────┼─────────────┘
                    │
                    ▼
         ┌──────────────────────┐
         │ Weighted Score (0-100)│
         └──────────┬───────────┘
                    │
                    ▼
         ┌──────────────────────┐
         │   RAG Retrieval      │
         │  (Context Lookup)    │
         └──────────┬───────────┘
                    │
                    ▼
         ┌──────────────────────┐
         │   LLM Analysis       │
         │  (Optional Insights) │
         └──────────┬───────────┘
                    │
                    ▼
         ┌──────────────────────┐
         │   Final Analysis     │
         │   Result w/ Insights │
         └──────────────────────┘
```

### Scoring Formula

```
Overall Score = (TF-IDF Score × 0.20)
              + (Semantic Score × 0.40)
              + (Skill Score × 0.40)
```

---

## 🛠 Technology Stack

### Backend Framework
- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for production deployments
- **Python 3.12+**: Latest Python runtime

### Machine Learning & NLP
- **scikit-learn**: TF-IDF vectorization and similarity calculations
- **Sentence Transformers**: State-of-the-art semantic similarity models
- **PyMuPDF (fitz)**: PDF text extraction with high accuracy

### Database & ORM
- **PostgreSQL**: Robust relational database
- **SQLAlchemy 2.0+**: Modern SQL toolkit and ORM
- **Psycopg**: PostgreSQL adapter for Python

### Authentication & Security
- **PyJWT**: JWT token creation and verification
- **pwdlib + Argon2**: Secure password hashing algorithms
- **OAuth2**: Industry-standard authentication protocol

### Frontend
- **Jinja2 Templates**: Server-side HTML rendering
- **Vanilla JavaScript**: Pure client-side logic without frameworks
- **CSS3**: Modern styling and responsive design
- **HTML5**: Semantic markup

### API & LLM Integration
- **OpenRouter API**: Access to various LLM providers
- **httpx**: Async HTTP client for API calls
- **Pydantic**: Data validation and serialization

### Dependency Management
- **uv**: Fast Python package manager and resolver

---

## 📊 Language Composition

| Language   | Percentage |
|-----------|-----------|
| Python    | 45.7%     |
| JavaScript| 24.6%     |
| CSS       | 16.8%     |
| HTML      | 12.9%     |

---

## 📁 Project Structure

```
job-resume-matcher/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── analysis_routes.py      # Analysis history endpoints
│   │   ├── auth_routes.py          # User registration/login
│   │   ├── dependencies.py         # Shared dependencies (JWT verification)
│   │   ├── job_routes.py           # Job description endpoints
│   │   ├── match_routes.py         # Resume-job matching endpoints
│   │   └── resume_routes.py        # Resume extraction endpoints
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py               # Environment configuration
│   │   └── security.py             # JWT & password hashing utilities
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── analysis.py             # Analysis database model
│   │   └── user.py                 # User database model
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── analysis_history_schema.py    # Paginated history response
│   │   ├── analysis_schema.py            # Analysis response schema
│   │   ├── job_schema.py                 # Job description schema
│   │   ├── token_schema.py               # JWT token schema
│   │   └── user_schema.py                # User registration/login schema
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── llm_service.py          # LLM insight generation
│   │   ├── matching_service.py     # Core matching orchestration
│   │   ├── pdf_service.py          # PDF text extraction
│   │   ├── preprocessing_service.py # Text cleaning & normalization
│   │   ├── scoring_service.py      # Score calculation
│   │   ├── semantic_matching_service.py  # Semantic similarity
│   │   ├── skill_matching_service.py     # Skill extraction & matching
│   │   ├── skill_service.py        # Skill database operations
│   │   └── rag_service.py          # RAG retrieval system
│   │
│   ├── static/
│   │   ├── css/
│   │   │   ├── auth.css            # Login/register page styles
│   │   │   ├── common.css          # Global styles
│   │   │   └── dashboard.css       # Dashboard page styles
│   │   └── js/
│   │       ├── api.js              # API request utilities
│   │       ├── auth.js             # Authentication logic
│   │       └── dashboard.js        # Dashboard functionality
│   │
│   ├── templates/
│   │   ├── base.html               # Base template
│   │   ├── dashboard.html          # Analysis dashboard
│   │   ├── login.html              # Login page
│   │   └── register.html           # Registration page
│   │
│   ├── database.py                 # Database initialization & session management
│   ├── init_db.py                  # Database table creation
│   └── main.py                     # FastAPI application entry point
│
├── .gitignore                      # Git ignore patterns
├── .python-version                 # Python version specification
├── pyproject.toml                  # Project metadata & dependencies
├── uv.lock                         # Dependency lock file
└── README.md                       # This file
```

---

## 📦 Prerequisites

Before installing, ensure you have:

- **Python 3.12 or newer**
- **PostgreSQL 12 or newer**
- **uv package manager**
- **OpenRouter API key** (for AI insights)

### Verify Installations

```bash
python3 --version    # Should show Python 3.12+
psql --version       # Should show PostgreSQL 12+
uv --version        # Should show uv version
```

---

## 🚀 Installation

### 1. Clone Repository

```bash
git clone https://github.com/Deepaksingh0907/job-resume-matcher.git
cd job-resume-matcher
```

### 2. Install Dependencies

```bash
uv sync
```

This command:
- Creates a virtual environment
- Installs all dependencies from `pyproject.toml`
- Locks versions in `uv.lock`

### 3. PostgreSQL Setup

#### Start PostgreSQL service:

```bash
# Linux (systemd)
sudo systemctl enable --now postgresql

# macOS (Homebrew)
brew services start postgresql

# Windows
# PostgreSQL should start automatically after installation
```

#### Create database:

```bash
# Connect to PostgreSQL
sudo -u postgres psql

# Inside PostgreSQL shell
ALTER USER postgres WITH PASSWORD 'your_secure_password';
CREATE DATABASE job_resume_matcher;
\q
```

---

## ⚙️ Configuration

### Create `.env` File

Create a `.env` file in the project root (same level as `pyproject.toml`):

```bash
# Database Configuration
DATABASE_URL=postgresql+psycopg://postgres:your_secure_password@127.0.0.1:5432/job_resume_matcher

# JWT Configuration
SECRET_KEY=your-very-long-random-secret-key-minimum-32-characters
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# LLM Configuration (OpenRouter)
OPENROUTER_API_KEY=your_openrouter_api_key_here
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
LLM_MODEL=deepseek/deepseek-chat  # or another model you prefer
LLM_TIMEOUT_SECONDS=60
```

### Environment Variables Explained

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql+psycopg://user:pass@host:5432/dbname` |
| `SECRET_KEY` | Key for JWT token signing | A long random string (min 32 chars) |
| `ALGORITHM` | JWT signing algorithm | `HS256` (recommended) |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | JWT token expiration time | `30` minutes |
| `OPENROUTER_API_KEY` | API key from OpenRouter | Available from openrouter.ai |
| `OPENROUTER_BASE_URL` | OpenRouter API endpoint | `https://openrouter.ai/api/v1` |
| `LLM_MODEL` | LLM model to use | `deepseek/deepseek-chat`, `meta-llama/llama-2-70b-chat`, etc. |
| `LLM_TIMEOUT_SECONDS` | API request timeout | `60` seconds |

### Security Notes for `.env`

⚠️ **IMPORTANT**: Never commit `.env` to version control!

```bash
# The .env file is already in .gitignore, but verify:
echo ".env" >> .gitignore
```

---

## 🏗️ Initialize Database

```bash
uv run python -m app.init_db
```

This creates:
- `users` table (for authentication)
- `analyses` table (for storing analysis results)

---

## ▶️ Running the Application

### Start Development Server

```bash
uv run uvicorn app.main:app --reload
```

**Output should show:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

### Access the Application

- **Web Interface**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **API Docs (Swagger)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **API Docs (ReDoc)**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
- **Health Check**: [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)

### Production Deployment

```bash
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

---

## 📚 API Documentation

### Authentication

#### Register User
```http
POST /api/v1/auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "secure_password_8+"
}

Response: 
{
  "message": "User registered successfully"
}
```

#### Login
```http
POST /api/v1/auth/login
Content-Type: application/x-www-form-urlencoded

username=user@example.com&password=secure_password_8+

Response:
{
  "access_token": "eyJhbGc...",
  "token_type": "bearer"
}
```

### Resume Analysis

#### Extract Text from PDF
```http
POST /api/v1/resumes/extract-text
Content-Type: multipart/form-data

file: <PDF file>

Response:
{
  "text": "Extracted resume text..."
}
```

#### Analyze Resume Against Job Description
```http
POST /api/v1/matches/analyze
Authorization: Bearer <access_token>
Content-Type: multipart/form-data

file: <PDF resume>
job_description: "Job description text..."

Response:
{
  "analysis_id": "uuid",
  "overall_score": 75.5,
  "tfidf_score": 68.2,
  "semantic_score": 78.0,
  "skill_score": 80.5,
  "skill_analysis": {
    "matched_skills": ["Python", "FastAPI"],
    "missing_skills": ["Kubernetes", "Docker"],
    "additional_skills": []
  },
  "llm_insights": {
    "summary": "Strong technical foundation with some gaps...",
    "strengths": ["Python expertise", "API design knowledge"],
    "recommendations": ["Learn Docker", "Study Kubernetes basics"],
    "interview_questions": ["Explain your FastAPI experience..."]
  },
  "created_at": "2026-09-03T10:30:00"
}
```

### Analysis History

#### List User's Analyses
```http
GET /api/v1/analyses/history?skip=0&limit=10
Authorization: Bearer <access_token>

Response:
{
  "analyses": [
    {
      "analysis_id": "uuid",
      "overall_score": 75.5,
      "created_at": "2026-09-03T10:30:00"
    }
  ],
  "total": 15,
  "skip": 0,
  "limit": 10
}
```

#### View Single Analysis
```http
GET /api/v1/analyses/{analysis_id}
Authorization: Bearer <access_token>

Response: (Full analysis object as shown above)
```

### Health Check

```http
GET /health

Response:
{
  "status": "healthy",
  "service": "AI Job Resume Matcher"
}
```

---

## 💡 Usage Examples

### Example 1: Web UI Workflow

1. Visit [http://127.0.0.1:8000](http://127.0.0.1:8000)
2. Click "Create Account"
3. Enter email and password (8+ characters)
4. Log in with credentials
5. Upload resume PDF
6. Paste job description
7. Click "Analyze"
8. Review scores and AI insights

### Example 2: API Usage (cURL)

```bash
# Register
curl -X POST http://127.0.0.1:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "MySecurePass123"
  }'

# Login
TOKEN=$(curl -X POST http://127.0.0.1:8000/api/v1/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=MySecurePass123" \
  | jq -r '.access_token')

# Analyze Resume
curl -X POST http://127.0.0.1:8000/api/v1/matches/analyze \
  -H "Authorization: Bearer $TOKEN" \
  -F "file=@resume.pdf" \
  -F "job_description=Senior Python Developer required with 5+ years experience..."
```

### Example 3: Python Client

```python
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

# Register
response = requests.post(
    f"{BASE_URL}/api/v1/auth/register",
    json={"email": "user@example.com", "password": "MySecurePass123"}
)

# Login
response = requests.post(
    f"{BASE_URL}/api/v1/auth/login",
    data={"username": "user@example.com", "password": "MySecurePass123"}
)
token = response.json()["access_token"]

# Analyze
with open("resume.pdf", "rb") as resume:
    files = {"file": resume}
    data = {"job_description": "Senior Python Developer..."}
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.post(
        f"{BASE_URL}/api/v1/matches/analyze",
        files=files,
        data=data,
        headers=headers
    )
    
    result = response.json()
    print(f"Overall Score: {result['overall_score']}%")
    print(f"Matched Skills: {result['skill_analysis']['matched_skills']}")
```

---

## 🏗️ Architecture

### Component Breakdown

#### **API Layer** (`app/api/`)
- Handles HTTP requests/responses
- Implements FastAPI routes
- Manages request validation with Pydantic

#### **Services Layer** (`app/services/`)
- **matching_service.py**: Orchestrates the entire matching pipeline
- **pdf_service.py**: Extracts text from uploaded PDFs
- **preprocessing_service.py**: Cleans and normalizes text
- **scoring_service.py**: Calculates weighted overall score
- **semantic_matching_service.py**: Computes semantic similarity using Sentence Transformers
- **skill_matching_service.py**: Extracts and matches skills
- **llm_service.py**: Integrates with OpenRouter for AI insights
- **rag_service.py**: Retrieves relevant context for enhanced insights

#### **Models Layer** (`app/models/`)
- SQLAlchemy ORM models
- Maps to database tables
- Handles database queries

#### **Schemas Layer** (`app/schemas/`)
- Pydantic models for request/response validation
- Type hints and documentation
- Data serialization

#### **Security** (`app/core/security.py`)
- JWT token creation and verification
- Password hashing with Argon2
- OAuth2 implementation

#### **Frontend** (`app/static/`, `app/templates/`)
- Server-side template rendering with Jinja2
- Client-side JavaScript for interactivity
- CSS for styling

### Data Flow

```
User Request
    ↓
FastAPI Route Handler
    ↓
Request Validation (Pydantic Schemas)
    ↓
Authentication Check (JWT)
    ↓
Service Layer Processing
    ├─ PDF Text Extraction
    ├─ Text Preprocessing
    ├─ TF-IDF Scoring
    ├─ Semantic Similarity
    ├─ Skill Matching
    ├─ RAG Retrieval
    └─ LLM Insight Generation
    ↓
Database Operations (SQLAlchemy)
    ├─ Save Analysis
    ├─ Retrieve History
    └─ User Management
    ↓
Response Formatting (Pydantic Schemas)
    ↓
JSON Response to Client
```

---

## ⚠️ Known Limitations

### Current Limitations
- LLM insights are returned in responses but not stored in the database
- Using SQLAlchemy's `Base.metadata.create_all()` instead of Alembic migrations
- JWT tokens stored in browser's localStorage (not secure HttpOnly cookies)
- First Sentence Transformer model download may take time
- Score weights are default values, not tuned on labeled data
- No file size validation or rate limiting

### Future Improvements
- [ ] Implement Alembic for database migrations
- [ ] Switch to secure HttpOnly cookies for token storage
- [ ] Add file upload size validation
- [ ] Implement rate limiting
- [ ] Add comprehensive test suite
- [ ] Background job processing for large batches
- [ ] Model weight optimization using labeled data
- [ ] Support for multiple resume formats (DOCX, TXT, etc.)
- [ ] Advanced RAG with vector embeddings
- [ ] Real-time analysis progress tracking

---

## 🔐 Security Considerations

### Best Practices Implemented
✅ Password hashing with Argon2 (never store plaintext)
✅ JWT-based stateless authentication
✅ OAuth2 password bearer security scheme
✅ User isolation: analyses scoped to authenticated user
✅ HTTP-only communication (implement HTTPS in production)

### Production Recommendations
🔒 Use HTTPS with valid SSL certificates
🔒 Implement CSRF protection
🔒 Add request rate limiting
🔒 Use environment variables for secrets (never hardcode)
🔒 Set strong `SECRET_KEY` (minimum 32 random characters)
🔒 Implement secure HttpOnly cookies instead of localStorage
🔒 Add SQL injection prevention (already handled by SQLAlchemy)
🔒 Regular security audits and dependency updates
🔒 Monitor API logs for suspicious activity
🔒 Set appropriate CORS policies

### Credential Management
```bash
# Generate a secure SECRET_KEY
python -c "import secrets; print(secrets.token_urlsafe(32))"

# Store in .env (never in code)
SECRET_KEY=your_generated_secret_key_here
```

---

## 🤝 Contributing

We welcome contributions! To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Write/update tests
5. Commit: `git commit -am 'Add your feature'`
6. Push: `git push origin feature/your-feature`
7. Submit a Pull Request

### Development Setup

```bash
# Install development dependencies
uv sync --all-extras

# Run tests (when available)
uv run pytest

# Format code
uv run black app/

# Type checking
uv run mypy app/
```

---

## 📄 License

This project is currently for **learning and portfolio purposes**.

Before distributing this project publicly, please:
- [ ] Add an appropriate license (MIT, Apache 2.0, GPL, etc.)
- [ ] Update this README with license information
- [ ] Ensure compliance with all dependencies' licenses

### Recommended Licenses
- **MIT**: Permissive, great for open source
- **Apache 2.0**: Include explicit patent grants
- **GPL 3.0**: Copyleft, requires derivatives to be open source

---

## 📞 Support & Questions

- 📖 **API Documentation**: Visit `/docs` after starting the app
- 🐛 **Report Issues**: Open an issue on GitHub
- 💬 **Discussions**: Use GitHub Discussions for questions

---

## 🙏 Acknowledgments

- **FastAPI**: Modern web framework
- **Sentence Transformers**: Semantic similarity models
- **OpenRouter**: LLM API access
- **PostgreSQL**: Robust database
- **scikit-learn**: Machine learning toolkit

---

**Built with ❤️ by Deepaksingh0907**

Last Updated: September 3, 2026
