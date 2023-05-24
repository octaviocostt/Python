def encontra_impares(list: list) -> list:
    odd = []

    if len(list) > 0:
        if list[0] % 2 > 0:
            odd.append(list[0])

        odd.extend(encontra_impares(list[1:]))

    return odd
