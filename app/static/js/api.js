async function apiRequest(url, options = {}) {
    const token = localStorage.getItem("access_token");

    const headers = new Headers(
        options.headers || {}
    );

    if (token) {
        headers.set(
            "Authorization",
            `Bearer ${token}`
        );
    }

    const response = await fetch(
        url,
        {
            ...options,
            headers: headers
        }
    );

    const data = await response
        .json()
        .catch(() => ({}));


    if (response.status === 401) {
        localStorage.removeItem("access_token");
        window.location.href = "/";

        return;
    }


    if (!response.ok) {
        let message = "Request failed.";

        if (Array.isArray(data.detail)) {
            message = data.detail
                .map((error) => error.msg)
                .join(", ");
        } else if (data.detail) {
            message = data.detail;
        }

        const error = new Error(message);
        error.status = response.status;

        throw error;
    }

    return data;
}


function logoutUser() {
    localStorage.removeItem("access_token");
    window.location.href = "/";
}