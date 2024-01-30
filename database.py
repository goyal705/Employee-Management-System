from flask import session
import pymongo
import re
from datetime import datetime
import random
import string
import hashlib
import os

usernamedb=os.getenv('usernamedb')
password=os.getenv('password')

def handlesignin(data):
    connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_url)
    db = client["EmployeeManagementSystem"]
    collection = db["Employees"]
    data["password"]=hashpass(data["password"])
    cursor = collection.find(data)
    response={"UserPresent":"False","usertype":None}
    
    for document in cursor:
        response={"UserPresent":"True","usertype":document.get("usertype")}

    client.close()
    return response

def hashpass(password):
    salt = "1234567890abcdefghijklmnopqrstuvwxyz"
    dataBase_password = password+salt
    hashed = hashlib.md5(dataBase_password.encode())
 
    passwordhash=hashed.hexdigest()
    return passwordhash

def showpersonaldetails():
    username=session.get("username")
    connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_url)
    db = client["EmployeeManagementSystem"]
    collection = db[(username)]
    projection = {"_id": 0}
    cursor = collection.find_one({"empid":username},projection)
    # cursor = collection.find({"empid":username},projection)
    # for document in cursor:
    #     client.close()
    #     return document    
    # return "None"
    return cursor


def assigntasks(data):
    status=""
    try:
        assignee=data["empid"]
        connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(connection_url)
        db = client["EmployeeManagementSystem"]
        collection = db[assignee]
        collection.find_one({"empid":assignee})
        data["status"]="Incomplete"
        data["taskid"]=generaterandomid()
        collection.update_one(
        {"empid": assignee},
        {"$push": {"tasks": data}}
        )
        status= "True"
    except Exception as e:
        print("Err occ: ",e)
        status= "False"
    finally:
        client.close()
        appendtaskprogres(data)
        return status


def appendtaskprogres(data):
    username=session["username"]
    assignee=data.get("empid")

    connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_url)
    db = client["EmployeeManagementSystem"]
        
    collection = db[username]
    data["empid"]=assignee
    collection.update_one(
        {"empid": username},
        {"$push": {"tasks_given": data}}
        )
    client.close()

def sendtaskforapproval(data):
    status="False"
    try:
        username=session["username"]
        repmanager=data["repmanager"]

        connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(connection_url)
        db = client["EmployeeManagementSystem"]
            
        collection = db[repmanager]
        data["empid"]=username
        condition = {
            "empid": repmanager,
            "tasks.1.taskrelated": {
            "$not": {
                "$elemMatch": {
                    "taskid": data["taskid"],
                }
            }
            }
        }

        existing_data = collection.find_one(condition)
        if existing_data:
            collection.update_one(
                {"empid":data["repmanager"]},
                {"$push": {"tasks.1.taskrelated": data}}
            )
            print("Data updated.")
        else:
            print("Data already present with the same status.")
            collection.update_one(
                {"empid":data["repmanager"],"tasks.1.taskrelated":{"$elemMatch": {
                    "taskid": data["taskid"]
                }}},
                {"$set": {"tasks.1.taskrelated.$.addnotes": data["addnotes"]}}
            )
        
        status="True"
    except Exception as e:
        status="False"
        print("An error occ ",e)
    finally:
        client.close()
        return status

