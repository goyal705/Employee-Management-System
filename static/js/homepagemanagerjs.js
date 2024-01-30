var data = ""
document.addEventListener('DOMContentLoaded', function () {
    startwheel();
    fetch('/showdetails')
        .then(response => response.json())
        .then(response => {
            endwheel();
            data = response.response;
            updatenotification();
        })

    setInterval(function () {
        fetch('/showdetails')
            .then(response => response.json())
            .then(response => {
                data = response.response;
                updatenotification();
            });
    }, 60000);
})

function updatenotification() {
    const tasks = data['tasks'];

    var leavesvar = tasks[0].leavesrelated.length;
    var tasksvar = tasks[1].taskrelated.length;
    var pullrequestvar = tasks[2].pullrequestrelated.length;
    const totaltaskslen = leavesvar + tasksvar + pullrequestvar;
    if (totaltaskslen > 0) {
        var notification = document.getElementById("notification");
        notification.style.background = "rgb(219, 219, 142)";
        notification.textContent = totaltaskslen;
    }
    else {
        return;
    }

}

function insertpersonalinfo() {

    const newDiv = document.getElementById("content-container")
    newDiv.innerHTML = `
            <div class="box-content" id="box-content">
                <div class="box-content-content">
                    <div class="box-content-content-span">
                        <span>EmployeeId</span>
                        <span>Email</span>
                        <span>Your Name</span>
                        <span>Contact Number</span>
                        <span>Address</span>
                        <span>Designation</span>
                        <span>Salary</span>
                        <span>Date Of Joining</span>
                        <span>Department</span>
                        <span>Technology Stack</span>
                        <span>Reporting Manager</span>
                    </div>
                    
                    <div class="box-content-content-input">
                        <input type="text" readonly id="employeeid">
                        <input type="text" readonly id="email">
                        <input type="text" readonly id="yourname">
                        <input type="text" readonly id="contactnumber">
                        <input type="text" readonly id="address">
                        <input type="text" readonly id="designation">
                        <input type="text" readonly id="salary">
                        <input type="text" readonly id="dateofjoining">
                        <input type="text" readonly id="department">
                        <input type="text" readonly id="techstack">
                        <input type="text" readonly id="repmanager">
                    </div>
                </div>
                <button type="button" onclick="updateuserdetails()">Update Details</button>
            </div>
    `;

    const empid = data.empid;
    const email = data.emailaddr;
    const emp_name = data.emp_name;
    const contact = data.contact;
    const address = data.address;
    const designation = data.designation;
    const salary = data.salary;
    const doj = data.doj;
    const department = data.department;
    const techstack = data.techstack;
    const repmanager = data.repmanager;

    document.getElementById("employeeid").value = empid;
    document.getElementById("email").value = email;
    document.getElementById("yourname").value = emp_name;
    document.getElementById("contactnumber").value = contact;
    document.getElementById("address").value = address;
    document.getElementById("designation").value = designation;
    document.getElementById("salary").value = salary;
    document.getElementById("dateofjoining").value = doj;
    document.getElementById("department").value = department;
    document.getElementById("techstack").value = techstack;
    document.getElementById("repmanager").value = repmanager;


}

function insertleaves() {

    const newDiv = document.getElementById("content-container")
    newDiv.innerHTML = `
    <div class="box-content" id="box-content">
        <div class="box-content-content">
            <div class="box-content-content-span" id="box-content-content-span">
                <span>Select Start Date</span>
                <span>Select End Date</span>
                <span>Select Partial Days</span>
                <span>Add Notes</span>
                <span>Type Of Leave</span>
            </div>
            
            <div class="box-content-content-input" id="box-content-content-input">
            <input type="date" required id="startdate">
            <input type="date" required id="enddate">
            <select id="partialdays">
                <option>None</option>
                <option>Start Days</option>
                <option>End Days</option>
            </select>
            <input type="text" required id="notes">
            <select id="myselect"></select>
        </div>
        </div>
        <button type="submit" onclick="calduration()" id="caldurationbtn">CALCULATE DURATION</button>
    </div>
`;
    const leaves = data["leaves"][0];
    var selectElement = document.getElementById("myselect");
    for (var key in leaves) {
        if (leaves.hasOwnProperty(key)) {
            var option = document.createElement("option");
            option.text = key + " (" + leaves[key] + ")";
            selectElement.add(option);
        }
    }


}
function calduration() {
    const startdate = document.getElementById("startdate").value;
    const enddate = document.getElementById("enddate").value;
    const partialdays = document.getElementById("partialdays").value;
    const notes = document.getElementById("notes").value;
    const leavetype = document.getElementById("myselect").value;
    var leaveduration = 0;
    var date1 = new Date(startdate);
    var date2 = new Date(enddate);

    if (!startdate || !enddate || !notes || !leavetype || !partialdays) {
        alert("Fill all fields");
        return 0;
    }
    else {
        if (partialdays == "Start Days") {
            leaveduration = (date2 - date1) / 86400000 + 1;
            leaveduration = leaveduration * 0.5
        }
        else if (partialdays == "End Days") {
            leaveduration = (date2 - date1) / 86400000 + 1;
            leaveduration = leaveduration * 0.5
        }
        else {
            leaveduration = (date2 - date1) / 86400000 + 1;
        }

        if (leaveduration === 0 || leaveduration < 0) {
            alert("Start Value Should Not Be Greater Than End Date");
            return 0;
        }
        else {
            var selectdiv1 = document.getElementById("box-content-content-span");
            var selectdiv2 = document.getElementById("box-content-content-input");

            var newspan = document.createElement("span");
            var newinput = document.createElement("input");
            newspan.innerHTML = "Total Duration In Days";
            newinput.id = "leaveduration";
            newinput.readOnly = true;
            newinput.value = leaveduration;
            selectdiv1.appendChild(newspan);
            selectdiv2.appendChild(newinput);

            var submitbtn = document.getElementById("caldurationbtn");
            submitbtn.innerHTML = "SUBMIT";
            submitbtn.id = "submitbtn";
            submitbtn.onclick = submitleaves;

            document.getElementById("startdate").readOnly = true;
            document.getElementById("enddate").readOnly = true;
            document.getElementById("partialdays").disabled = true;
            document.getElementById("notes").readOnly = true;
            document.getElementById("myselect").disabled = true;
        }
    }


}

