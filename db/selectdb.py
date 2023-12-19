import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="DarknessKD1.",
  database="pytest"
)

mycursor = mydb.cursor()
for i in ['quadras', 'usuarios']:
  mycursor.execute(f"SELECT * FROM {i}")
  print(f"-- {i} -- \n")
  myresult = mycursor.fetchall()
  for x in myresult:
      print(x)