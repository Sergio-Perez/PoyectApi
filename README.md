# Proyect Api
## Descripción:
![Image APi](imagenes/Api.jpeg)



En este projecto tenemos que crear una API. Con módulo flask y con MongoDB creamos una base de datos de 
personas con sus frases, que poodemos actualizar, y analizamos los sentimientos de esas frases con el módulo nltk.

### Empiezo creando una  base de datos con un json.
   Saco los datos del archivo “quotes-100-en.json” y añado aleatoriamente los nombres y las frases.

### Creo la carpeta SRC
  En la carpeta src creo varios archivos en los cuales reparto las funciones de mi API. Dentro de esta carpeta genero dos carpetas:

      - Helpers --> Controla los errores de la API.      
      - Controllers --> Genera los controles de la API.
  

#### Controllers:
      - Dentro de la carpeta encontamos varios ficheros:
          - Analizador de sentimientos: 
              - Se encuentra el código donde analizamos los sentimientos de las frases:
                  - /Analizar/<name>/lista   --> Analiza todas las frases de un usuario.
                  - /Analizar/<name>/comunes --> Analizamos y decimos a qué otros usuarios somos más afines.
                  - /Analizar/<chat>         --> Analiza todas las frases de un chat.
                    
          - Base de datos:
             Muestreo de la base de datos:
                 - /chat/<name> --> Creamos una ruta en la API para buscar por chat.
                 - /<name>      --> Creamos una ruta en la API para buscar por nombre.
                    
          - Nuevo Usuarios:
              - Añadimos usuarios, chats y sus frases:
                  - /create --> Desde esta url podemos crear el usuario, su chat y su frase con parametros.
                   ejemplo:"http://localhost:xxxx/create?name=Sergio&chat=Ironhack&frase=I%20love%20my%20live"
                  - /create/chat/<chat>           --> Creamos un chat.                  
                  - /chat/<chat>/name/<name>      --> Creamos un usuario y un chat. 
                  - /anadir/<chat>/<name_id>      --> Añadimos al usuario en un chat.
                  - /anadir/<chat>/<name>/<frase> --> Añadimos una frase a un usuario.
        
          - Parms:
              - Aquí genero una función para poder añadir parametros.
          
          - Reportes:
              - /chat/<chat>/lista --> Devolvemos todos los mensajes de un chat.
              
          - Config:
              - La configuración de mi base de datos y mi conexión.
              
                     
#### El resto de los archivos ponen en marcha la API y el servidor.
