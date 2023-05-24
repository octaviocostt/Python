numero = -1
lista = []
while numero != 0:
    numero = int(input('Digite um número:'))
    if numero != 0:
        #lista.append(numero)
        lista.insert(0,numero)

for i in lista:
    print(i)
	
