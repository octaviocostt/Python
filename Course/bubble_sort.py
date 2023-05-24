def bubble_sort(list: list) -> list:
    """Ordena uma lista utilizando o algoritmo: Ordenação da Bolha."""
    list = list[:]

    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                print(list)

    return list
