from app.services.skill_service import extract_skills


def compare_skills(
    resume_text: str,
    job_description: str
) -> dict:
    resume_skills = set(
        extract_skills(resume_text)
    )

    job_skills = set(
        extract_skills(job_description)
    )

    matched_skills = resume_skills.intersection(
        job_skills
    )

    missing_skills = job_skills.difference(
        resume_skills
    )

    if job_skills:
        skill_score = (
            len(matched_skills)
            / len(job_skills)
        ) * 100
    else:
        skill_score = 0.0

    return {
        "resume_skills": sorted(resume_skills),
        "job_skills": sorted(job_skills),
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills),
        "skill_score": round(skill_score, 2)
    }