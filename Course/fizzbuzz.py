num = int(input("Digite um numero inteiro: "))

resto2 = num % 5

resto1 = num % 3

if (resto1 == 0 and resto2 == 0):
	print("FizzBuzz")
else:
	print(num)
