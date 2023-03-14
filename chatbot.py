import nltk
import numpy as np
import random
import string # to process standard python strings
import difflib

# importamos una funcion personalizada
from Logica.productosTable import tablaProd
from Logica.autenticarUsuario import autenticar_usuario, registrar_usuario, revisarDatosRepetidos



f=open('chatbot.txt','r',errors = 'ignorar')
raw=f.read()
raw=raw.lower()# converts to lowercase
# nltk.download('punkt') # first-time use only
# nltk.download('wordnet') # first-time use only
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words

lemmer = nltk.stem.WordNetLemmatizer()
#WordNet is a semantically-oriented dictionary of English included in NLTK.
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

GREETING_INPUTS = ("Hola", "hey", "saludos", "que hay..?", "que tal","chil",)
GREETING_RESPONSES = ["hola", "que tal", "*nods*", "como estas", "wow", "me alegra que estes hablando conmigo"]
def greeting(sentence):
    
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):        
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response if robo_response == '' else "ROBO: " + robo_response



sesion_iniciada = False

def iniciarSesion():
    nom_user = input("ROBO: Ingresa tu nombre de usuario: ")
    password = input("ROBO: Ingresa tu contraseña: ")
    
    #verificando los datos
    resultado = autenticar_usuario(nom_user, password)
    if resultado:
        print("ROBO: Sesion iniciada, Bienvenido!! ")
        sesion_iniciada = True
    else:
        print("ROBO: nombre de usuario o contraseña incorrectas")
        iniciarSesion()
        
def registro():
    nombre = input("ROBO: Ingresa tu nombre: ")
    apellidos = input("ROBO: Ingresa tu apellidos: ")
    nom_user = input("ROBO: Ingresa tu nombre de usuario: ")
    password = input("ROBO: Ingresa tu contraseña: ")
    correo = input("ROBO: Ingresa tu correo: ")
    numero = input("ROBO: Ingresa tu numero: ")
    dni = input("ROBO: Ingresa tu dni: ")
    
    resultado = registrar_usuario(nombre, apellidos, nom_user, password, correo, numero, dni)
    
    if resultado():
        print("ROBO: Lo siento ya existe un usuario con estas credenaiales")


with open('posibles_peticiones.txt', 'r') as file:
    posibles_peticiones = file.readlines()
    posibles_peticiones = [respuesta.strip() for respuesta in posibles_peticiones]

def buscarRespuestaParecida(user_response, posibles_peticiones):
    respuesta_parecida = difflib.get_close_matches(user_response, posibles_peticiones, n = 1, cutoff = 0.6)
    if respuesta_parecida:
        return respuesta_parecida[0]
    else:
        return None



flag = True
print("ROBO: My nombre es ROBO, te ayudare en lo que pueda, si deseas salir escribe 'Bye'")
user_name = input("ROBO: Por favor, dime tu nombre: ")
print("ROBO: Hola " + user_name + ", Deberas de iniciar sesion o registrarte para continuar hablando")
print("ROBO: Porfavor dime si deseas iniciar sesion o registrarte")
while (flag == True):
    user_response = input("You: ")
    user_response = user_response.lower()
    
    if (user_response != 'bye'):
        if (user_response == 'quiero iniciar sesion'):
            print("ROBO: eljiste iniciar sesion")
            iniciarSesion()
            continue
        elif(user_response == "quiero registrarme"):
            print("ROBO: Elejiste registrarte")
            
        else: 
            print("ROBO: lo siento no entendi quieres intentar de nuevo?")
        
        if (user_response == 'Gracias' or user_response == 'muchas gracias'):
            flag = False
            print("ROBO: No hay porque, estoy para servirte")
        else:
            if (greeting(user_response) != None):
                print("ROBO: " + greeting(user_response))
            else:
                # print("ROBO: ", end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
        if (user_response in posibles_peticiones):
            print("ROBO: esta es la tabla con los productos disponibles: ")
            tablaProd()
            continue
        elif user_response not in posibles_peticiones:
            respuesta_parecida = buscarRespuestaParecida(user_response, posibles_peticiones)
        if respuesta_parecida:
            print(f"ROBO: lo siento no entendi tu respuesta")
            continue
        else:
            print("ROBO: Lo siento, no entendí tu respuesta.")
    else:
        flag = False
        print(f"ROBO: Adios cuidate {user_name}")
