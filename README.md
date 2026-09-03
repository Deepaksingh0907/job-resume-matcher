# 🤖 AI Job Resume Matcher

An AI-powered FastAPI application that intelligently compares resumes with job descriptions using advanced NLP, machine learning, semantic embeddings, and generative AI. Get detailed match scores, identify skill gaps, and receive personalized AI-generated recommendations to improve your candidacy.

## ✨ Features

**Core Analysis**
- 📄 Upload and extract text from PDF resumes using PyMuPDF
- 📝 Compare resumes against job descriptions
- 🎯 Three-factor scoring system:
  - TF-IDF similarity (20% weight) - Traditional text matching
  - Semantic similarity (40% weight) - Deep learning contextual matching using Sentence Transformers
  - Skill matching (40% weight) - Extract and match technical/soft skills

**Intelligent Insights**
- 🤖 AI-powered LLM analysis with personalized recommendations
- 📊 Detailed skill gap analysis (matched vs missing skills)
- 🎤 AI-generated interview preparation questions
- 🔍 RAG-enhanced context retrieval for better insights

**User Management**
- 👤 JWT-based OAuth2 authentication system
- 📚 Store and view complete analysis history
- 📑 Pagination support for history retrieval
- 🔐 Secure password hashing with Argon2

**User Interface & API**
- 🎨 Interactive web dashboard for resume analysis
- 🌐 Authentication pages (login/register)
- 📱 Responsive, mobile-friendly design
- 📚 Interactive Swagger UI documentation at `/docs`
- 🚀 RESTful API with clean endpoints

## 🔄 How Matching Works

The analysis pipeline uses a weighted scoring approach:

```
Resume PDF + Job Description
    ↓
Text Extraction & Preprocessing
    ↓
┌─────────────────────────────────┐
│  TF-IDF Score (20%)             │  Traditional text similarity
│  Semantic Score (40%)           │  Deep learning contextual match
│  Skill Score (40%)              │  Skill extraction & matching
└─────────────────────────────────┘
    ↓
Weighted Overall Score (0-100%)
    ↓
RAG Retrieval System
    ↓
LLM-Generated Insights
├─ Summary analysis
├─ Resume strengths
├─ Recommendations for improvement
└─ Interview preparation questions
    ↓
Complete Analysis Report
```

**Scoring Formula:**
```
Overall Score = (TF-IDF × 0.20) + (Semantic × 0.40) + (Skill × 0.40)
```

## 🛠 Technology Stack

| Category | Technologies |
|----------|--------------|
| **Backend** | FastAPI, Uvicorn, Python 3.12+ |
| **Database** | PostgreSQL, SQLAlchemy 2.0+, Psycopg |
| **ML/NLP** | scikit-learn, Sentence Transformers, PyMuPDF |
| **Authentication** | JWT (PyJWT), OAuth2, Argon2 (pwdlib) |
| **Frontend** | Jinja2, HTML5, CSS3, Vanilla JavaScript |
| **LLM Integration** | OpenRouter API, RAG retrieval system |
| **Dependency Mgmt** | uv (fast Python package manager) |

## 📁 Project Structure

```
job-resume-matcher/
├── app/
│   ├── api/                          # API route handlers
│   │   ├── auth_routes.py           # User registration & login
│   │   ├── match_routes.py          # Resume matching endpoint
│   │   ├── resume_routes.py         # PDF text extraction
│   │   ├── analysis_routes.py       # Analysis history & retrieval
│   │   ├── job_routes.py            # Job description endpoints
│   │   └── dependencies.py          # JWT verification
│   │
│   ├── core/                         # Core configuration
│   │   ├── config.py                # Environment variables
│   │   └── security.py              # JWT & password utilities
│   │
│   ├── models/                       # Database ORM models
│   │   ├── user.py                  # User model
│   │   └── analysis.py              # Analysis results model
│   │
│   ├── schemas/                      # Pydantic validation schemas
│   │   ├── user_schema.py           # Registration/login schemas
│   │   ├── analysis_schema.py       # Analysis response format
│   │   ├── token_schema.py          # JWT token schema
│   │   └── analysis_history_schema.py # Paginated history
│   │
│   ├── services/                     # Business logic & processing
│   │   ├── matching_service.py      # Orchestrates entire pipeline
│   │   ├── pdf_service.py           # PDF extraction logic
│   │   ├── preprocessing_service.py # Text cleaning & normalization
│   │   ├── scoring_service.py       # Score calculation
│   │   ├── semantic_matching_service.py # Semantic similarity
│   │   ├── skill_matching_service.py # Skill extraction & matching
│   │   ├── llm_service.py           # LLM API integration
│   │   └── rag_service.py           # RAG retrieval system
│   │
│   ├── static/                       # Frontend assets
│   │   ├── css/
│   │   │   ├── common.css           # Global styles
│   │   │   ├── auth.css             # Login/register styles
│   │   │   └── dashboard.css        # Dashboard styles
│   │   └── js/
│   │       ├── api.js               # API request utilities
│   │       ├── auth.js              # Authentication logic
│   │       └── dashboard.js         # Dashboard functionality
│   │
│   ├── templates/                    # HTML templates
│   │   ├── base.html                # Base layout
│   │   ├── login.html               # Login page
│   │   ├── register.html            # Registration page
│   │   └── dashboard.html           # Main analysis dashboard
│   │
│   ├── database.py                   # Database session management
│   ├── init_db.py                    # Database table creation
│   └── main.py                       # FastAPI app entry point
│
├── .gitignore                        # Git ignore patterns
├── .python-version                   # Python version (3.12)
├── pyproject.toml                    # Project metadata & dependencies
├── uv.lock                           # Locked dependency versions
└── README.md                         # This file
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.12 or newer
- PostgreSQL 12 or newer
- uv package manager
- OpenRouter API key (for AI insights)

### Step 1: Clone Repository
```bash
git clone https://github.com/Deepaksingh0907/job-resume-matcher.git
cd job-resume-matcher
```

### Step 2: Install Dependencies
```bash
uv sync
```

### Step 3: PostgreSQL Setup
```bash
# Create database
sudo -u postgres psql
ALTER USER postgres WITH PASSWORD 'your_password';
CREATE DATABASE job_resume_matcher;
\q
```

### Step 4: Create `.env` File
```env
# Database
DATABASE_URL=postgresql+psycopg://postgres:your_password@127.0.0.1:5432/job_resume_matcher

