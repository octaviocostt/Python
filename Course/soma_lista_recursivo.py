def soma_lista(list: list) -> int:

    if len(list) == 1:
        return list[0]

    return list[0] + soma_lista(list[1:])
