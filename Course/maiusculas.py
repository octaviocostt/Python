def maiusculas(frase):
    maiusculas = []

    for i in range(len(frase)):
        caracter = frase[i]
        decASCII = ord(caracter)

        if decASCII > 64 and decASCII < 91:
            maiusculas.append(caracter)

    return "".join(maiusculas)

def test_unicoMaiusculo():
    assert maiusculas('Programamos em python 2?') == 'P'

def test_variosMaiusculos():
    assert maiusculas('PrOgRaMaMoS em python!') == 'PORMMS'
