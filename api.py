from src.config import PORT
from src.app import app
import src.controllers.basedatos
from flask import request
import src.controllers.nuevoUsuarios
import src.controllers.params
import src.controllers.reportes
import src.controllers.analizadorSentimientos
import src.generandoElementos





app.run("0.0.0.0", PORT, debug=True)
