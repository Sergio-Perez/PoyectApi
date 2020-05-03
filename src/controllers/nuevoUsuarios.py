from src.app import app
from pymongo import MongoClient
from src.config import DBURL
from bson.json_util import dumps
import time
from src.helpers.errorHandler import *
from src.controllers.params import *


# Me conecto a MongoDb
client = MongoClient(DBURL)
db = client.get_default_database()["Project_Api"]

# Damos la opción de crear usuario,chat y frase con parámetros de una vez. 
@app.route("/create")
@errorHandler
@params
def creando(name,chat=[],frase=[]): 
    query = list(db.find({"Name": name},{"_id":0}))
    if query:
        raise APIError (f"Name {name} ya exite")
    
    nuevo = {'Chat': chat, 'Name': name, 'Frase': frase, 'Date': time.strftime("%m/%d/%Y %I:%M %p") }
    nuevo["_id"]= db.insert_one(nuevo).inserted_id
    print(nuevo)
    return dumps(nuevo)

# De esta manera solo creamos el chat
@app.route("/create/chat/<chat>")
@errorHandler

def crearChat(chat):
    query  =list(db.find({"Chat" : chat},{"_id":0}))
    if query:
        raise APIError (f"Chat {chat} ya existe")
    x = db.insert_one({"Chat": chat, "Name" : [], "Frase" : [],"Date":time.strftime("%m/%d/%Y %I:%M %p")})
    chat_id = x.inserted_id
    return dumps([chat_id,{"Chat": chat}])

# Aqui añadimos un usuario a un chat
@app.route("/chat/<chat>/name/<name>")
@errorHandler

def anadirUsario(chat,name):
    query = list(db.find({"Name": name},{"_id":0}))
    if query:
        raise APIError (f"Name {name} ya exite")
    x = db.insert_one({"Chat":chat,"Name":name,"Frase": [],"Date": time.strftime("%m/%d/%Y %I:%M %p")})
    usuario = x.inserted_id    
    print(chat,name)
    return dumps([usuario,{"Name":name}])

# Aqui añadimos al usuario en un chat
@app.route("/anadir/<chat>/<name_id>")
@errorHandler

def anadirUsChat(chat,name_id): 
    
    query = list(db.find({"Chat":chat,"Name":name_id},{"_id":0}))
    if query:
        raise APIError(f"El usuario {name_id} ya esta en ese chat")
    
    query2 = list(db.find({"Name": name_id},{"__id": 0}))    
    if not query:
        creando(name_id) 

    x = db.update({"Name": name_id},{"$set":{"Chat":chat}})
    print(chat)
    return dumps([{"Chat" :chat}])

# Añadimos una frase a un usuario
@app.route("/anadir/<chat>/<name>/<frase>")
@errorHandler

def anadirFrases(chat,name,frase): 
    
    query = list(db.find({"Chat":chat,"Name":name},{"_id":0}))
    if not query:
        raise APIError(f'Este usuario {name}, no esta en el chat {chat} si quiere cambiarse use "/anadir/<nombre del chat>/<nombre de su usuario>/ y podra cambiarse a ese chat')
      
    x = db.update({"Name": name},{"$push":{"Frase":{"$each":[frase]}}})
    print(frase)
    return dumps([{"Name":name,"Frase" :frase}])



