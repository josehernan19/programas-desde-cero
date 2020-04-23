print('Bienvenido a Don Blanco!')
print('cuentas con un descuento del 60% al no comprar en  el dia')
panes=int(input('cuantos panes llevara? '))
precio_original= 3.49
descuento= 60
operacion_descuento= descuento / 100
precio_con_descuento= precio_original * panes * operacion_descuento 
print('el precio sin descuento es ', precio_original, 'cuenta con un descuento', descuento, 'el total a pagar es ', precio_con_descuento)