# JWT Configuration
SECRET_KEY=your-very-long-random-secret-key-min-32-chars
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# LLM Configuration (OpenRouter)
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
LLM_MODEL=deepseek/deepseek-chat
LLM_TIMEOUT_SECONDS=60
```

### Step 5: Initialize Database
```bash
uv run python -m app.init_db
```

### Step 6: Run Application
```bash
uv run uvicorn app.main:app --reload
```

Access at: **http://127.0.0.1:8000**

## 📚 API Endpoints

### Authentication
```http
POST /api/v1/auth/register
Content-Type: application/json
{
  "email": "user@example.com",
  "password": "SecurePassword123"
}

POST /api/v1/auth/login
Content-Type: application/x-www-form-urlencoded
username=user@example.com&password=SecurePassword123
```

### Resume Analysis
```http
POST /api/v1/matches/analyze
Authorization: Bearer <JWT_TOKEN>
Content-Type: multipart/form-data
file=<resume.pdf>
job_description=<job description text>

Response: {
  "analysis_id": "uuid",
  "overall_score": 75.5,
  "tfidf_score": 68.2,
  "semantic_score": 78.0,
  "skill_score": 80.5,
  "skill_analysis": {
    "matched_skills": ["Python", "FastAPI", "PostgreSQL"],
    "missing_skills": ["Docker", "Kubernetes"],
    "additional_skills": []
  },
  "llm_insights": {
    "summary": "Strong technical foundation...",
    "strengths": ["Python expertise", "API design"],
    "recommendations": ["Learn Docker", "Study Kubernetes"],
    "interview_questions": ["Explain FastAPI experience..."]
  },
  "created_at": "2026-09-03T10:30:00"
}
```

### Analysis History
```http
GET /api/v1/analyses/history?skip=0&limit=10
Authorization: Bearer <JWT_TOKEN>

GET /api/v1/analyses/{analysis_id}
Authorization: Bearer <JWT_TOKEN>

GET /health  # Health check (no auth required)
```

### Documentation
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 📊 Language Composition

| Language | Percentage |
|----------|-----------|
| Python | 45.7% |
| JavaScript | 24.6% |
| CSS | 16.8% |
| HTML | 12.9% |

## 🔐 Security

**Implemented:**
✅ Password hashing with Argon2
✅ JWT-based stateless authentication
✅ User isolation (analyses scoped to authenticated user)
✅ SQL injection prevention via SQLAlchemy ORM

**Production Recommendations:**
- Use HTTPS with valid SSL certificates
- Set strong `SECRET_KEY` (generate with `secrets.token_urlsafe(32)`)
- Store JWT in secure HttpOnly cookies (not localStorage)
- Implement rate limiting and CSRF protection
- Regular security audits and dependency updates
- Monitor API logs for suspicious activity

## ⚙️ Configuration Details

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection | `postgresql+psycopg://user:pass@host:5432/db` |
| `SECRET_KEY` | JWT signing key | Random 32+ character string |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | JWT expiration | `30` |
| `OPENROUTER_API_KEY` | LLM API access | Available at openrouter.ai |
| `LLM_MODEL` | Model selection | `deepseek/deepseek-chat`, `meta-llama/llama-2-70b-chat` |

## 📈 Future Improvements

- [ ] Alembic database migrations
- [ ] HttpOnly cookies for JWT storage
- [ ] File upload size validation
- [ ] Rate limiting
- [ ] Comprehensive test suite
- [ ] Background job processing
- [ ] Support for DOCX, TXT formats
- [ ] Advanced vector-based RAG
- [ ] Model weight optimization

## 🔧 Development

```bash
# Format code
uv run black app/

# Type checking
uv run mypy app/

# Run tests (when available)
uv run pytest
```

## 📄 License

For learning and portfolio purposes. Please add an appropriate license (MIT, Apache 2.0, GPL) before public distribution.

---

**Built with ❤️ by Deepaksingh0907**
