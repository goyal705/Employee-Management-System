document.addEventListener('DOMContentLoaded', function () {
    var queryParams = new URLSearchParams(window.location.search);

    var empid = queryParams.get('empid');
    var leaveid = queryParams.get('leaveid');
    var startdate = queryParams.get('startdate');
    var enddate = queryParams.get('enddate');
    var partialdays = queryParams.get('partialdays');
    var notes = queryParams.get('notes');
    var typeofleave = queryParams.get('typeofleave');
    var leaveduration = queryParams.get('leaveduration');
    var requestdate = queryParams.get('requestdate');

    updateElements(empid, leaveid, startdate, enddate, partialdays, notes, typeofleave, leaveduration, requestdate);
});

function updateElements(empid, leaveid, startdate, enddate, partialdays, notes, typeofleave, leaveduration, requestdate) {
    document.getElementById("empid").value = empid;
    document.getElementById("leaveid").value = leaveid;
    document.getElementById("startdate").value = startdate;
    document.getElementById("enddate").value = enddate;
    document.getElementById("notes").value = notes;
    document.getElementById("partialdays").value = partialdays;
    document.getElementById("typeofleave").value = typeofleave;
    document.getElementById("leaveduration").value = leaveduration;
    document.getElementById("requestdate").value = requestdate;
}

function sendleaveapproval() {

    const empid = document.getElementById("empid").value;
    const leaveid = document.getElementById("leaveid").value;
    const startdate = document.getElementById("startdate").value;
    const enddate = document.getElementById("enddate").value;
    const notes = document.getElementById("notes").value;
    const partialdays = document.getElementById("partialdays").value;
    const typeofleave = document.getElementById("typeofleave").value;
    const leaveduration = document.getElementById("leaveduration").value;
    const requestdate = document.getElementById("requestdate").value;
    const approvalstatus = document.getElementById("approvalstatus").value;

    const formdata = {
        "empid": empid,
        "leaveid": leaveid,
        "startdate": startdate,
        "enddate": enddate,
        "notes": notes,
        "partialdays": partialdays,
        "typeofleave": typeofleave,
        "leaveduration": leaveduration,
        "requestdate": requestdate,
        "approvalstatus": approvalstatus
    }
    startwheel();
    disableAllButtons();
    fetch('/approvalleave', {
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
            if (data.Status == "True" || data.Status == "Disapproved") {
                alert("Done");
            }
            else {
                alert("Something went wrong");
            }
            window.close();
            window.location.href = "/dashboard";
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

    buttons.forEach(function (button) {
        button.disabled = true;
    });
}
function enableAllButtons() {
    var buttons = document.querySelectorAll('button');

    buttons.forEach(function (button) {
        button.disabled = false;
    });
}