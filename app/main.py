from pathlib import Path

from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.analysis_routes import router as analysis_router
from app.api.auth_routes import router as auth_router
from app.api.match_routes import router as match_router
from app.api.resume_routes import router as resume_router


BASE_DIR = Path(__file__).resolve().parent


app = FastAPI(
    title="AI Job Resume Matcher",
    description="Match resumes with job descriptions using NLP and machine learning.",
    version="1.0.0"
)


app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static"
)


templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


@app.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )


@app.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={}
    )


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={}
    )


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AI Job Resume Matcher"
    }


app.include_router(auth_router)
app.include_router(match_router)
app.include_router(resume_router)
app.include_router(analysis_router)