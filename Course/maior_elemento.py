def maior_elemento(lista):
    maior = lista[0]
    for i in lista:
        for j in lista:
            if i < j:
                maior = j
    return maior
	
