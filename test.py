import pymongo
import os

usernamedb=os.getenv('usernamedb')
password=os.getenv('password')

connection_url = f"mongodb+srv://{usernamedb}:{password}@cluster0.znfsndq.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_url)
db=client["EmployeeManagementSystem"]
# collection=db["Admin"]

# d=collection.find_one({"empid":"Admin"})

# print(d)


collection=db["Emails"]
collection.insert_one({"data":[]})