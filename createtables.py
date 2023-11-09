import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="DarknessKD1.",
  database="pytest"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE quadras (quadraid INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(255), local VARCHAR(255), capacidade INT, horario_disponivel VARCHAR(255), horario_limpeza VARCHAR(255))")
mycursor.execute("CREATE TABLE usuarios (nome VARCHAR(255), tipo VARCHAR(255), matricula INT PRIMARY KEY, email VARCHAR(255), cargo VARCHAR (255),telefone INT,data_nascimento VARCHAR(255),cidade VARCHAR(255),departamento VARCHAR(255), senha VARCHAR(255), punicao INT)")
mycursor.execute("CREATE TABLE reservas (reservaid INT AUTO_INCREMENT PRIMARY KEY, usuarioid INT,quadraid INT,hora TIME,data DATE,FOREIGN KEY (usuarioid) REFERENCES usuarios(matricula),FOREIGN KEY (quadraid) REFERENCES quadras(quadraid))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)