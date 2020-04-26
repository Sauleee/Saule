import pymongo
import ssl
client = pymongo.mongo_client.MongoClient("mongodb+srv://pp2:pp2password@cluster0-yy11s.mongodb.net/test?retryWrites=true&w=majority",ssl_cert_reqs=ssl.CERT_NONE)
mydb = client["mydatabase"] 
mycol = mydb["students"]

studentnum1 = mycol.find_one()  #возвращает первое значение
print(studentnum1)

students = mycol.find()
for x in students:       
    print(x)

students = mycol.find()
for x in students:
    print(x['name'])   #только имена выйдут

students = mycol.find({}, {"_id": 0 , "name" : 1 , "address" : 1})
for x in students:
    print(x)

myresult = mycol.find().limit(5)
for x in myresult:          #сколько строку ты хочешь вывести
    print(x)



