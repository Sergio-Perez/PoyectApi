import json
from pymongo import MongoClient
import random
from src.config import *
# Abro mongodb
print(f"Conectando a MongoDb")
client = MongoClient({DBURL})
# Cargo archivo de conversaciones
with open(archivoDescarga,"r") as archivo:
    data =json.load(archivo)

# Separo en dos variables  dos listas con autores y frases
autores = list(data.keys())
frases=list(data.values())

# Genero una función para sacar autores aleatoriamente 
def selecAutores(autores,numero):
    a=[]
    for nombre in range(0,numero):    
        a.append(random.choice(autores))
    return a
autor = selecAutores(autores,900)
print(elem)

# Genero una función para sacar frases aleatoriamente 
def selecFrases(autores,numero):
    a=[]
    for num in range(0,numero):    
        a.append(random.choice(autores))
    return a
fras = selecFrases(frases,900)


# Genero una función para sacar fechas aleatorias
import random
import time

def str_time_prop(start, end, format, prop):
    """Obtenga un tiempo en una proporción de un rango de dos tiempos formateados.

     start y end deben ser cadenas que especifiquen tiempos formateados en el
     formato dado (estilo strftime), dando un intervalo [inicio, fin].
     prop especifica cómo una proporción del intervalo que se tomará después
     comienzo. El tiempo devuelto estará en el formato especificado.
     """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))

# Genero las fechas aleatorias
def random_date(start, end, numero):
    time = []
    for e in range(0,numero):
        time.append(str_time_prop(start, end, '%m/%d/%Y %I:%M %p', random.random()))
    return time

time = random_date("1/1/2019 1:30 PM", "1/1/2020 4:50 AM", len(fras))



# Creamos una lista de dicionarios de miembros y sus chats 
def crearMiembro(autor,frase,date):
    chats =["La cofradia de San Pete","La sede de la peña","Vulvas con mascarilla","Chat de gurdus","Pussychat","La orquesta del Titanic","Ironhack","Esto es un inferno","Dos mejor que uno"]
    d=[]
    ch = []
    for chat in range(0,len(autor)):
        
        ch.append(random.choice(chats))
   
    for c, n, j, s in zip( ch,autor, frase, date):
        person = { 'chat':c, 'name': n, 'frase': j, 'date': s }
        d.append(person)
    return d
miembros = crearMiembro(autor,fras,time)

# Creamos un json de nuestros datos
json_object = json.dumps(miembros, indent = 4)   
with open("sample.json", "w") as outfile: 
    outfile.write(json_object) 

# Exportamos los datos a MongoDb
!mongoimport --db=datamad0320 --collection=Project_Api --jsonArray --drop sample.json