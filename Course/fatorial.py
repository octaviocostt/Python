num = int(input("Digite o valor de n: "))

i = 2
fatorial = 1
if num == 0:
	print(1)
else:
	while i <= num:
		fatorial = fatorial * i
		i = i+1
	print(fatorial)

        
