const sessionTimeout = 1800;  // in seconds
let timer;

function startSessionTimer() {
    timer = setTimeout(logoutUser, sessionTimeout * 1000);
}

function resetSessionTimer() {
    clearTimeout(timer);
    startSessionTimer();
}

function logoutUser() {
    alert("Session expired. Please log in again.");
    window.location.href="/";
}


// Reset the session timer on user activity (e.g., button click, form submission, etc.)
startSessionTimer();