num = input("Digite um número inteiro:")
tamanho = len(num)
numadj = False
aux1=0
aux2=0

while not numadj:
  aux1 = int(num) // (10**(tamanho-1))
  num = int(num) % (10**(tamanho-1))
  tamanho=tamanho-1
  aux2 = num // (10**(tamanho-1))
  if aux1 == aux2 and tamanho > 0:
    numadj=True  
    print("sim")
  elif tamanho==0:
    numadj=True
    print("não")