function submitleaves() {
    const empid = data["empid"];
    const repmanager = data["repmanager"];
    const startdate = document.getElementById("startdate").value;
    const enddate = document.getElementById("enddate").value;
    const partialdays = document.getElementById("partialdays").value;
    const notes = document.getElementById("notes").value;
    const typeofleave = document.getElementById("myselect").value;
    const leaveduration = document.getElementById("leaveduration").value;

    const formdata = {
        "empid": empid,
        "repmanager": repmanager,
        "startdate": startdate,
        "enddate": enddate,
        "partialdays": partialdays,
        "notes": notes,
        "typeofleave": typeofleave,
        "leaveduration": leaveduration
    }
    startwheel();
    disableAllButtons();

    fetch('/submitleaveapproval', {
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
            if (data.Status = "True") {
                alert("Submitted For Approval");
            }
            else {
                alert("An Error Occurred");
            }
            window.location.href = "/dashboard"
        })
}

function updateuserdetails() {
    const name = document.getElementById("yourname");
    name.removeAttribute("readonly");
}

function assigntasks() {
    const newDiv = document.getElementById("content-container")
    newDiv.innerHTML = `
    <div class="box-content" id="box-content">
        <div class="box-content-content">
            <div class="box-content-content-span">
                <span>Enter Task Name</span>
                <span>Select Employee Id</span>
                <span>Select Start Date</span>
                <span>Select End Date</span>
                <span>Add Notes</span>
            </div>
            
            <div class="box-content-content-input">
                <input type="text" id="taskname" required>
                <select id="myselect"></select>    
                <input type="date" id="startdate" required>
                <input type="date" id="enddate" required>
                <input type="text" id="notes" required>
            </div>
        </div>
        <button type="submit" onclick="assigntasksbtn()">SUBMIT</button>
    </div>
`;
    var personrep = data["personreporting"];
    for (let i = 0; i < personrep.length; i++) {
        var selectElement = document.getElementById("myselect");
        var option = document.createElement("option");
        option.text = personrep[i];
        selectElement.add(option);
    }

}

function assigntasksbtn() {
    const taskname = document.getElementById("taskname").value;
    const empid = document.getElementById("myselect").value;
    const startdate = document.getElementById("startdate").value;
    const enddate = document.getElementById("enddate").value;
    const notes = document.getElementById("notes").value;

    const formdata = {
        "taskname": taskname,
        "empid": empid,
        "startdate": startdate,
        "enddate": enddate,
        "notes": notes
    }

    if (!taskname || !empid || !startdate || !enddate || !notes) {
        alert("Kindly Fill All The Fields");
        return;
    }
    else {
        if (startdate > enddate) {
            alert("Start Date Can't Be More Than End Date");
            return;
        }
        else {
            startwheel();
            disableAllButtons();
            fetch('/assigntasks', {
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

                        alert("thanks");
                    }
                    else {
                        alert("An Error Occ");
                    }
                })
        }
    }
    assigntasks();
}


