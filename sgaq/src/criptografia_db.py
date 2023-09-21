import json
from cryptography.fernet import Fernet
import os 

key = Fernet.generate_key()

cipher_suite = Fernet(key)

mysql_host = "127.0.0.6"
mysql_user = "adm"
mysql_password = "12345"
mysql_database = "db_sgaq"

connection_info= {
    "mysql_host": mysql_host,
    "mysql_user": mysql_user,
    "mysql_password": mysql_password,
    "mysql_database": mysql_database,
}

connection_info_json = json.dumps(connection_info)

encrypted_connection_info = cipher_suite.encrypt(connection_info_json.encode())

current_directory = os.path.dirname(os.path.abspath(__file__))

output_path = os.path.join(current_directory, "connection_info.encrypted")


with open(output_path, "wb") as file:
    file.write(encrypted_connection_info)

print(f"Chave de Uso no Sistema: {key}\n")