def sendleaveforapproval(data):
    status="False"
    repmanager=data["repmanager"]
    current_date = datetime.now().date()
    formatted_date = current_date.strftime("%Y-%m-%d")
    data["reqdate"]=formatted_date
    data["leaveid"]=generaterandomid()
    try:
        connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(connection_url)
        db = client["EmployeeManagementSystem"]        
        collection = db[repmanager]
        condition = {
            "empid": repmanager,
            "tasks.0.leavesrelated": {
            "$not": {
                "$elemMatch": {
                    "empid": data["empid"],
                    "startdate":data["startdate"],
                    "enddate":data["enddate"],
                    "partialdays":data["partialdays"]
                }
            }
            }
        }

        existing_data = collection.find_one(condition)
        if existing_data:
            collection.update_one(
                {"empid":data["repmanager"]},
                {"$push": {"tasks.0.leavesrelated": data}}
            )
            print("Leave Data updated.")
        else:
            print("Leave Data already present with the same status.")
            collection.update_one(
                {"empid":data["repmanager"],"tasks.0.leavesrelated":{"$elemMatch": {
                    "empid": data["empid"],
                    "leaveid":data["leaveid"],
                    "startdate":data["startdate"],
                    "enddate":data["enddate"],
                    "partialdays":data["partialdays"]
                }}},
                {"$set": {"tasks.0.leavesrelated.$.notes": data["notes"]}}
            )
        
        status="True"

    except Exception as e:
        print("An error occ: ",e)
    finally:
        client.close()
        updateuserleavedata(data)
        return status

def updateuserleavedata(data):
    try:
        typeofleave=data["typeofleave"]
        leavetype=typeofleave.split(" ")[0].strip()
        leavecount=typeofleave.split(" ")[1].strip()
        regex = r'\((\d+(\.\d+)?)\)'
        match = re.search(regex, leavecount)
        leavecount = match.group(1)
        
        connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(connection_url)
        db = client["EmployeeManagementSystem"]        
        updatedleaves=str(float(leavecount)-float(data["leaveduration"]))

        collection = db[data["empid"]]
        collection.update_one(
                {"empid":data["empid"]},
                {"$set": {f"leaves.0.{leavetype}": updatedleaves}}
            )
        collection.update_one(
            {"empid":data["empid"]},
            {"$push":{"leaves_taken":{
                "leaveid":data["leaveid"],
                leavetype:data["leaveduration"],
                "requestdate":data["reqdate"],
                "startdate":data["startdate"],
                "enddate":data["enddate"],
                "status":"Gone For Approval"
            }}}
        )
        print("data updated")
    except Exception as e:
        print("Error Occ:",e)
    finally:
        client.close()

def approvaltaskstatus(data):
    status="False"
    try:
        connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(connection_url)
        db = client["EmployeeManagementSystem"]
        
        if data["approvalstatus"]=="Approve":
            #updating staff collection
            collection=db[data["empid"]]
            update_query = {
                "$set": {
                "tasks.$.status": "Complete"
                }
            }

            filter_query = {
                    "tasks.taskid": data["taskid"]
                }
                
            collection.update_one(filter_query,update_query)
            print(f"Updated status of {data['taskname']} to Complete in {data['empid']}")
            
            #updating manager collection
            collection=db[session["username"]]
            filter_query={"tasks_given.taskid":data["taskid"]}
            update_query={"$set":{"tasks_given.$":data}}
            collection.update_one(filter_query,update_query)
            
            deletetaskdatamanager(data)
            status="True" 
        else:
            status="Not Changed"
            deletetaskdatamanager(data)
         
    except Exception as e:
        print("Error Occ ",e)        
    finally:
        client.close()
        return status

def deletetaskdatamanager(data):
    username=session.get("username")
    try:
        connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(connection_url)
        db = client["EmployeeManagementSystem"]
        collection=db[username]

        filter_query = {"empid": username,"tasks.taskrelated.taskid":data["taskid"],"tasks.taskrelated.empid":data["empid"]}
        update_query = {"$pull":{"tasks.$.taskrelated": 
                                    {"empid": data["empid"],
                                    "taskid":data["taskid"]
                                    }
                                }
                        }
        collection.update_one(filter_query, update_query)

    except Exception as e:
        print("err occ",e)
    finally:
        client.close()

