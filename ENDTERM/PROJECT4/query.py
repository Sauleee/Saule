import pymongo
import ssl
client = pymongo.mongo_client.MongoClient("mongodb+srv://pp2:pp2password@cluster0-yy11s.mongodb.net/test?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
mydb = client["mydatabase"] 
mycol = mydb["students"]


query = { "name" : "SAULE"}
students = mycol.find(query)
for x in students:     #выйдут одинаковые имена если они есть
    print(x)


query = { "address": { "$gt": "S" } }  #greater than "S"
students = mycol.find(query)
for x in students:
    print(x)


query = { "address": { "$regex": "^S" } }
students = mycol.find(query)
for x in students:
    print(x)