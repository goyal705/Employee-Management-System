from flask import Flask, jsonify, render_template,request, session
import random
from database import handlesignin
from database import showpersonaldetails
from database import assigntasks
from database import sendtaskforapproval
from database import sendleaveforapproval
from database import approvaltaskstatus
from database import updateemailscoll
from database import getemailaddr
from database import updatetaskdetail
from database import approvalleavestatus
from database import collectempids
from database import getempdetails
from database import sendpullrequest
from database import sendpullrequestapproval
from database import createempinfo
from database import removeemp2
from database import checkuser
from database import changepass
from datetime import datetime,timedelta
from mailtemplates import mails
import os
import pytz

app2 = Flask(__name__)
app2.secret_key = os.getenv('key')

@app2.route('/')
def home():
    return render_template('signin.html')

@app2.route("/signin",methods=["POST"])
def login():
    data = request.get_json()
    user_info = handlesignin(data)
    session["username"]=data.get("username")
    session["user_info"]=user_info
    
    timezone = pytz.UTC
    session["endtime"]=timezone.localize(datetime.now()+timedelta(minutes=30))
    
    if user_info["UserPresent"] == "True":
        current_time = datetime.now()
        time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        email,name=getemailaddr(data["username"])
        email_body={"recipientmail":email,
                    "subject":"Login Activity Mail",
                    "body":mails["Login"].format(name=name,time_string=time_string)}
        updateemailscoll(email_body)
        
        return jsonify({'message': 'Login successful', 'user_info': user_info})
    else:
        return jsonify({'message': 'Invalid credentials'})

@app2.route("/signout")
def logout():
    username=session["username"]
    email,name=getemailaddr(username)
    current_time = datetime.now()
    time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    email_body={"recipientmail":email,
                "subject":"Logout Activity Mail",
                "body":mails["Logout"].format(name=name,time_string=time_string)
                }
    updateemailscoll(email_body)
    
    session["username"]=None
    session["user_info"]=None
    return render_template('signin.html')
    
@app2.route("/dashboard")
def dashboard():
    user_info = session.get('user_info')
    
    currenttime=datetime.now()
    timezone=pytz.UTC
    currenttime=timezone.localize(currenttime)
    
    if user_info and user_info["UserPresent"] == "True":
        if session['endtime']>currenttime:

            if user_info["usertype"] == "Manager":
                return render_template("homepagemanager.html", user_info=user_info)
            elif user_info["usertype"]=="Admin":
                return render_template("admin.html", user_info=user_info)
            else:
                return render_template("homepagestaff.html", user_info=user_info)
        else:
            return "Session expired login again"
    else:
            return "User is not logged in"

    
@app2.route("/showdetails",methods=["GET"])
def perdetails():
    response=showpersonaldetails()
    return {"response":response,"endtime":session["endtime"]}

@app2.route("/assigntasks",methods=["POST"])
def givetasks():
    data=request.get_json()
    response=assigntasks(data)
    
    if response=="True":
        current_time = datetime.now()
        time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        emailstaff,namestaff=getemailaddr(data["empid"])
        email_body={"recipientmail":emailstaff,
                    "subject":"Task Assignment Mail",
                    "body":mails["Taskassignedstaff"].format(namestaff=namestaff,time_string=time_string,taskid=data["taskid"],taskname=data["taskname"],startdate=data['startdate'],enddate=data['enddate'],notes=data['notes'])}
        updateemailscoll(email_body)
        
        emailmanager,namemanager=getemailaddr(session["username"])
        email_body={"recipientmail":emailmanager,
                    "subject":"Task Assigned Confirmation Mail",
                    "body":mails["Taskassignedmanager"].format(namemanager=namemanager,time_string=time_string,namestaff=namestaff,taskid=data["taskid"],taskname=data["taskname"],startdate=data['startdate'],enddate=data['enddate'],notes=data['notes'])}
        updateemailscoll(email_body)
    
    return {"Status":response}

@app2.route("/updatetaskstatus",methods=["POST"])
def updatetaskstatusstaff():
    data=request.get_json()
    response=sendtaskforapproval(data)
    
    if response=="True":
        current_time = datetime.now()
        time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        emailstaff,namestaff=getemailaddr(session["username"])
        email_body={"recipientmail":emailstaff,
                    "subject":"Task Sent For Approval",
                    "body":mails["Updatetaskstatusstaff"].format(namestaff=namestaff,repmanager=data["repmanager"],time_string=time_string,taskid=data['taskid'],taskname=data['taskname'],startdate=data['startdate'],enddate=data['enddate'],notes=data['notes'],addnotes=data['addnotes'])}
        updateemailscoll(email_body)
        
        emailmanager,namemanager=getemailaddr(data["repmanager"])
        email_body={"recipientmail":emailmanager,
                    "subject":"Task Approval Request Mail",
                    "body":mails["Updatetaskstatusmanager"].format(namemanager=namemanager,time_string=time_string,namestaff=namestaff,taskid=data['taskid'],taskname=data['taskname'],startdate=data['startdate'],enddate=data['enddate'],notes=data['notes'],addnotes=data['addnotes'],status=data['status'])}
        updateemailscoll(email_body)
    
    return {"Status":response}

