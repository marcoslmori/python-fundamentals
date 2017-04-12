# mongodb.py
from pymongo import MongoClient


client = MongoClient('127.0.0.1')
db = client['devops']

#insert

 db.fila.insert({
 		"_id": 2, 
 		"servico": "intranet",
 		"status": 0
 	})


db.fila.insert({
 		"_id": 3, 
 		"servico": "dns",
 		"status": 0
 	})
# control + / para comentar tudo


#update


db.fila.update(
	{"_id": 1, "servico": "dns"},
	{"$set": {"status": 1}}

	)

# remove
db.fila.remove({"_id": 2})

# find
for d in db.fila.find({}):
	print d