function viewtasksprogress() {
    const newDiv = document.getElementById("content-container");
    newDiv.innerHTML = `
        <div class="box-content" id="box-content">
            <div class="box-content-content">
                <div class="box-content-content-span">
                    <span>Select EmployeeId</span>
                </div>
                <div class="box-content-content-input">
                    <select id="myselect" onclick="seetask()"></select>
                </div>
            </div>
            <div class="box-content-content">
                <div class="box-content-content-span">
                    <span>Select Task Name</span>
                    <span>TaskId</span>
                    <span>Start Date</span>
                    <span>End Date</span>
                    <span>Notes</span>
                    <span>Status</span>
                </div>
                <div class="box-content-content-input">
                    <select id="taskname" onclick="seetaskdetails()"></select>   
                    <input type="text" id="taskid" readonly>
                    <input type="date" id="startdate" readonly>
                    <input type="date" id="enddate" readonly>
                    <input type="text" id="notes" readonly>
                    <input type="text" id="status" readonly>
                </div>
            </div>      
        <button type="button" onclick="updatetaskdetails()">Update Task</button>
        <button type="button" onclick="cleardata()" id="cleardata">Clear Data</button>
    </div>`

    var selectElement = document.getElementById("myselect");
    const emprep = data["personreporting"];
    for (let i = 0; i < emprep.length; i++) {
        var empid = emprep[i];
        var option = document.createElement("option");
        option.id = "optionid";
        option.text = empid;
        selectElement.add(option);
    }
}

function updatetaskdetails() {
    document.getElementById("myselect").disabled = true
    document.getElementById("taskname").disabled = true
    document.getElementById("startdate").readOnly = false
    document.getElementById("enddate").readOnly = false
    document.getElementById("notes").readOnly = false
    var status = document.getElementById("status");
    var clearbtn = document.getElementById("cleardata");
    var submitbtn = document.createElement("button");
    submitbtn.onclick = sendupdatedtaskdetails;
    submitbtn.innerText = "SUBMIT";
    var selectElement = document.createElement("select");
    selectElement.id = "updatedstatus";

    var option1 = document.createElement("option");
    var option2 = document.createElement("option");
    var option3 = document.createElement("option");
    option1.text = "Incomplete";
    option2.text = "Pending";
    option3.text = "Complete";

    selectElement.add(option1);
    selectElement.add(option2);
    selectElement.add(option3);
    if (!document.getElementById("updatedstatus")) {
        status.parentNode.replaceChild(selectElement, status);
        clearbtn.parentNode.appendChild(submitbtn);
    }
    else {
        return;
    }

}

function sendupdatedtaskdetails() {
    const empid = document.getElementById("myselect").value;
    const taskid = document.getElementById("taskid").value;
    const taskname = document.getElementById("taskname").value;
    const startdate = document.getElementById("startdate").value;
    const enddate = document.getElementById("enddate").value;
    const notes = document.getElementById("notes").value;
    const status = document.getElementById("updatedstatus").value;

    var startdate1 = new Date(startdate);
    var enddate1 = new Date(enddate);

    if (!startdate || !enddate || !notes || !status) {
        alert("Kindly fill all the fields");
        return;
    }
    else if (startdate1 > enddate1) {
        alert("Startdate should be less than end date");
        return;
    }

    formdata = {
        "empid": empid,
        "taskid": taskid,
        "taskname": taskname,
        "startdate": startdate,
        "enddate": enddate,
        "notes": notes,
        "status": status
    }
    startwheel();
    disableAllButtons();
    fetch('/updatetaskdetail', {
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
        })
    viewtasksprogress();

}

function seetask() {
    const empid = document.getElementById("myselect").value;
    const selectElement = document.getElementById("taskname");
    document.getElementById("taskid").value = "";
    document.getElementById("startdate").value = "";
    document.getElementById("enddate").value = "";
    document.getElementById("notes").value = "";
    document.getElementById("status").value = "";
    tasks_given = data["tasks_given"];
    selectElement.innerHTML = "";
    for (let i = 0; i < tasks_given.length; i++) {
        if (tasks_given[i]["empid"] == empid) {
            const taskname = tasks_given[i]["taskname"];
            var option = document.createElement("option");
            option.text = taskname;
            selectElement.add(option);
        }
    }
}

function seetaskdetails() {
    const taskname = document.getElementById("taskname").value;
    tasks_given = data["tasks_given"];

    for (let i = 0; i < tasks_given.length; i++) {
        if (tasks_given[i]["taskname"] == taskname) {
            console.log("here");
            document.getElementById("taskid").value = tasks_given[i]["taskid"];
            document.getElementById("startdate").value = tasks_given[i]["startdate"];
            document.getElementById("enddate").value = tasks_given[i]["enddate"];
            document.getElementById("notes").value = tasks_given[i]["notes"];
            document.getElementById("status").value = tasks_given[i]["status"];
            return;
        }

    }

}

function cleardata() {
    viewtasksprogress();
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


