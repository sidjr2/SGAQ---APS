from cryptography.fernet import Fernet
import json
import os 
import mysql.connector

current_directory = os.path.dirname(os.path.abspath(__file__))

output_path = os.path.join(current_directory, "connection_info.encrypted")

key = b'-cshsYRNUTkvIrhYynSwL53GL86nh6gAQBPPMzE6G-Y='

cipher_suite = Fernet(key)
try: 

    with open(output_path, "rb") as file:
        encrypted_connection_info = file.read()

    decrypted_connection_info_json = cipher_suite.decrypt(encrypted_connection_info)

    connection_info = json.loads(decrypted_connection_info_json)

    mysql_host = connection_info["mysql_host"]
    mysql_user = connection_info["mysql_user"]
    mysql_password = connection_info["mysql_password"]
    mysql_database = connection_info["mysql_database"]

    connection = mysql.connector.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        database=mysql_database
    )

    if connection.is_connected():
        print("Conexão com o MySQL estabelecida com sucesso!")

        #chama a main do sistema 

except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

finally:
    if 'connection' in locals():
        connection.close()