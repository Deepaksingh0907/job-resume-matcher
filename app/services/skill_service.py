import re


SKILL_KEYWORDS = {
    "python": ["python"],
    "fastapi": ["fastapi"],
    "django": ["django"],
    "flask": ["flask"],
    "sql": ["sql"],
    "postgresql": ["postgresql", "postgres"],
    "mysql": ["mysql"],
    "mongodb": ["mongodb"],
    "docker": ["docker"],
    "aws": ["aws"],
    "git": ["git"],
    "github": ["github"],
    "rest api": ["rest api", "restful api"],
    "javascript": ["javascript"],
    "java": ["java"],
    "c++": ["c++"],
    "c#": ["c#"],
    "dsa": ["dsa", "data structures and algorithms"],
    "oop": ["oop", "object oriented programming"],
    "dbms": ["dbms", "database management systems"],
    "linux": ["linux"],
    "windows": ["windows"],
    "machine learning": ["machine learning"],
    "deep learning": ["deep learning"],
    "natural language processing": [
        "natural language processing"
    ],
    "nlp": ["nlp"],
    "scikit-learn": ["scikit-learn", "sklearn"],
    "tensorflow": ["tensorflow"],
    "pytorch": ["pytorch"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "communication": ["communication"],
    "analytical thinking": ["analytical thinking", "analytical"],
    "logical reasoning": ["logical reasoning"],
    "team collaboration": ["team collaboration"],
}


def extract_skills(text: str) -> list[str]:
    normalized_text = text.lower()

    found_skills = []

    for skill, aliases in SKILL_KEYWORDS.items():
        for alias in aliases:
            pattern = rf"(?<!\w){re.escape(alias)}(?!\w)"

            if re.search(pattern, normalized_text):
                found_skills.append(skill)
                break

    return found_skills