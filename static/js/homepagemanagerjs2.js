var data = ""
document.addEventListener('DOMContentLoaded', function () {
    startwheel();
    fetch('/showdetails')
        .then(response => response.json())
        .then(response => {
            endwheel();
            data = response.response;
            document.getElementById("userinfo").innerHTML = data.emp_name;
        })

})

function approverequests() {
    const newDiv = document.getElementById("content-container");
    const taskvar = data["tasks"][1].taskrelated;
    const leavevar = data["tasks"][0].leavesrelated;
    const pullreqvar = data["tasks"][2].pullrequestrelated;
    const taskvarlen = taskvar.length;
    const leavevarlen = leavevar.length;
    const pullreqlen = pullreqvar.length;
    newDiv.innerHTML = `
        <div class="outer" id="outer">
        </div>
    `
    if (taskvarlen > 0) {
        for (let i = 0; i < taskvarlen; i++) {
            const outerdiv = document.getElementById("outer");
            var innerdiv = document.createElement("div");
            const formdata = { "empid": taskvar[i].empid, "taskname": taskvar[i].taskname, "startdate": taskvar[i].startdate, "enddate": taskvar[i].enddate, "notes": taskvar[i].notes, "status": taskvar[i].status, "addnotes": taskvar[i].addnotes, "taskid": taskvar[i].taskid }
            var argument = `popuptasks(${JSON.stringify(formdata)})`;
            innerdiv.className = "inner";
            innerdiv.setAttribute("onclick", argument)
            innerdiv.innerHTML = "<b>Approval For Task</b>" + "<br>" + "EmployeeId: " + taskvar[i].empid + "<br>" + "Task Name: " + taskvar[i].taskname;
            outerdiv.append(innerdiv);
        }

    }

    if (leavevarlen > 0) {
        for (let i = 0; i < leavevarlen; i++) {
            const outerdiv = document.getElementById("outer");
            var innerdiv = document.createElement("div");
            const formdata = { "empid": leavevar[i].empid, "startdate": leavevar[i].startdate, "enddate": leavevar[i].enddate, "partialdays": leavevar[i].partialdays, "notes": leavevar[i].notes, "typeofleave": leavevar[i].typeofleave, "leaveduration": leavevar[i].leaveduration, "requestdate": leavevar[i].reqdate, "leaveid": leavevar[i].leaveid }
            var argument = `popupleaves(${JSON.stringify(formdata)})`;
            innerdiv.className = "inner";
            innerdiv.setAttribute("onclick", argument)
            innerdiv.innerHTML = "<b>Approval Of Leave</b>" + "<br>" + "EmployeeId: " + leavevar[i].empid;
            outerdiv.append(innerdiv);
        }
    }

    if (pullreqlen>0) {
        for (let i = 0; i < pullreqlen; i++) {
            const outerdiv = document.getElementById("outer");
            var innerdiv = document.createElement("div");
            const formdata = { "empid": pullreqvar[i].empid, "currentrepmanager": pullreqvar[i].currentrepmanager, "requestingmanager": pullreqvar[i].requestingmanager, "requestdate": pullreqvar[i].requestdate }
            var argument = `popuppullreq(${JSON.stringify(formdata)})`;
            innerdiv.className = "inner";
            innerdiv.setAttribute("onclick", argument)
            innerdiv.innerHTML = "<b>Resource Pull Request</b>" + "<br>" + "EmployeeId: " + pullreqvar[i].empid + "<br>" + "Requesting Person: " + pullreqvar[i].requestingmanager;
            outerdiv.append(innerdiv);
        }
    }

}

function popuptasks(argument) {
    var windowFeatures = 'width=548,height=624';
    var queryString = new URLSearchParams(argument).toString();

    var url = "/popuptasks?" + queryString;

    window.open(url, '_blank', windowFeatures);
}

function popupleaves(argument) {
    var windowFeatures = 'width=548,height=700';
    var queryString = new URLSearchParams(argument).toString();

    var url = "/popupleaves?" + queryString;

    window.open(url, '_blank', windowFeatures);
}

function popuppullreq(argument) {
    var windowFeatures = 'width=548,height=364';
    var queryString = new URLSearchParams(argument).toString();

    var url = "/popuppullreq?" + queryString;

    window.open(url, '_blank', windowFeatures);
}

function pullresource() {
    const newDiv = document.getElementById("content-container")
    newDiv.innerHTML = `
    <div class="box-content" id="box-content">
        <div class="box-content-content">
            <div class="box-content-content-span">
                <span>EmployeeId</span>
                <span>Employee Name</span>
                <span>Employee Department</span>
                <span>Employee Tech Stack</span>
                <span>Employee Designation</span>
                <span>Employee Manager</span>
            </div>
            <div class="box-content-content-input">
                <select id="empid" onclick="addempdetails()"></select>
                <input type="text" id="empname" readonly>
                <input type="text" id="department" readonly>
                <input type="text" id="techstack" readonly>
                <input type="text" id="designation" readonly>
                <input type="text" id="manager" readonly>
            </div>
            </div>
            <button onclick="sendpullrequest()">SEND PULL REQUEST</button>
    </div>
`
    // here make a api call to get empids from employees collection
    startwheel();
    fetch('/collectempids')
        .then(response => response.json())
        .then(data1 => {
            endwheel();
            var empid = document.getElementById("empid");
            for (let i = 0; i < data1.response.length; i++) {
                if (data1.response[i] != data["repmanager"]) {
                    const option = document.createElement("option");
                    option.text = data1.response[i];
                    empid.add(option);
                }

            }
        })
}

function addempdetails() {
    const empid = document.getElementById("empid").value;
    const formdata = { "empid": empid };
    startwheel();
    disableAllButtons();
    fetch('/getempdetails', {
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
            document.getElementById("empname").value = data["empname"]
            document.getElementById("department").value = data["department"]
            document.getElementById("techstack").value = data["techstack"]
            document.getElementById("designation").value = data["designation"]
            document.getElementById("manager").value = data["manager"]
        })
}

function sendpullrequest() {
    const empid = document.getElementById("empid").value;
    const currentrepmanager = document.getElementById("manager").value;
    const requestingmanager = data["empid"];

    if (!empid || !currentrepmanager) {
        alert("Fill all the fields");
        return;
    }
    if(currentrepmanager==data["empid"]){
        alert("Can't pull from self");
        return;
    }
    else {
        formdata = {
            "empid": empid,
            "currentrepmanager": currentrepmanager,
            "requestingmanager": requestingmanager
        }
        var yesno = window.confirm("Do You Want To Submit Request?");
        if (yesno) {
            startwheel();
            disableAllButtons();
            fetch('/sendpullrequest', {
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
                        alert("Request sent for approval");
                        pullresource();
                    }
                    else {
                        alert("Something went wrong");
                    }
                })
        }
        else {
            return;
        }

    }



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

function logout() {
    var yesno = window.confirm("Do You Want To Logout?");
    if (yesno) {
        window.location.href = "/signout"
    }
    else {
        return;
    }

}


