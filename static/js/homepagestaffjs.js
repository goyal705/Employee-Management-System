var data=""
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
            // window.location.href = "/dashboard";
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

function showtasks() {
    const newDiv = document.getElementById("content-container");
    newDiv.innerHTML = `
    <div class="box-content" id="box-content">
        <div class="box-content-content">
            <div class="box-content-content-span">
                <span>Complete Tasks Number</span>
                <span>Incomplete Tasks Number</span>
                <span>Incomplete Task Name</span>
                <span>Task Id</span>
                <span>Task Start Date</span>
                <span>Task End Date</span>
                <span>Notes</span>
                <span>Status</span>
                <span>Add Notes</span>
            </div>
            <div class="box-content-content-input">
                <input type="text" id="completetasks" readonly>
                <input type="text" id="incompletetasks" readonly>
                <select id="taskname" onclick="showtaskdetails()"></select>
                <input type="text" id="taskid" readonly>
                <input type="date" id="startdate" readonly>
                <input type="date" id="enddate" readonly>
                <input type="text" id="notes" readonly>
                <input type="text" id="status" readonly>
                <input type="text" id="addnotes">
            </div>
        </div>
        <button type="submit" id="updatestatusbtn" onclick="updatestatusbtn()">Update Task Status</button>
        <button type="submit" id="updatestatus" onclick="updatestatus()">Submit</button>
    </div>
`
    const tasks = data["tasks"];
    var incompletetasks = 0;
    var completetasks = 0;
    for (let i = 0; i < tasks.length; i++) {
        if (tasks[i].status == "Incomplete" || tasks[i].status == "Pending") {
            incompletetasks++;
        }
        if (tasks[i].status == "Complete") {
            completetasks++;
        }
    }

    document.getElementById("completetasks").value = completetasks;
    document.getElementById("incompletetasks").value = incompletetasks;

    var selectElement = document.getElementById("taskname");
    for (let i = 0; i < tasks.length; i++) {
        if (tasks[i]["status"] == "Incomplete" || tasks[i]["status"] == "Pending") {
            var option = document.createElement("option");
            option.text = tasks[i]["taskname"];
            selectElement.add(option);
        }
    }

}

function showtaskdetails() {
    const taskname = document.getElementById("taskname").value;
    tasks_given = data["tasks"];

    for (let i = 0; i < tasks_given.length; i++) {
        if (tasks_given[i]["taskname"] == taskname) {
            console.log("here");
            document.getElementById("startdate").value = tasks_given[i]["startdate"];
            document.getElementById("enddate").value = tasks_given[i]["enddate"];
            document.getElementById("notes").value = tasks_given[i]["notes"];
            document.getElementById("status").value = tasks_given[i]["status"];
            document.getElementById("taskid").value = tasks_given[i]["taskid"];
        }

    }

}

function updatestatusbtn() {
    var status = document.getElementById("status");
    const selectElement = document.createElement("select");
    selectElement.id = "status";
    const option1 = document.createElement("option");
    option1.text = "Incomplete";
    const option2 = document.createElement("option");
    option2.text = "Complete";
    const option3 = document.createElement("option");
    option3.text = "Pending";

    selectElement.add(option1);
    selectElement.add(option2);
    selectElement.add(option3);

    status.replaceWith(selectElement);
}

function updatestatus() {

    const taskname = document.getElementById("taskname").value;
    const startdate = document.getElementById("startdate").value;
    const enddate = document.getElementById("enddate").value;
    const notes = document.getElementById("notes").value;
    const status = document.getElementById("status").value;
    const addnotes = document.getElementById("addnotes").value;
    const taskid=document.getElementById("taskid").value;

    if (!status && !addnotes) {
        alert("Kindly fill all details");
        return 0;
    }
    if (!status) {
        alert("Kindly fill Status");
        return 0;
    }
    if (!addnotes) {
        alert("Kindly fill Notes");
        return 0;
    }

    const formdata = {
        "repmanager": data["repmanager"],
        "taskname": taskname,
        "startdate": startdate,
        "enddate": enddate,
        "notes": notes,
        "status": status,
        "addnotes": addnotes,
        "taskid":taskid
    }
    startwheel();
    disableAllButtons();
    fetch('/updatetaskstatus', {
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
            if (response.Status == "True") {
                alert("Sent For Approval");
                showtasks();
            }
            else {
                alert("Something went wrong");
                window.location.href = "/dashboard";
            }
        })
}

function updateuserdetails() {
    const name = document.getElementById("yourname");
    name.removeAttribute("readonly");
}


function logout(){
    var yesno=window.confirm("Do You Want To Logout?");
    if(yesno){
        window.location.href="/signout"
    }
    else{
        return;
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