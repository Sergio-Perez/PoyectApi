from src.app import app
from pymongo import MongoClient
from src.config import DBURL
from bson.json_util import dumps
import re
from src.helpers.errorHandler import *



# Me conecto a MongoDb
client = MongoClient(DBURL)
db = client.get_default_database()["Project_Api"]

# Vamos a devolver todos los mensajes de un chat.
@app.route("/chat/<chat>/lista")
@errorHandler
def listallFrases(chat):
    
    
    
    query = list(db.Project_Api.find({"Chat": chat},{"_id":0, "Name":1, "Frase":1, "Date":1}))
    print(query)
    #query = db.find_all({"Chat": chat_id})
    
    if query:
        raise APIError(f"No existe el chat {chat},pruebe con alguno de estos {query}")
    
    
    querysalida = list(db.Project_Api.find({"$and":[{"Chat" : chat},{"Frase":{ "$exists": True }}]}))
    return dumps(querysalida)