@app2.route('/popuptasks')
def popup1():
    return render_template('taskspopup.html')

@app2.route('/popupleaves')
def popup2():
    return render_template('leavespopup.html')

@app2.route('/popuppullreq')
def popup3():
    return render_template('pullreqpopup.html')

@app2.route("/submitleaveapproval",methods=["POST"])
def leaveapproval():
    data=request.get_json()
    response=sendleaveforapproval(data)
    
    if response=="True":
        current_time = datetime.now()
        time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        emailstaff,namestaff=getemailaddr(data["empid"])
        email_body={"recipientmail":emailstaff,
                    "subject":"Leave Request Confiration Mail",
                    "body":mails["Leaverequeststaff"].format(namestaff=namestaff,repmanager=data['repmanager'],time_string=time_string,leaveid=data['leaveid'],startdate=data['startdate'],enddate=data['enddate'],notes=data['notes'],typeofleave=data['typeofleave'],leaveduration=data['leaveduration'])}
        updateemailscoll(email_body)
        
        emailmanager,namemanager=getemailaddr(data["repmanager"])
        email_body={"recipientmail":emailmanager,
                    "subject":"Leave Approval Request Mail",
                    "body":mails["Leaverequestmanager"].format(namemanager=namemanager,namestaff=namestaff,time_string=time_string,leaveid=data['leaveid'],startdate=data['startdate'],enddate=data['enddate'],notes=data['notes'],typeofleave=data['typeofleave'],leaveduration=data['leaveduration'])}
        updateemailscoll(email_body)
        
    return {"Status":response}

@app2.route("/approvaltask",methods=["POST"])
def sendapprovalstatus():
    data=request.get_json()
    response=approvaltaskstatus(data)
    
    if response=="True":
        current_time = datetime.now()
        time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        emailstaff,namestaff=getemailaddr(data["empid"])
        email_body={"recipientmail":emailstaff,
                    "subject":"Task Approval Confiration Mail",
                    "body":mails["Taskapprovalstaff"].format(namestaff=namestaff,username=session['username'],time_string=time_string,taskid=data['taskid'],taskname=data['taskname'],startdate=data['startdate'],enddate=data['enddate'],notes=data['notes'],addnotes=data['addnotes'],status=data['status'],approvalstatus=data['approvalstatus'])}
        updateemailscoll(email_body)
        
        emailmanager,namemanager=getemailaddr(session["username"])
        email_body={"recipientmail":emailmanager,
                    "subject":"Task Approval Confiration Mail",
                    "body":mails["Taskapprovalmanager"].format(namemanager=namemanager,namestaff=namestaff,username=session['username'],time_string=time_string,taskid=data['taskid'],taskname=data['taskname'],startdate=data['startdate'],enddate=data['enddate'],notes=data['notes'],addnotes=data['addnotes'],status=data['status'],approvalstatus=data['approvalstatus'])}
        updateemailscoll(email_body)
    else:
        current_time = datetime.now()
        time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        emailstaff,namestaff=getemailaddr(data["empid"])
        email_body={"recipientmail":emailstaff,
                    "subject":"Task Disapproval Mail",
                    "body":mails["Taskapprovalstaff"].format(namestaff=namestaff,username=session['username'],time_string=time_string,taskid=data['taskid'],taskname=data['taskname'],startdate=data['startdate'],enddate=data['enddate'],notes=data['notes'],addnotes=data['addnotes'],status=data['status'],approvalstatus=data['approvalstatus'])}
        updateemailscoll(email_body)
        
        emailmanager,namemanager=getemailaddr(session["username"])
        email_body={"recipientmail":emailmanager,
                    "subject":"Task Disapproval Mail",
                    "body":mails["Taskapprovalmanager"].format(namemanager=namemanager,namestaff=namestaff,username=session['username'],time_string=time_string,taskid=data['taskid'],taskname=data['taskname'],startdate=data['startdate'],enddate=data['enddate'],notes=data['notes'],addnotes=data['addnotes'],status=data['status'],approvalstatus=data['approvalstatus'])}
        updateemailscoll(email_body)
            
    return {"Status":response}

