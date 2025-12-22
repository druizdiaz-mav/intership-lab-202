import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="clean_db",
        user="clean_user",
        password="clean_pass"
    )
