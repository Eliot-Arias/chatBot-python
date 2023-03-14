from ConexionDB.conexion import connectDB


def autenticar_usuario(nom_user, password):

    mydb = connectDB()

    myCursor = mydb.cursor()
    query = "SELECT * FROM usuarios WHERE nom_user = %s AND password = %s"
    values = (nom_user, password)
    myCursor.execute(query, values)
    
    resultados = myCursor.fetchone()
    return resultados is not None


def registrar_usuario(nombre, apellidos, nom_user, password, correo, numero, dni):
    mydb = connectDB()
    
    myCursor = mydb.cursor()
    query = "INSERT INTO`usuarios` (`nombre`, `apellidos`,`nom_user`,`password`,`correo`,`numero`,`dni`)VALUES (%s, %s, %s, %s, %s, %s, %s);"
    values = (nombre, apellidos, nom_user, password, correo, numero, dni)
    myCursor.execute(query, values)
    return "Registro exitoso"
    

def revisarDatosRepetidos(nom_user, correo, dni):
    mydb = connectDB()

    myCursor = mydb.cursor()
    
    myCursor.execute("SELECT * FROM usuarios WHERE username = %s", (nom_user,))
    resultado = myCursor.fetchone()
    
    if resultado:
        return True
    else:
        return False
    
    
