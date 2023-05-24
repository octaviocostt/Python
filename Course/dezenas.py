numero = int(input("Digite um número inteiro: "))
unidade = numero%10
temp = (numero - unidade)/10
dezena = int(temp%10)
print("O dígito das dezenas é",dezena)
