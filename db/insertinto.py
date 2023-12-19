import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="DarknessKD1.",
  database="pytest"
)
mycursor = mydb.cursor()
sql = "INSERT INTO usuarios (nome, tipo, matricula, email, cargo, telefone, data_nascimento, cidade, departamento, senha, punicao,userid) VALUES (%s, %s,%s,%s,%s, %s,%s,%s,%s,%s,%s)"
val = ('Cardinal', 'Tom B. Erichsen', '123', 'Stavanger', '4006', 'Norway','020202','RJ','123','0')

mycursor.execute(sql, val)

mydb.commit()
