import configuration
import requests
import data

################################################### GET ##################################################
#################### DEVOLVER DOCUMENTACIÓN ####################
def get_docs():#define una función llamada get_docs. Cuando se llama a esta
    # función, realiza una solicitud GET a la combinación de URL_SERVICE y DOC_PATH
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

##response = get_docs()##esta línea llama a la función get_docs() y almacena la respuesta en la variable de respuesta
#muestra el código de estado de la respuesta HTTP. Por ejemplo,
#si todo va bien, debe mostrarse 200, que es el código de estado de OK.
##print(response.status_code)

#################### LOG_MAIN_PATH ####################
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)

#response = get_docs()
#print(response.status_code) #se imprime el código
#print(response.headers) #Se imprimen los encabezados

#################### OBTENER INFO DE BASE DE DATOS ####################
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

#response = get_users_table()
#print(response.status_code)

################################################### POST ##################################################

#################### CREAR USUARIO ####################
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

#response = post_new_user(data.user_body)
#print(response.status_code)
#print(response.json())

#################### buscar los kits por sus productos ####################
def post_products_kits(products_ids):
    # Realiza una solicitud POST para buscar kits por productos.
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, # Concatenación de URL base y ruta.
                         json=products_ids, # Datos a enviar en la solicitud.
                         headers=data.headers) # Encabezados de solicitud.

#response = post_products_kits(data.product_ids);
#print(response.status_code)
#print(response.json()) # Muestra del resultado en la consola