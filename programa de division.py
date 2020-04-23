print('bienvenidos a este programa, te diremos cual es el resto y cociente de tu division')
n=int(input('por favor introduzca un numero '))
m=int(input('por favor introduzca otro '))
while m == 0:
    m=int(input('no puedes dividir un numero entre cero '))
cociente= n / m 
resto= n % m 
print('este es tu cociente ', cociente, 'y este es tu resto ', resto)