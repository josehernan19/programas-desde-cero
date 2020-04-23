print('BIENVENIDO CALCULAREMOS TU INDICE DE MASA CORPORAL. POR FAVOR, LA PARTE DECIMAL INTRODUCELA CON PUNTO(.) Y NO CON COMA(,)')
altura=float(input("introduce tu altura "))
peso=float(input('introduce tu peso '))
denominador= altura ** 2
indice= peso / denominador
print('tu indice de masa corporal es ', '{0:.2f}'.format(indice))
