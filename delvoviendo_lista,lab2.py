print("BIENVENIDOS, TE DEVOLVEREMOS EN UNA LISTA LOS NUMEROS MULTIPLOS DE 3 Y 5 ")
a=int(input("introduce un numero "))
b= range(1,a)
c=[]
def devolviendo_lista(d):
    for i in b:
        if i % 3 == 0 and i % 5 == 0:
            c.append(i)
devolviendo_lista(a)
print(c)