def approvalleavestatus(data):
    status="False"
    try:
        connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(connection_url)
        db = client["EmployeeManagementSystem"]
        
        if data["approvalstatus"]=="Approve":
            #updating staff collection if leave approved status would change to approved otherwise leave would get back to original place
            collection=db[data["empid"]]
            update_query = {
                "$set": {
                "leaves_taken.$.status": "Approved"
                }
            }

            filter_query = {
                    "leaves_taken.leaveid": data["leaveid"],
                }
                
            collection.update_one(filter_query,update_query)
            deleteleavedatamanager(data)
            status="True" 
        else:
            collection=db[data["empid"]]
            
            originalleaveplustype=data["typeofleave"]
            match = re.search(r'(\w+) \((\d+(?:\.\d+)?)\)', originalleaveplustype)
            typeleave = match.group(1).strip()
            originalleaveno = match.group(2).strip()

            filter_query={"empid": data["empid"]}
            update_query={"$set":{
                f"leaves.0.{typeleave}":originalleaveno,
            }}
            collection.update_one(filter_query,update_query)
            
            update_query = {
                "$set": {
                "leaves_taken.$.status": "Disapproved"
                }
            }

            filter_query = {
                    "empid": data["empid"],
                    "leaves_taken.leaveid":data["leaveid"]
                }
                
            collection.update_one(filter_query,update_query)
            
            deleteleavedatamanager(data)
            status="Disapproved"
    except Exception as e:
        print("Error Occ ",e)        
    finally:
        client.close()
        return status

def deleteleavedatamanager(data):
    username=session.get("username")
    try:
        connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(connection_url)
        db = client["EmployeeManagementSystem"]
        collection=db[username]

        filter_query = {"empid": username,"tasks.leavesrelated.leaveid":data["leaveid"]}
        update_query = {"$pull":{"tasks.$.leavesrelated": {"leaveid": data["leaveid"],"empid":data["empid"]}}}
        collection.update_one(filter_query, update_query)

    except Exception as e:
        print("err occ",e)
    finally:
        client.close()        

def updateemailscoll(data):
    connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_url)
    db = client["EmployeeManagementSystem"]
    collection=db["Emails"]
    update_query={"$push":{"data":data}}
    collection.update_one({},update_query)
    client.close()

def updatetaskdetail(data):
    status="False"
    connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_url)
    db = client["EmployeeManagementSystem"]
    try:
        #updating manager taskgiven
        collection=db[session["username"]]
        filter_query={"tasks_given.taskid":data["taskid"],"tasks_given.empid":data["empid"]}
        update_query={"$set":{"tasks_given.$":data}}
        collection.update_one(filter_query,update_query)

        #updating staff tasks
        collection=db[data["empid"]]
        filter_query={"tasks.taskid":data["taskid"],"tasks.empid":data["empid"]}
        update_query={"$set":{"tasks.$":data}}
        e=collection.update_one(filter_query,update_query)
        print(e.matched_count)
        status="True"
    except Exception as e:
        print("An err occ:",e)
        
    finally:
        client.close()
        return status

def getemailaddr(empid):
    connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_url)
    db = client["EmployeeManagementSystem"]
    collection=db[empid]
    email=collection.find_one({})["emailaddr"]
    name=collection.find_one({})["emp_name"]
    return email,name
    
def generaterandomid():
    characters = string.ascii_letters + string.digits + "+"
    code = ''.join(random.choices(characters, k=10))
    
    # connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
    # client = pymongo.MongoClient(connection_url)
    # db = client["EmployeeManagementSystem"]
    # collection=db["Ids"]
    
    #checks if generated id exists in collection

    # id=collection.find_one({})["id"]
    # if code in id:
    #     #same id found
    #     generaterandomid()
    # collection.update_one({},{"$push":{"id":code}})   
    # client.close()
    return code

def collectempids():
    connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_url)
    db = client["EmployeeManagementSystem"]
    collection=db["Employees"]
    alldocs=collection.find()
    empids=[]
    for document in alldocs:
        if document.get("username")!=session["username"]:
            empids.append(document.get("username"))
    client.close()
    return {"response":empids}


def getempdetails(data):
    empid=data["empid"]
    connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_url)
    db = client["EmployeeManagementSystem"]
    collection=db[empid]
    cursor=collection.find_one({"empid":empid})
    client.close()
    response={
        "empname":cursor.get("emp_name"),
        "department":cursor.get("department"),
        "techstack":cursor.get("techstack"),
        "designation":cursor.get("designation"),
        "manager":cursor.get("repmanager")
    }
    return response

