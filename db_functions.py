import mysql.connector
import datetime

# Nombre base datos "3744065_logpersonal"
def fecha_hoy():
    hoy = datetime.datetime.now()
    año = hoy.year
    mes = hoy.month
    dia = hoy.day

    fecha = hoy.replace(año, mes, dia)
    fecha = hoy.strftime("%Y/%m/%d")
    print(fecha)
    return(fecha)

def send2db(valor):
  mydb = mysql.connector.connect(
    host="192.168.1.100",
    user='peterquinn',
    password="G0l0ndr1na",
    database="tests"
  )

  mycursor = mydb.cursor()

  sql = "INSERT INTO logdiario(fecha, nfollowers) VALUES(%s,%s)"
  val = (fecha_hoy(), valor)
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "Record insertado.")
  return()

fecha_hoy()