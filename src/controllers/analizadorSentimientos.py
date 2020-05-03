import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from src.helpers.errorHandler import *
from src.app import app
from pymongo import MongoClient
from src.config import DBURL
from bson.json_util import dumps
from src.controllers.nuevoUsuarios import creando
import pandas as pd
import numpy as np
from scipy.spatial.distance import euclidean, pdist, squareform

# Me conecto a MongoDb
client = MongoClient(DBURL)
db = client.get_default_database()

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()
sia.polarity_scores

# Devolvemos las frases analizadas  
@app.route("/Analizar/<name>/lista")
@errorHandler
def AnalizarUsuario(name):
    query = list(db.Project_Api.find({"Name": name},{"_id":0,"Frase":1}))
    if not query:
        raise APIError(f"No existe el usuario {name}")    
    
    z = {}
    for e in query[0]["Frase"]:
   
        d = sia.polarity_scores(e)
        z.update({e : d})
    
    return dumps(z)

# Analizamos las frases de todo un chat
@app.route("/Analizar/<chat>")
@errorHandler
def AnalizarFrase(chat):
    query = list(db.Project_Api.find({"Chat": chat},{"_id":0,"Frase":1}))
    if not query:
        raise APIError(f"No existe el Chat {chat}") 
    return sia.polarity_scores(str(query).strip('[]'))

    z=""""""
    for e in chat3:
        d =(str(e["Frase"]).strip("[]"))
        z += d
   
    return sia.polarity_scores(z)    

# Analizamos todas las frases de todos los chats

@app.route("/Analizar/<name>/comunes")
@errorHandler
def AnalizarmasComunes(name):
    query = list (db.Project_Api.distinct("Name"))
    contenedor = []
    print("hola")
    if  name not in query:
        raise APIError(f"No existe el usuario {name}, pruebe con alguno de estos {query}") 
    for e in query:
        query = list(db.Project_Api.find({"Name": e },{"_id":0, "Frase":1}))
        analizamos = sia.polarity_scores(str(query).strip('[]'))
        contenedor.append({"Name": e, "neg": analizamos['neg'],  "neu": analizamos['neu'], "pos": analizamos['pos']})
        distancia = pd.DataFrame.from_dict(contenedor).set_index('Name').T 
        similar = distancia[name].sort_values(ascending=False)[1:5].index
        return {f"The users that have more in commun with {name} are ": dumps(similar)}