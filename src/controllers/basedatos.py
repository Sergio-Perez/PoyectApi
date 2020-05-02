from src.app import app
from pymongo import MongoClient
from src.config import DBURL
from bson.json_util import dumps
import re
from src.controllers.params import *
from src.helpers.errorHandler import errorHandler, Error404
#Nos conectamos a MongoDb
client = MongoClient(DBURL)
print(f"Connected to MongoDb")
db = client.get_default_database()

# Creamos una ruta en la Api para buscar por chats.
@app.route("/chat/<name>")
@errorHandler
#@params
def getChat(name):
    
    chatname = re.compile(f"^{name}", re.IGNORECASE)
    chat = list(db.Project_Api.find({"Chat": chatname},{"_id":0, "Name":1, "Frase":1, "Date":1}))
    print(chatname)
    if not chatname:
        print("ERROR")
        raise Error404("Chat not found")
    
    return dumps(chat)

# Creamos una ruta en la Api para buscar los nombres 
@app.route("/<name>")
@errorHandler
#@params
def getName(name):
    
    namereg = re.compile(f"^{name}", re.IGNORECASE)
    name = list(db.Project_Api.find({"Name": namereg}, { "_id":0, "Name":1, "Frase":1,"Date":1}))
    print(namereg)
    if not name:
        print("ERROR")
        raise Error404("Name not found")
    
    return dumps(name)


