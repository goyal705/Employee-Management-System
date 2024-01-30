function signIN() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    formdata = { username: username, password: password }

    if (username && password) {
        startwheel();
        disableAllButtons();
        fetch('/signin', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formdata)
        })
        .then(response => response.json())
        .then(data => {
            endwheel();
            enableAllButtons();
            if (data.message === "Login successful") {
                alert(data.message);
                window.location.href = "/dashboard";
            }
            else {
                alert(data.message);
            }
        })

    }
    else {
        alert("Kindly fill all the fields")
    }
}

function forgotpassword() {
    // const form = document.getElementById("search-form");
    document.getElementById("passlabel").remove();
    document.getElementById("password").remove();

    document.getElementById("emaillabel").style.display = "block";
    document.getElementById("email").style.display = "block";

    document.getElementById("doblabel").style.display = "block";
    document.getElementById("dob").style.display = "block";

    document.getElementById("messageContainer").style.display = "block";
    document.getElementById("back").style.display = "block";
    document.getElementById("submit").style.display = "block";
    document.getElementById("signin").style.display = "none";
    document.getElementById("forgotpass").style.display = "none";

}

function closeMessage() {
    document.getElementById("messageContainer").style.display = "none";
}

function goback() {
    window.location.href = "/";
}

function submitbtn() {
    var username = document.getElementById("username").value;
    var dob = document.getElementById("dob").value;
    var email = document.getElementById("email").value;

    if ((username && dob) || (username && email)) {
        const formdata = {
            "empid": username,
            "dob": dob,
            "email": email
        }
        startwheel();
        disableAllButtons();
        fetch('/checkuser', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formdata)
        })
            .then(response => response.json())
            .then(response => {
                endwheel();
                enableAllButtons();
                if (response["Status"] == "Emp Present") {
                    document.getElementById("msg").innerText = "Welcome " + response["empname"];

                    document.getElementById("newpasslabel").style.display = "block";
                    document.getElementById("newpass").style.display = "block";
                    document.getElementById("codelabel").style.display = "block";
                    document.getElementById("code").style.display = "block";
                    document.getElementById("submit").onclick = changepass;

                    document.getElementById("username").readOnly = true;
                    document.getElementById("dob").readOnly = true;
                    document.getElementById("email").readOnly = true;

                }
                else {
                    alert("User not present");
                }
            })
    }
    else {
        alert("Fill atleast two fields");
        return;
    }

}

function changepass() {
    var username = document.getElementById("username").value;
    var newpass = document.getElementById("newpass").value;
    var code = document.getElementById("code").value;

    if (!newpass || !code) {
        alert("Fill all the required fields");
        return;
    }

    const formdata = {
        "empid": username,
        "newpass": newpass,
        "code": code
    }
    startwheel();
    disableAllButtons();
    fetch('/changepass', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formdata)
    })
        .then(response => response.json())
        .then(response => {
            endwheel();
            enableAllButtons();
            if (response["Status"] == "True") {
                alert("Password change successfull");
                window.location.href = "/";
            }
            else if (response["Status"] == "Code not matched") {
                alert("Invalid Code Entered");
                return;
            }
            else {
                alert("Something went wrong");
            }
        })

}

function startwheel() {
    document.getElementById("loading-overlay").style.display = "flex";
    document.getElementById("loading-overlay").style.justifyContent = "center";
    document.getElementById("loading-overlay").style.alignItems = "center";
}

function endwheel() {
    document.getElementById("loading-overlay").style.display = "none";
}

function disableAllButtons() {
    var buttons = document.querySelectorAll('button');

    buttons.forEach(function(button) {
        button.disabled = true;
    });
}
function enableAllButtons() {
    var buttons = document.querySelectorAll('button');

    buttons.forEach(function(button) {
        button.disabled = false;
    });
}