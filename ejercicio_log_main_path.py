'''Agrega a la solicitud del log el parámetro
params={"count":20}, ejecuta el código y comprueba si el código de respuesta es diferente'''

import configuration
import requests

#################### DEVOLVER DOCUMENTACIÓN ####################
def get_docs():#define una función llamada get_docs. Cuando se llama a esta
    # función, realiza una solicitud GET a la combinación de URL_SERVICE y DOC_PATH
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

#################### LOG_MAIN_PATH ####################
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count": 20})


#################### DEVOLVER DOCUMENTACIÓN ####################
#response = get_docs()##esta línea llama a la función get_docs() y almacena la respuesta en la variable de respuesta
#muestra el código de estado de la respuesta HTTP. Por ejemplo,
#si todo va bien, debe mostrarse 200, que es el código de estado de "OK".
##print(response.status_code)

#################### LOG_MAIN_PATH ####################
response = get_docs()
print(response.status_code) #se imprime el código
print(response.headers) #Se imprimen los encabezados

