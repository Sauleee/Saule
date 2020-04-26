import pymongo
import ssl
client = pymongo.mongo_client.MongoClient("mongodb+srv://pp2:pp2password@cluster0-yy11s.mongodb.net/test?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
mydb = client["mydatabase"] 
mycol = mydb["students"]

query = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }
mycol.update_one(query, newvalues)

#for x in mycol.find():
#    print(x)

query = { "address": { "$regex": "^S" } }  
newvalues = { "$set": { "name": "Minnie" } }
x = mycol.update_many(query, newvalues)

#print(x.modified_count, "documents updated.")