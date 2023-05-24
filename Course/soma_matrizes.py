def soma_matrizes(m1, m2):
    if dimensoes(m1) == dimensoes(m2):
        matriz = []
        for t in range(len(m1)):
            linhanova = []
            for t1 in range(len(m1[0])):
                linhanova.append(m1[t][t1] + m2[t][t1])
            matriz.append(linhanova)
        return matriz
    else:
        return False


def dimensoes(matriz):
    col = len(matriz[0])
    lin = len(matriz)
    return lin, col
