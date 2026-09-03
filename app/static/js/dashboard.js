document.addEventListener("DOMContentLoaded", () => {
    const token = localStorage.getItem("access_token");

    if (!token) {
        window.location.href = "/";
        return;
    }


    const resumeFile = document.getElementById("resumeFile");
    const jobDescription = document.getElementById("jobDescription");
    const analyzeButton = document.getElementById("analyzeButton");
    const analysisResult = document.getElementById("analysisResult");

    const historyButton = document.getElementById("historyButton");
    const historyResult = document.getElementById("historyResult");
    const logoutLink = document.getElementById("logoutLink");


    function escapeHtml(value) {
        return String(value ?? "")
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }


    function setButtonLoading(
        button,
        isLoading,
        loadingText,
        normalText
    ) {
        button.disabled = isLoading;
        button.textContent = isLoading
            ? loadingText
            : normalText;
    }


    function renderSkills(skills, className) {
        if (!skills || skills.length === 0) {
            return `<span class="empty-skill">None</span>`;
        }

        return skills
            .map(
                (skill) => `
                    <span class="skill-chip ${className}">
                        ${escapeHtml(skill)}
                    </span>
                `
            )
            .join("");
    }


    function renderList(items) {
        if (!items || items.length === 0) {
            return "<li>No information available.</li>";
        }

        return items
            .map(
                (item) => `
                    <li>${escapeHtml(item)}</li>
                `
            )
            .join("");
    }


    function renderLLMInsights(insights) {
        if (!insights) {
            return `
                <div class="llm-insights">
                    <h3>AI insights</h3>

                    <p class="empty-message">
                        AI insights are not available for this analysis.
                    </p>
                </div>
            `;
        }

        return `
            <div class="llm-insights">

                <h3>AI insights</h3>

                <p class="llm-summary">
                    ${escapeHtml(insights.summary)}
                </p>


                <div class="insight-group">
                    <h4>Strengths</h4>

                    <ul class="insight-list">
                        ${renderList(insights.strengths)}
                    </ul>
                </div>


                <div class="insight-group">
                    <h4>Recommendations</h4>

                    <ul class="insight-list">
                        ${renderList(insights.recommendations)}
                    </ul>
                </div>


                <div class="insight-group">
                    <h4>Interview questions</h4>

                    <ul class="insight-list">
                        ${renderList(insights.interview_questions)}
                    </ul>
                </div>

            </div>
        `;
    }


    function renderAnalysis(data) {
        const skills = data.skill_analysis || {};

        analysisResult.innerHTML = `
            <div class="score-summary">

                <div class="score-card">
                    <h3>Overall score</h3>
                    <strong>
                        ${Number(data.overall_score).toFixed(2)}%
                    </strong>
                </div>

                <div class="score-card">
                    <h3>Semantic score</h3>
                    <strong>
                        ${Number(data.semantic_score).toFixed(2)}%
                    </strong>
                </div>

                <div class="score-card">
                    <h3>TF-IDF score</h3>
                    <strong>
                        ${Number(data.tfidf_score).toFixed(2)}%
                    </strong>
                </div>

                <div class="score-card">
                    <h3>Skill score</h3>
                    <strong>
                        ${Number(skills.skill_score).toFixed(2)}%
                    </strong>
                </div>

            </div>


            <div class="skills-section">
                <h3>Matched skills</h3>

                <div class="skill-list">
                    ${renderSkills(
                        skills.matched_skills,
                        "matched-skill"
                    )}
                </div>
            </div>


            <div class="skills-section">
                <h3>Missing skills</h3>

                <div class="skill-list">
                    ${renderSkills(
                        skills.missing_skills,
                        "missing-skill"
                    )}
                </div>
            </div>


            ${renderLLMInsights(data.llm_insights)}
        `;
    }


    async function analyzeResume() {
        const file = resumeFile.files[0];
        const jobText = jobDescription.value.trim();

        if (!file) {
            analysisResult.innerHTML = `
                <p class="error-message">
                    Please select a resume PDF.
                </p>
            `;
            return;
        }

        if (!file.name.toLowerCase().endsWith(".pdf")) {
            analysisResult.innerHTML = `
                <p class="error-message">
                    Please upload a PDF file only.
                </p>
            `;
            return;
        }

        if (!jobText) {
            analysisResult.innerHTML = `
                <p class="error-message">
                    Please enter a job description.
                </p>
            `;
            return;
        }

        setButtonLoading(
            analyzeButton,
            true,
            "Analyzing...",
            "Analyze resume"
        );

        const formData = new FormData();

        formData.append("file", file);
        formData.append("job_description", jobText);

        try {
            const data = await apiRequest(
                "/api/v1/matches/analyze",
                {
                    method: "POST",
                    body: formData
                }
            );

            renderAnalysis(data);

        } catch (error) {
            analysisResult.innerHTML = `
                <p class="error-message">
                    ${escapeHtml(error.message)}
                </p>
            `;

        } finally {
            setButtonLoading(
                analyzeButton,
                false,
                "Analyzing...",
                "Analyze resume"
            );
        }
    }


    function renderHistory(data) {
        if (!data.items || data.items.length === 0) {
            historyResult.innerHTML = `
                <p class="empty-message">
                    No previous analyses found.
                </p>
            `;
            return;
        }

        historyResult.innerHTML = data.items
            .map(
                (item) => `
                    <div class="history-item">

                        <h3>
                            ${escapeHtml(item.resume_filename)}
                        </h3>

                        <p>
                            Overall score:
                            <strong>
                                ${Number(item.overall_score).toFixed(2)}%
                            </strong>
                        </p>

                        <p>
                            Matched skills:
                            ${item.matched_skills?.length || 0}
                        </p>

                        <p>
                            ${new Date(
                                item.created_at
                            ).toLocaleString()}
                        </p>

                    </div>
                `
            )
            .join("");
    }


    async function loadHistory() {
        setButtonLoading(
            historyButton,
            true,
            "Loading...",
            "Load history"
        );

        try {
            const data = await apiRequest(
                "/api/v1/analyses/history?skip=0&limit=10"
            );

            renderHistory(data);

        } catch (error) {
            historyResult.innerHTML = `
                <p class="error-message">
                    ${escapeHtml(error.message)}
                </p>
            `;

        } finally {
            setButtonLoading(
                historyButton,
                false,
                "Loading...",
                "Load history"
            );
        }
    }


    analyzeButton.addEventListener(
        "click",
        analyzeResume
    );

    historyButton.addEventListener(
        "click",
        loadHistory
    );

    logoutLink.addEventListener(
        "click",
        (event) => {
            event.preventDefault();
            logoutUser();
        }
    );
});