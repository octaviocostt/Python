def busca(list: list, element):
    """Busca por um valor utilizando o algoritmo: Binário."""
    first = 0
    last = len(list) - 1

    while first <= last:
        middle = (first + last) // 2

        print(middle)

        if list[middle] == element:
            return middle
        else:
            if element < list[middle]:
                last = middle - 1
            else:
                first = middle + 1

    return False
