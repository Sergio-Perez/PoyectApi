from src.app import app
from pymongo import MongoClient
from src.config import DBURL
from bson.json_util import dumps
import re

from src.helpers.errorHandler import errorHandler, Error404
#Nos conectamos a MongoDb
client = MongoClient(DBURL)
print(f"Connected to {DBURL}")
db = client.get_default_database()

# Creamos una ruta en la Api para buscar por chats.
@app.route("/chat/<name>")
@errorHandler
def getChat(name):
    chatname = re.compile(f"^{name}", re.IGNORECASE)
    chat = list(db.Project_Api.find({"chat": chatname},{"_id":0, "name":1, "frase":1, "date":1}))
    print(chatname)
    if not name:
        print("ERROR")
        raise Error404("Chat not found")
    print("OK")
    return dumps(chat)

# Creamos una ruta en la Api para buscar los nombres 
@app.route("/<name>")
@errorHandler
def getName(name):
    namereg = re.compile(f"^{name}", re.IGNORECASE)
    name = list(db.Project_Api.find({"name": namereg}, { "_id":0, "name":1, "frase":1,"date":1}))
    print(namereg)
    if not name:
        print("ERROR")
        raise Error404("Name not found")
    print("OK")
    return dumps(name)


#@app.route("/<name>")
#@errorHandler
#def getDate(fecha):
#    namereg = re.compile(f"^{name}", re.IGNORECASE)
#    name = db.find_one({"name": namereg}, { "_id":0, "name":1, "frase":1,"date":1})
#    print(namereg)
#    if not name:
#        print("ERROR")
#        raise Error404("Name not found")
#    print("OK")
#    return dumps(name)