var data = ""
document.addEventListener('DOMContentLoaded', function () {
    startwheel();
    fetch('/showdetails')
        .then(response => response.json())
        .then(response => {
            endwheel();
            data = response.response;
            document.getElementById("userinfo").innerHTML = data.emp_name;
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

    var pullrequestvar = tasks[2].pullrequestrelated.length;
    const totaltaskslen = pullrequestvar;
    if (totaltaskslen > 0) {
        var notification = document.getElementById("notification");
        notification.style.background = "rgb(219, 219, 142)";
        notification.textContent = totaltaskslen;
    }
    else {
        return;
    }

}

function sendmail(){
    const newDiv = document.getElementById("content-container")
    newDiv.innerHTML = `
    <div class="box-content" id="box-content">
        <div class="box-content-content">
            <div class="box-content-content-span">
                <span>EmployeeId</span>
                <span>Select All</span>
                <span>Email Subject</span>
                <span>Email Body</span>
            </div>
            <div class="box-content-content-input">
                <select id="empids"></select>
                <input type="checkbox" id="selectall">
                <input type="text" id="subject">
                <textarea id="emailbody" rows="4" columns="50"></textarea>
            </div>
        </div>
        <button type="submit" onclick="sendmailbtn()">SEND</button>
    </div>
    `
    var empids=document.getElementById("empids");
    for(let i=0;i<data.emps.length;i++){
        var option=document.createElement("option");
        option.text=data.emps[i];
        empids.add(option);
    }
}

function sendmailbtn(){
    var checkbox=document.getElementById("selectall");
    var checkboxvalue=checkbox.checked;
    var empids=document.getElementById("empids").value;
    var empids=[empids];
    console.log(empids);
    var subject=document.getElementById("subject").value;
    var body=document.getElementById("emailbody").value;

    if(!empids || !subject || !body){
        alert("Fill all the details");
        return;
    }

    if(checkboxvalue){
        empids=data["emps"];
    }

    const formdata={
        "empids":empids,
        "subject":subject,
        "emailbody":body
    }
    startwheel();
    disableAllButtons();

    fetch('/sendmails', {
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
        if(data.Status=="True"){
            alert("Sent");
            sendmail();
        }
        else{
            alert("Something Went Wrong");
        }
    })

}


function addemployee(){
    const newDiv = document.getElementById("content-container")
    newDiv.innerHTML = `
            <div class="box-content" id="box-content">
                <div class="box-content-content">
                    <div class="box-content-content-span">
                        <span>EmployeeId</span>
                        <span>Employee Type</span>
                        <span>Email</span>
                        <span>Employee Name</span>
                        <span>Contact Number</span>
                        <span>Date Of Birth</span>
                        <span>Address</span>
                        <span>Designation</span>
                        <span>Salary</span>
                        <span>Date Of Joining</span>
                        <span>Department</span>
                        <span>Technology Stack</span>
                    </div>

                    <div class="box-content-content-input">
                        <input type="text" id="employeeid" required>
                        <select id="emptype">
                            <option>Manager</option>
                            <option>Staff</option>
                        <select>
                        <input type="text" id="email" required>
                        <input type="text" id="empname" required>
                        <input type="text" id="contactnumber" required>
                        <input type="date" id="dob" required>
                        <input type="text" id="address" required>
                        <input type="text" id="designation" required>
                        <input type="text" id="salary" required>
                        <input type="date" id="dateofjoining" required>
                        <input type="text" id="department" required>
                        <input type="text" id="techstack" required>
                    </div>
                </div>
                <button type="submit" onclick="submitempinfo()">SUBMIT</button>
            </div>  
    `  
}

function submitempinfo(){
    const empid =document.getElementById("employeeid").value;
    const emptype =document.getElementById("emptype").value;
    const email=document.getElementById("email").value;
    const empname=document.getElementById("empname").value;
    const contactnumber=document.getElementById("contactnumber").value;
    const dob=document.getElementById("dob").value;
    const address=document.getElementById("address").value;
    const designation=document.getElementById("designation").value;
    const salary=document.getElementById("salary").value;
    const dateofjoining=document.getElementById("dateofjoining").value;
    const department=document.getElementById("department").value;
    const techstack=document.getElementById("techstack").value;
    var empExists=false;

    if(!empid || !emptype || !email || !empname || !contactnumber || !dob || !address || !designation || !salary || !dateofjoining || !department || !techstack){
        alert("Fill all the fields");
        return;
    }

    for(let i=0;i<data["emps"].length;i++){
        if(data["emps"][i]==empid){
            empExists=true;
            break;
        }
    }

    if(empExists){
        alert("Empid exists");
        return;
    }

    const formdata={
        "empid":empid,
        "emptype":emptype,
        "email":email,
        "empname":empname,
        "contactnumber":contactnumber,
        "dob":dob,
        "address":address,
        "designation":designation,
        "salary":salary,
        "dateofjoining":dateofjoining,
        "department":department,
        "techstack":techstack
    }
startwheel();
disableAllButtons();
    fetch('/submitempinfo', {
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
        if(data.Status=="True"){
            alert("Sent");
            addemployee();
        }
        else{
            alert("Something Went Wrong");
        }
    })

}

function approverequests() {
    const newDiv = document.getElementById("content-container");
    const pullreqvar = data["tasks"][2].pullrequestrelated;
    const pullreqlen = pullreqvar.length;
    newDiv.innerHTML = `
        <div class="outer" id="outer">
        </div>
    `

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

function popuppullreq(argument) {
    var windowFeatures = 'width=548,height=364';
    var queryString = new URLSearchParams(argument).toString();

    var url = "/popuppullreq?" + queryString;

    window.open(url, '_blank', windowFeatures);
}

function removeemployee(){
    const newDiv = document.getElementById("content-container")
    newDiv.innerHTML = `
            <div class="box-content" id="box-content">
                <div class="box-content-content">
                    <div class="box-content-content-span">
                        <span>Select EmployeeId</span>
                        <span>Effective Date</span>
                        <span>Reason</span>
                    </div>
                    <div class="box-content-content-input">
                        <select id="empid"></select>
                        <input type="date" id="effectivedate">
                        <input type="text" id="reason">
                    </div>
                </div>
                <button id="removebtn" onclick="submitremoveemp()" type="submit">REMOVE</button>
            </div>
    `
    const empids=document.getElementById("empid");
    for(let i=0;i<data["emps"].length;i++){
        var option=document.createElement("option");
        option.text=data["emps"][i];
        empids.add(option);
    }
}

function submitremoveemp(){
    const empid=document.getElementById("empid").value;
    const effectivedate=document.getElementById("effectivedate").value;
    const reason=document.getElementById("reason").value;

    if(!empid || !effectivedate || !reason){
        alert("Fill All Details");
        return;
    }

    const formdata={
        "empid":empid,
        "effectivedate":effectivedate,
        "reason":reason
    }
    startwheel();
    disableAllButtons();

    fetch('/removeemp', {
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
        if(data.Status=="True"){
            alert("Employee Removed");
            removeemployee();
        }
        else{
            alert("Something Went Wrong");
        }
    })
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