import mysql.connector

def connectDB():
    mydb = mysql.connector.connect(
        host = 'localhost',
        user='id20203615_fortalezawtf2',
        password='q~D3KT2CuOY4L@4_',
        database='id20203615_eliotdb'
    )    
    return mydb


# mydb = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = '',
#     database = 'ferreteriaApp'
# )
# myCursor = mydb.cursor()


# myCursor.execute("SELECT * FROM vista_productos")

# resultados = myCursor.fetchall()

# tabla = PrettyTable()

# tabla.field_names = ["COD_Producto", "Descripción", "Unidad", "Precio"]

# for row in resultados:
#     tabla.add_row(row)
# print(tabla)




#Prubasssss
# import mysql.connector

# def connectDB():
#     mydb = mysql.connector.connect(
#         host = 'localhost',
#         user = 'root',
#         password = '',
#         database = 'ferreteriaApp'
#     )

#     return mydb

# def tablaProd():
    
#     mydb = connectDB()
    
#     if mydb.is_connected():
#         myCursor = mydb.cursor()
#         myCursor.execute("SELECT * FROM vista_productos")
#         resultados = myCursor.fetchall()

#         for row in resultados:
#             print(row)

#         myCursor.close()
#         mydb.close()
#     else:
#         print("No se pudo establecer la conexión con la base de datos")

# tablaProd()
