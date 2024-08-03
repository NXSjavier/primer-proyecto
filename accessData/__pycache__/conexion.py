#Aqui estamos importando una libreria de mysql 
import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    #Aqui estamos configurando la contracena y nombre que utilisaremos en el mysql el host y tambien como se va allamar nuestra base de datos
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='0000',
            database='planeta'  # Cambia esto al nombre de tu base de datos
        )
        print("Conexión exitosa a MySQL")
    except Error as e:
        print(f"Error '{e}' ocurrió al conectar a MySQL")

    return connection

# Usar la conexión
conn = create_connection()
