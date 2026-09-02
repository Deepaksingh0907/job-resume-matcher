document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.getElementById("loginForm");
    const registerForm = document.getElementById("registerForm");

    const loginButton = document.getElementById("loginButton");
    const registerButton = document.getElementById("registerButton");

    const loginMessage = document.getElementById("loginMessage");
    const registerMessage = document.getElementById("registerMessage");


    function getErrorMessage(data) {
        if (Array.isArray(data.detail)) {
            return data.detail
                .map((error) => error.msg)
                .join(", ");
        }

        return data.detail || "Something went wrong.";
    }


    function setLoading(button, isLoading, loadingText, normalText) {
        if (!button) {
            return;
        }

        button.disabled = isLoading;
        button.textContent = isLoading
            ? loadingText
            : normalText;
    }


    function showMessage(element, message, isSuccess = false) {
        if (!element) {
            return;
        }

        element.textContent = message;
        element.style.color = isSuccess
            ? "#16a34a"
            : "#dc2626";
    }


    async function loginUser(event) {
        event.preventDefault();

        const email = document.getElementById("loginEmail").value.trim();
        const password = document.getElementById("loginPassword").value;

        if (!email || !password) {
            showMessage(
                loginMessage,
                "Please enter your email and password."
            );
            return;
        }

        setLoading(
            loginButton,
            true,
            "Logging in...",
            "Login"
        );

        try {
            const formData = new URLSearchParams();

            formData.append("username", email);
            formData.append("password", password);

            const response = await fetch(
                "/api/v1/auth/login",
                {
                    method: "POST",
                    headers: {
                        "Content-Type":
                            "application/x-www-form-urlencoded"
                    },
                    body: formData
                }
            );

            const data = await response.json();

            if (!response.ok) {
                throw new Error(getErrorMessage(data));
            }

            localStorage.setItem(
                "access_token",
                data.access_token
            );

            window.location.href = "/dashboard";

        } catch (error) {
            showMessage(
                loginMessage,
                error.message
            );

        } finally {
            setLoading(
                loginButton,
                false,
                "Logging in...",
                "Login"
            );
        }
    }


    async function registerUser(event) {
        event.preventDefault();

        const email = document
            .getElementById("registerEmail")
            .value
            .trim();

        const password = document
            .getElementById("registerPassword")
            .value;

        if (!email || !password) {
            showMessage(
                registerMessage,
                "Please enter your email and password."
            );
            return;
        }

        if (password.length < 8) {
            showMessage(
                registerMessage,
                "Password must contain at least 8 characters."
            );
            return;
        }

        setLoading(
            registerButton,
            true,
            "Creating account...",
            "Create account"
        );

        try {
            const response = await fetch(
                "/api/v1/auth/register",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        email: email,
                        password: password
                    })
                }
            );

            const data = await response.json();

            if (!response.ok) {
                throw new Error(getErrorMessage(data));
            }

            showMessage(
                registerMessage,
                "Account created successfully. Redirecting...",
                true
            );

            setTimeout(() => {
                window.location.href = "/";
            }, 1000);

        } catch (error) {
            showMessage(
                registerMessage,
                error.message
            );

        } finally {
            setLoading(
                registerButton,
                false,
                "Creating account...",
                "Create account"
            );
        }
    }


    if (loginForm) {
        loginForm.addEventListener(
            "submit",
            loginUser
        );
    } else if (loginButton) {
        loginButton.addEventListener(
            "click",
            loginUser
        );
    }


    if (registerForm) {
        registerForm.addEventListener(
            "submit",
            registerUser
        );
    } else if (registerButton) {
        registerButton.addEventListener(
            "click",
            registerUser
        );
    }
});