@app2.route("/approvalleave",methods=["POST"])
def sendleaveapprovalstatus():
    data=request.get_json()
    response=approvalleavestatus(data)
    
    if response=="True":
        current_time = datetime.now()
        time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        emailstaff,namestaff=getemailaddr(data["empid"])
        email_body={"recipientmail":emailstaff,
                    "subject":"Leave Approval Confiration Mail",
                    "body":mails["Leaveapprovalstaff"].format(namestaff=namestaff,username=session['username'],time_string=time_string,leaveid=data["leaveid"],startdate=data["startdate"],enddate=data["enddate"],notes=data["notes"],leaveduration=data["leaveduration"],requestdate=data["requestdate"],approvalstatus=data["approvalstatus"])}
        updateemailscoll(email_body)
        
        emailmanager,namemanager=getemailaddr(session["username"])
        email_body={"recipientmail":emailmanager,
                    "subject":"Leave Approval Confiration Mail",
                    "body":mails["Leaveapprovalmanager"].format(namemanager=namemanager,namestaff=namestaff,empid=data["empid"],time_string=time_string,leaveid=data["leaveid"],startdate=data["startdate"],enddate=data["enddate"],notes=data["notes"],leaveduration=data["leaveduration"],requestdate=data["requestdate"],approvalstatus=data["approvalstatus"])}
        updateemailscoll(email_body)
    else:
        current_time = datetime.now()
        time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        emailstaff,namestaff=getemailaddr(data["empid"])
        email_body={"recipientmail":emailstaff,
                    "subject":"Leave Disapproval Confiration Mail",
                    "body":mails["Leaveapprovalstaff"].format(namestaff=namestaff,username=session['username'],time_string=time_string,leaveid=data["leaveid"],startdate=data["startdate"],enddate=data["enddate"],notes=data["notes"],leaveduration=data["leaveduration"],requestdate=data["requestdate"],approvalstatus=data["approvalstatus"])}
        updateemailscoll(email_body)
        
        emailmanager,namemanager=getemailaddr(session["username"])
        email_body={"recipientmail":emailmanager,
                    "subject":"Leave Disapproval Confiration Mail",
                    "body":mails["Leaveapprovalmanager"].format(namemanager=namemanager,namestaff=namestaff,empid=data["empid"],time_string=time_string,leaveid=data["leaveid"],startdate=data["startdate"],enddate=data["enddate"],notes=data["notes"],leaveduration=data["leaveduration"],requestdate=data["requestdate"],approvalstatus=data["approvalstatus"])}
        updateemailscoll(email_body)
    
    return {"Status":response}

@app2.route("/updatetaskdetail",methods=["POST"])
def updatetaskdetail1():
    data=request.get_json()
    response=updatetaskdetail(data)
    
    if response=="True":
        current_time = datetime.now()
        time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        emailstaff,namestaff=getemailaddr(data["empid"])
        email_body={"recipientmail":emailstaff,
                    "subject":"Task Details Updation Mail",
                    "body":mails["Taskdetailsupdatestaff"].format(namestaff=namestaff,taskname1=data["taskname"],username=session["username"],time_string=time_string,taskid=data["taskid"],taskname2=data["taskname"],startdate=data["startdate"],enddate=data["enddate"],notes=data["notes"],status=data["status"])}
        updateemailscoll(email_body)
        
        emailmanager,namemanager=getemailaddr(session["username"])
        email_body={"recipientmail":emailmanager,
                    "subject":"Task Details Updation Mail",
                    "body":mails["Taskdetailsupdatemanager"].format(namemanager=namemanager,taskname1=data["taskname"],namestaff=namestaff,empid=data["empid"],time_string=time_string,taskid=data["taskid"],taskname2=data["taskname"],startdate=data["startdate"],enddate=data["enddate"],notes=data["notes"],status=data["status"])}
        updateemailscoll(email_body)
    
    return {"Status":response}

@app2.route("/collectempids")
def collectempid():
    response=collectempids()
    return response

@app2.route("/getempdetails",methods=["POST"])
def collectempdetails():
    data=request.get_json()
    response=getempdetails(data)
    return response

@app2.route("/sendpullrequest",methods=["POST"])
def submitpullreq():
    data=request.get_json()
    response=sendpullrequest(data)
    
    current_time = datetime.now()
    time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
    email,name=getemailaddr(data["currentrepmanager"])
    email_body={"recipientmail":email,
                "subject":"Pull Request Recieved",
                "body":mails["Pullrequestcurrentmanager"].format(name=name,requestingmanager1=data["requestingmanager"],time_string=time_string,empid=data["empid"],requestingmanager2=data["requestingmanager"])
                }
    updateemailscoll(email_body)
    
    email,name=getemailaddr(data["requestingmanager"])
    email_body={"recipientmail":email,
                "subject":"Pull Request Sent",
                "body":mails["Pullrequestreportingmanager"].format(name=name,currentrepmanager1=data["currentrepmanager"],time_string=time_string,empid=data["empid"],currentrepmanager2=data["currentrepmanager"])
                }
    updateemailscoll(email_body)
    
    return response