def sendpullrequest(data):
    current_time = datetime.now()
    time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
    data["requestdate"]=time_string
    status="False"
    try:
        connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(connection_url)
        db = client["EmployeeManagementSystem"]
        
        #then would update current manager pullrequestrelated
        collection=db[data["currentrepmanager"]]
        collection.update_one({
            "empid":data["currentrepmanager"]},
            {"$push":{
                "tasks.2.pullrequestrelated":data  
            }})
        
        #first would update new manager pullrequest
        data["status"]="Gone For Approval"
        collection=db[data["requestingmanager"]]
        collection.update_one({
            "empid":data["requestingmanager"]},
            {"$push":{
                "pullrequests":data
            }})    
        
        status="True"    
    except Exception as e:
        print("Err occ: ",e)
    finally:
        client.close()
        return {"Status":status}

def sendpullrequestapproval(data):
    status="False"
    try:
        connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(connection_url)
        db = client["EmployeeManagementSystem"]
        
        if data["approvalstatus"]=="Approve":
            collection=db[session["username"]]
            
            #updating current manager pullrequestrelated deleting request from it
            collection.update_one({"empid":session["username"],"tasks.pullrequestrelated.empid":data["empid"]},{
                    "$pull":{
                        "tasks.$.pullrequestrelated":{
                            "empid":data["empid"],
                            "requestingmanager":data["requestingmanager"],
                            "requestdate":data["requestdate"]
                        }  
            }})
            
            #deleting the pulled emp form the personreporting array
            collection.update_one({"empid":session["username"]},{"$pull":{"personreporting":data["empid"]}})         

            ##################################################################################################

            collection=db[data["requestingmanager"]]
            #updating pullrequest status to approved in newmanager
            collection.update_one({"empid":data["requestingmanager"],"pullrequests.empid":data["empid"],"pullrequests.requestdate":data["requestdate"]},{"$set":{
                "pullrequests.$.status":"Approved"
            }})
            
            #updating personreporting array in newmanager with new emp
            collection.update_one({"empid":data["requestingmanager"]},{"$push":{"personreporting":data["empid"]}})
            
            #updating empid collection to new repmanager
            collection=db[data['empid']]
            collection.update_one({"empid":data["empid"]},{"$set":{"repmanager":data["requestingmanager"]}})
        else:
            collection=db[session["username"]]
            
            #updating current manager pullrequestrelated deleting request from it
            collection.update_one({"empid":session["username"],"tasks.pullrequestrelated.empid":data["empid"]},{
                    "$pull":{
                        "tasks.$.pullrequestrelated":{
                            "empid":data["empid"],
                            "requestingmanager":data["requestingmanager"],
                            "requestdate":data["requestdate"]
                        }  
            }})

            ##################################################################################################

            collection=db[data["requestingmanager"]]
            #updating pullrequest status to disapproved in newmanager
            collection.update_one({"empid":data["requestingmanager"],"pullrequests.empid":data["empid"],"pullrequests.requestdate":data["requestdate"]},{"$set":{
                "pullrequests.$.status":"Disapproved"
            }})
        status="True"
    except Exception as e:
        print("An err occ ",e)
    finally:
        client.close()
        return {"Status":status}        

