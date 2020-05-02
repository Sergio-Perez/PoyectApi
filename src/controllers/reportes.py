from src.app import app
from pymongo import MongoClient
from src.config import DBURL
from bson.json_util import dumps
import re
from src.helpers.errorHandler import *



# Me conecto a MongoDb
client = MongoClient(DBURL)
print(f"Connected to MongoDb")
db = client.get_default_database()

# Vamos a devolver todos los mensajes de un chat.
@app.route("/chat/<chat>/lista")
@errorHandler
def listallFrases(chat):
    
    chatname = re.compile(f"^{chat}", re.IGNORECASE)
    query = list(db.Project_Api.find({"Chat": chatname},{"_id":1, "Name":1, "Frase":1, "Date":1}))   
    query2 = list(db.Project_Api.find({"Chat" :{ "$exists": True }},{"_id":0, "Name":0, "Frase":0, "Date":0}))   
    if not query:
        raise APIError(f"No existe el chat {chat}, pruebe con alguno de estos {query2}")    
    
    querysalida = list(db.Project_Api.find({"$and":[{"Chat" : chat},{"Frase":{ "$exists": True }}]}))
    z={}
    for e,prueba  in enumerate(querysalida):
         z.update({prueba['Name']:prueba['Frase']})
    
    return dumps(z)