@app2.route("/sendpullrequestapproval",methods=["POST"])
def submitpullreqapp():
    data=request.get_json()
    response=sendpullrequestapproval(data)
    
    if response.get("Status")=="True" and data["approvalstatus"]=="Approve":
        current_time = datetime.now()
        time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        email,name=getemailaddr(session["username"])
        email_body={"recipientmail":email,
                "subject":"Pull Request Approved",
                "body":mails["Pullrequestapprcurrmanager"].format(name=name,empid1=data["empid"],time_string=time_string,empid2=data["empid"],requestingmanager=data["requestingmanager"],requestdate=data["requestdate"])
                }
        updateemailscoll(email_body)
        
        email,name=getemailaddr(data["requestingmanager"])
        email_body={"recipientmail":email,
                "subject":"Pull Request Approved",
                "body":mails["Pullrequestapprrepmanager"].format(name=name,empid1=data["empid"],username1=session["username"],time_string=time_string,empid2=data["empid"],username2=session["username"],requestdate=data["requestdate"])
                }
        updateemailscoll(email_body)
        
        email,name=getemailaddr(data["empid"])
        email_body={"recipientmail":email,
                "subject":"Manager Changed",
                "body":mails["Pullrequestemp"].format(name=name,username=session["username"],requestingmanager=data["requestingmanager"])
                }
        updateemailscoll(email_body)
    
    else:
        current_time = datetime.now()
        time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        email,name=getemailaddr(session["username"])
        email_body={"recipientmail":email,
                "subject":"Pull Request Dispproved",
                "body":mails["Pullreqcurrmanager"].format(name=name,empid1=data["empid"],time_string=time_string,empid2=data["empid"],requestingmanager=data["requestingmanager"],requestdate=data["requestdate"])}
        updateemailscoll(email_body)

        email,name=getemailaddr(data["requestingmanager"])
        email_body={"recipientmail":email,
                "subject":"Pull Request Disapproved",
                "body":mails["Pullreqrepmanager"].format(name=name,empid1=data["empid"],username1=session["username"],time_string=time_string,empid2=data["empid"],username2=session["username"],requestdate=data["requestdate"])
                }
        updateemailscoll(email_body)
    
    return response

@app2.route("/sendmails",methods=["POST"])
def sendmails():
    data=request.get_json()
    status="False"
    try:
        for value in data["empids"]:
            email,name=getemailaddr(value)
            email_body={"recipientmail":email,
                        "subject":data["subject"],
                        "body":data["emailbody"]}
            updateemailscoll(email_body)
            status="True"
    except Exception as e:
        print("Err Occ: ",e)
    return {"Status":status}

@app2.route("/submitempinfo",methods=["POST"])
def submitempinfo():
    data=request.get_json()
    response=createempinfo(data)
    
    emailstaff,namestaff=getemailaddr(data["empid"])
    email_body={"recipientmail":emailstaff,
                "subject":"Congratulations account created",
                "body":mails["Acccreatedstaff"].format(namestaff=namestaff,empid=data["empid"])}
    updateemailscoll(email_body)
    
    emailadmin,nameadmin=getemailaddr(session["username"])
    email_body={"recipientmail":emailadmin,
                "subject":f"Account creation successfull mail",
                "body":mails["Acccreatedmanager"].format(nameadmin=nameadmin,namestaff=namestaff,empid=data["empid"])}
    updateemailscoll(email_body)

    return response
    
@app2.route("/removeemp",methods=["POST"])
def removeemp1():
    data=request.get_json()
    response=removeemp2(data)
    return response

@app2.route("/checkuser",methods=["POST"])
def forgotpass():
    data=request.get_json()
    response=checkuser(data)
    
    if response["Status"]=="Emp Present":
        code = random.randint(10000, 99999)
        session["code"]=code
        print(session["code"])
        response["code"]=code    

        emailstaff,namestaff=getemailaddr(data["empid"])
        email_body={"recipientmail":emailstaff,
                    "subject":"Code for password change",
                    "body":f"Hey {namestaff}, code for changing password is {code}"}
        updateemailscoll(email_body) 
    
    return response

@app2.route("/changepass",methods=["POST"])
def changepassword():
    data=request.get_json()

    if int(data["code"])==session["code"]:
        response=changepass(data)
        if response["Status"]=="True":
            current_time = datetime.now()
            time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
            
            emailstaff,namestaff=getemailaddr(data["empid"])
            email_body={"recipientmail":emailstaff,
                        "subject":"Password Changed",
                        "body":mails["Passchanged"].format(namestaff=namestaff,empid=data["empid"],time_string=time_string)}
            updateemailscoll(email_body)
        return response
    else:
        return {"Status":"Code not matched"}

  
if __name__ == '__main__':
    app2.run(port='5001',debug=True)