import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_DATABASE'),
}

db_clarke = mysql.connector.connect(**db_config)

if db_clarke.is_connected():
    print('Conectado ao banco de dados MySQL')
    
else:
    print('ERRO: Não foi possível conectar ao banco de dados MySQL')