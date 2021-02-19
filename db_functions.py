import mysql.connector

# Nombre base datos "3744065_logpersonal"

def send2db(sql):
  mydb = mysql.connector.connect(
    host="192.168.1.100",
    user='peterquinn',
    password="G0l0ndr1na",
    database="tests"
  )

  mycursor = mydb.cursor()


  val = ("2021/02/19", 67.5)
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "Record insertado.")
return()