import os
import psycopg2
from dotenv import load_dotenv

# Cargamos las variables del archivo .env al entorno de Python
load_dotenv()

def get_db_connection():
    try:
        # Intentamos conectar usando las credenciales del .env
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        return conn
    except Exception as e:
        print(f"Error al conectar la base de datos: {e}")
        raise e