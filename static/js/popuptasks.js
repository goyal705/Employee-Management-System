document.addEventListener('DOMContentLoaded', function () {
    var queryParams = new URLSearchParams(window.location.search);

    var empid = queryParams.get('empid');
    var taskid = queryParams.get('taskid');
    var taskname = queryParams.get('taskname');
    var startdate=queryParams.get('startdate');
    var enddate=queryParams.get('enddate');
    var notes1=queryParams.get('notes');
    var status=queryParams.get('status');
    var notes2=queryParams.get('addnotes');

    updateElements(empid,taskid,taskname,startdate,enddate,notes1,status,notes2);
});

function updateElements(empid,taskid,taskname,startdate,enddate,notes1,status,notes2) {
    document.getElementById("empid").value = empid;
    document.getElementById("taskid").value = taskid;
    document.getElementById("taskname").value = taskname;
    document.getElementById("startdate").value=startdate;
    document.getElementById("enddate").value=enddate;
    document.getElementById("notes1").value=notes1;
    document.getElementById("currentstatus").value=status;
    document.getElementById("notes2").value=notes2;
}

function sendtaskapproval(){
    const empid=document.getElementById("empid").value;
    const taskid=document.getElementById("taskid").value;
    const taskname= document.getElementById("taskname").value;
    const startdate=document.getElementById("startdate").value;
    const enddate=document.getElementById("enddate").value;
    const notes1=document.getElementById("notes1").value;
    const status=document.getElementById("currentstatus").value;
    const notes2=document.getElementById("notes2").value;
    const approvalstatus=document.getElementById("approvalstatus").value;
    const formdata={
        "empid":empid,
        "taskid":taskid,
        "taskname":taskname,
        "startdate":startdate,
        "enddate":enddate,
        "notes":notes1,
        "status":status,
        "addnotes":notes2,
        "approvalstatus":approvalstatus};
    startwheel();
    disableAllButtons();   
    fetch('/approvaltask', {
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
            alert("Done");
        }
        else if(data.Status=="Not Changed"){
            alert("Done");
        }
        else{
            alert("Something went wrong");
        }
    window.close();
    window.location.href="/dashboard";
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