import math
x1 = float(input("Digite um número X1: "))
y1 = float(input("Digite um número Y1: "))
x2 = float(input("Digite um número X2: "))
y2 = float(input("Digite um número Y2: "))

dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)

if dist >= 10:
	print("longe")
else:
	print("perto")
