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

# Analizamos y decimos a que otros usuarios somos más afines

@app.route("/Analizar/<name>/comunes")
@errorHandler

def AnalizarmasComunes(name):   
    query= (db.Project_Api.distinct("Name"))
    if name in query:
        query2 = list(db.Project_Api.distinct("Name"))
        lista = []
        for e in query2:
            query3 = list(db.Project_Api.find({"Name": e },{"_id":0, "Frase":1}))
            analizamos = sia.polarity_scores(str(query3).strip('[]'))
            lista.append({"Name": e, "neg": analizamos['neg'],  "neu": analizamos['neu'], "pos": analizamos['pos']})
        
        df = pd.DataFrame.from_dict(lista).set_index('Name').T
        distancia = pd.DataFrame(1/(1+ squareform(pdist(df.T, 'euclidean'))), index=df.columns, columns=df.columns)
        
        similar = distancia[name].sort_values(ascending=False)[1:4].index
        return ({f"Los usuarios que tiene en comun  {name} son": dumps(similar)})
    else:
        raise APIError(f"No existe el usuario {name}, pruebe con alguno de estos {query}")