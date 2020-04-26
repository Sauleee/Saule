import pymongo
import ssl
client = pymongo.mongo_client.MongoClient("mongodb+srv://pp2:pp2password@cluster0-yy11s.mongodb.net/test?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
mydb = client["mydatabase"] 
mycol = mydb["students"]

students = mycol.find().sort("name")
for x in students:
    print(x)

students = mycol.find().sort("name", -1)
for x in students:
    print(x)