a=input("por favor introduzca su nombre ")
b=input("introuduzca su apellido ")
c=input("instroduzca su email ")
d=input("introduzca su password ")
import pymysql
conectividad=pymysql.connect(
    host="localhost",
    user="root",
    passwd="Amoeloboe123",
    database="usuarios"
)
micursor=conectividad.cursor()
insertado="INSERT INTO datitos (nombre,apellido,email,passwd)values(%s,%s,%s,%s)"
micursor.execute(insertado,(a,b,c,d))
conectividad.commit()
micursor.close()
conectividad.close()