def createempinfo(data):
    status="Flase"
    try:
        connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(connection_url)
        db = client["EmployeeManagementSystem"]
        
        #adding empusername and pass in employees collection
        collection=db["Employees"]
        new_document={"username":data["empid"],
                      "password":hashpass(data["dob"]),
                      "usertype":data["emptype"]}
        collection.insert_one(new_document)
        
        #inserting data to new emp collection
        collection=db[data["empid"]]
        #for staff
        if data["emptype"]=="Staff":
            query={
                "emptype":data["emptype"],
                "empid": data["empid"],
                "emp_name": data["empname"],
                "dob":data["dob"],
                "contact":data["contactnumber"] ,
                "address": data["address"],
                "emailaddr": data["email"],
                "designation": data["designation"],
                "salary":data["salary"],
                "doj": data["dateofjoining"],
                "department": data["department"],
                "techstack":data["techstack"],
                "repmanager": session["username"],
                "tasks": [],
                "leaves": [{
                    "el": "15.0",
                    "sl": "10",
                    "cl": "12.0"}],
                "leaves_taken": []
            }
        #for manager
        else:
            query={
                "emptype":data["emptype"],
                "empid": data["empid"],
                "emp_name": data["empname"],
                "dob":data["dob"],
                "contact":data["contactnumber"] ,
                "address": data["address"],
                "emailaddr": data["email"],
                "designation": data["designation"],
                "salary":data["salary"],
                "doj": data["dateofjoining"],
                "department": data["department"],
                "techstack":data["techstack"],
                "repmanager": session["username"],
                "tasks": [{"leavesrelated": []},{"taskrelated":[]},{"pullrequestrelated": []}],
                "leaves": [{"el": "15.0","sl": "10","cl": "12.0"}],
                "leaves_taken": [],
                "personreporting":[],
                "tasks_given": [],
                "pullrequests": [],
            }
            
        collection.insert_one(query)
        
        #adding to admin collection
        collection=db[session["username"]]
        collection.update_one({},{"$push":{"emps":data["empid"]}})
        
        status="True"
    except Exception as e:
        print("Err Occ: ",e)
    finally:
        client.close()
        return {"Status":status}        

def removeemp2(data):
    connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_url)
    db = client["EmployeeManagementSystem"]
    status=""
    try:        
        collection=db[data["empid"]]
        repmanager=collection.find_one({})["repmanager"]
        emptype=collection.find_one({})["emptype"]
        if emptype=="Manager":
            collection=db[data["empid"]]
            personsreporting=collection.find_one({})["personreporting"]
            if len(personsreporting)>0:
                collection=db["Admin"]
                for i in personsreporting:
                    collection.update_one({"empid":"Admin"},{"$push":{"personreporting":i}})
                    collection=db[i]
                    collection.update_one({"empid":i},{"$set":{"repmanager":"Admin"}})

        #delete from its reporting manager      
        collection=db[repmanager]
        collection.update_one({"empid":repmanager},{"$pull":{"personreporting":data["empid"]}})         

        #delete from admin emps
        collection=db[session["username"]]
        collection.update_one({"empid":session["username"]},{"$pull":{"emps":data["empid"]}})
        
        #deleting from employees collection
        collection=db["Employees"]
        collection.delete_one({"username":data["empid"]})
            
        #delete emp collection
        collection=db[data["empid"]]
        collection.drop()
        
        status="True"
    except Exception as e:
        print("An err occ: ",e)
        status="False"
    finally:
        client.close()
        return {"Status":status,"repmanager":repmanager}
        
def checkuser(data):
    empname="null"
    status="Emp Not Present"
    emailaddr="null"
    connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_url)
    db = client["EmployeeManagementSystem"]
    try:
        userexist=data["empid"] in db.list_collection_names()
        if userexist:
            collection=db[data["empid"]]
            empname=collection.find_one({})["emp_name"]
            emailaddr=collection.find_one({})["emailaddr"]
            status="Emp Present"
    except Exception as e:
        print("Err Occ: ",e)
        status="False"
    finally:
        client.close()
        return {"Status":status,"empname":empname,"emailaddr":emailaddr}

def changepass(data):
    connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(connection_url)
    db = client["EmployeeManagementSystem"]    
    collection=db["Employees"]
    try:
        newpass=hashpass(data["newpass"])
        e=collection.update_one({"username":data["empid"]},{"$set":{"password":newpass}})
        status="True"
    except Exception as e:
        print("An err occ: ",e)
        status="False"
    finally:
        client.close()
        return {"Status":status}
    
    