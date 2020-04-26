import pymongo
import ssl
client = pymongo.mongo_client.MongoClient("mongodb+srv://pp2:pp2password@cluster0-yy11s.mongodb.net/test?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
mydb = client["mydatabase"]    #открываеем базу под именем "myDatabase"
print(client.list_database_names())   #что есть в Database


mydb = client['mydatabase']  #открываем collection
mycol = mydb["students"]
print(mydb.list_collection_names())    #что есть в collection



mydict={"name": "SAULE" , "surname" : "AKKALIEVA" , "_id" : "777" }     #пишем данные 
x = mycol.insert_one(mydict)                           #загружаем в коллекшин
print(x.inserted_id)


mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
x = mycol.insert_many(mylist)
print(x.inserted_ids)




