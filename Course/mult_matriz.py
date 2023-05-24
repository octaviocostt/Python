def dimensoes(matriz):
    return (len(matriz), len(matriz[0]))
def sao_multiplicaveis(matriz1, matriz2):
    dimensaoMatriz1 = dimensoes(matriz1)
    dimensaoMatriz2 = dimensoes(matriz2)

    return True if dimensaoMatriz1[1] == dimensaoMatriz2[0] else False
