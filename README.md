# AI Job Resume Matcher

An AI-powered FastAPI application that compares resumes with job descriptions using NLP, semantic AI, and skill matching. Get match scores, identify skill gaps, and receive AI-generated recommendations.

## Features

- 📄 Upload and extract text from PDF resumes
- 📝 Calculate TF-IDF similarity (20% weight)
- 🧠 Calculate semantic similarity using Sentence Transformers (40% weight)
- 🎯 Extract and match skills (40% weight)
- 🤖 Generate AI-based recommendations using LLM
- 👤 User authentication with JWT
- 📚 Store and view analysis history
- 🎨 Interactive web dashboard
- 📊 RESTful API with Swagger documentation

## Tech Stack

- **Backend**: FastAPI, Uvicorn, Python 3.12+
- **Database**: PostgreSQL, SQLAlchemy
- **ML/NLP**: scikit-learn, Sentence Transformers, PyMuPDF
- **Auth**: JWT, OAuth2, Argon2
- **Frontend**: Jinja2, HTML, CSS, Vanilla JavaScript
- **LLM**: OpenRouter API, RAG retrieval
- **Dependency Management**: uv

## Project Structure

```
app/
├── api/                    # API routes (auth, match, resume, analysis)
├── core/                   # Configuration, security utilities
├── models/                 # Database models (User, Analysis)
├── schemas/                # Pydantic schemas for validation
├── services/               # Business logic (matching, LLM, RAG, etc.)
├── static/                 # CSS and JavaScript files
├── templates/              # HTML templates (login, dashboard, etc.)
├── database.py             # Database setup
├── init_db.py              # Initialize database tables
└── main.py                 # FastAPI application entry point
```

## Installation

```bash
# Clone repository
git clone https://github.com/Deepaksingh0907/job-resume-matcher.git
cd job-resume-matcher

# Install dependencies
uv sync
```

## Configuration

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+psycopg://postgres:password@127.0.0.1:5432/job_resume_matcher
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
OPENROUTER_API_KEY=your_api_key
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
LLM_MODEL=deepseek/deepseek-chat
LLM_TIMEOUT_SECONDS=60
```

## Database Setup

```bash
# Create PostgreSQL database
sudo -u postgres psql
ALTER USER postgres WITH PASSWORD 'password';
CREATE DATABASE job_resume_matcher;
\q

# Initialize tables
uv run python -m app.init_db
```

## Running the Application

```bash
uv run uvicorn app.main:app --reload
```

Access the app at:
- Web: http://127.0.0.1:8000
- API Docs: http://127.0.0.1:8000/docs
- Health: http://127.0.0.1:8000/health

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register user
- `POST /api/v1/auth/login` - Login and get JWT

### Resume Analysis
- `POST /api/v1/resumes/extract-text` - Extract text from PDF
- `POST /api/v1/matches/analyze` - Analyze resume vs job (requires auth)

### Analysis History
- `GET /api/v1/analyses/history?skip=0&limit=10` - Get user's analyses (requires auth)
- `GET /api/v1/analyses/{analysis_id}` - Get single analysis (requires auth)

## How Matching Works

The analysis pipeline combines three scoring methods:

```
Resume PDF + Job Description
    ↓
Text Extraction & Preprocessing
    ↓
├─ TF-IDF Scoring (20%)
├─ Semantic Similarity (40%)
└─ Skill Matching (40%)
    ↓
Weighted Overall Score (0-100)
    ↓
RAG Retrieval & LLM Insights
    ↓
Final Analysis with Recommendations
```

## Language Composition

- **Python**: 45.7%
- **JavaScript**: 24.6%
- **CSS**: 16.8%
- **HTML**: 12.9%

## Security Notes

- Do not commit `.env` file
- Use strong `SECRET_KEY` (min 32 characters)
- Store password hashes, never plain text
- Validate file uploads in production
- Use HTTPS in production
- Keep JWT tokens in secure cookies

## Future Improvements

- Alembic database migrations
- HttpOnly cookies for token storage
- File size validation and rate limiting
- Test suite
- Background job processing
- Support for DOCX/TXT files
- Advanced vector-based RAG

## License

For learning and portfolio purposes. Add a license before public distribution.

---

**Built with ❤️ by Deepaksingh0907**
