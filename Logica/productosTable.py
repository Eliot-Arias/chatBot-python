from ConexionDB.conexion import connectDB
from prettytable import PrettyTable


def tablaProd():
    
    mydb = connectDB()
    
    myCursor = mydb.cursor()
    myCursor.execute("SELECT * FROM vista_productos")
    
    resultados = myCursor.fetchall()
        
    tabla = PrettyTable()
    tabla.field_names = ["COD_Producto", "Descripción", "Unidad", "Precio"]

    for row in resultados:
        tabla.add_row(row)
    # print(tabla)
    print(tabla)

# tablaProd()



# import sys
# print(sys.path)