# Proyect Api
## Descripción:
![Image APi](imagenes/Api.jpeg)



En este projecto tenemos que crear una api,con módulo flask y con Mongodb crear una base de datos de 
personas con sus frases, y analizar los sentimientos de esas frases con módulo nltk.

### Empiezo creando una  base de datos con un json.
   Saco los datos del archivo “quotes-100-en.json” y lo añado aleatoriamente los nombres y las frases a las cuales les añado la hora de creación.

### Creo la carpeta SRC
  En la carpeta src creo varios archivos en los cuales reparto las funciones de mi api. Dentro dede esta carpeta genero dos carpetas helpers y controllers.
      - Helpers --> Controla los errores de la Api.
      - Controllers --> Genera los controles de la Api
  

#### Controllers:
      - Dentro de la carpeta encontamos varios ficheros:
          - Analizador de sentimientos : 
              - Se encuentra el codigo donde analizamos los sentimientos de las frases:
                  - /Analizar/<name>/lista   --> Analiza todas las frases de un usuario.
                  - /Analizar/<name>/comunes --> Analizamos y decimos a que otros usuarios somos más afines.
                  - /Analizar/<chat>         --> Analiza todas las frases de un chat.
                    
          - Base de datos:
             Muestreo de la base de datos.
                 - /chat/<name> --> Creamos una ruta en la Api para buscar por chats.
                 - /<name>      --> Creamos una ruta en la Api para buscar los nombres
                    
          - Nuevo Usuarios:
              - Añadimos usuarios, chats y sus frases.
                  - /create --> Desde esta url podemos crear el usuario, su chat y su frase con parametros.
                   ejemplo:"http://localhost:xxxx/create?name=Sergio&chat=Ironhack&frase=I%20love%20my%20live"
                  - /create/chat/<chat>           --> Creamos un chat.                  
                  - /chat/<chat>/name/<name>      --> Creamos un usario y un chat. 
                  - /anadir/<chat>/<name_id>      --> Añadimos al usuario en un chat.
                  - /anadir/<chat>/<name>/<frase> --> Añadimos una frase a un usuario.
        
          - Parms:
              - Aqui genero una función para poder añaaidr parametros.
          
          - Reportes:
              - /chat/<chat>/lista --> Devolvemos todos los mensajes de un chat.
              
          - Config:
              - La configuración de mi base de datos y mi conexión.
              
                     
#### El resto de los archivos ponen en marcha la Api y el servidor.
