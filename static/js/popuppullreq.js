document.addEventListener('DOMContentLoaded', function () {
    var queryParams = new URLSearchParams(window.location.search);

    var empid = queryParams.get('empid');
    var currentrepmanager = queryParams.get('currentrepmanager');
    var requestingmanager = queryParams.get('requestingmanager');
    var requestdate = queryParams.get('requestdate');

    updateElements(empid, currentrepmanager, requestingmanager, requestdate);
});

function updateElements(empid, currentrepmanager, requestingmanager, requestdate) {
    document.getElementById("empid").value = empid;
    document.getElementById("requestingperson").value = requestingmanager;
    document.getElementById("reqdate").value = requestdate;
}

function sendpullreq() {
    const empid = document.getElementById("empid").value;
    const requestingmanager = document.getElementById("requestingperson").value;
    const requestdate = document.getElementById("reqdate").value;
    const approvalstatus = document.getElementById("approvalstatus").value;
    const formdata = {
        "empid": empid,
        "requestingmanager": requestingmanager,
        "requestdate": requestdate,
        "approvalstatus": approvalstatus
    }
    startwheel();
    disableAllButtons();
    fetch('/sendpullrequestapproval', {
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
        if (data.Status == "True") {
            alert("Done");
        }
        else {
            alert("Something went wrong");
        }
        window.close();
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