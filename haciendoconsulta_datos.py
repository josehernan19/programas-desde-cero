import pymysql
conectados=pymysql.connect(
    host="localhost",
    user="root",
    passwd="Amoeloboe123",
    database="usuarios"
)
micursor=conectados.cursor()  
micursor.execute("SELECT email FROM datitos")
resultado=micursor.fetchall()
print(resultado)