import pymongo
import ssl
client = pymongo.mongo_client.MongoClient("mongodb+srv://pp2:pp2password@cluster0-yy11s.mongodb.net/test?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
mydb = client["mydatabase"] 
mycol = mydb["students"]

query = { "address": "Mountain 21" }
mycol.delete_one(query)

query = { "address": {"$regex": "^S"} }
x = mycol.delete_many(query)
print(x.deleted_count, "documents deleted.")

x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")

 
mycol.drop()  #delete collection