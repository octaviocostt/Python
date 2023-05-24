def main():
        aux = False
        while aux == False:
                print("Bem-vindo ao jogo do NIM! Escolha: ")
                x = int(input("1 - para jogar uma partida isolada " "\n2 - para jogar um campeonato "))
                if x == 1:
                        print("Voce escolheu uma partida isolada! \n")
                        aux = True
                else:
                        if x == 2:
                                print("Voce escolheu um campeonato! \n")
                                aux = True
                        else:
                                print("Opção inválida! \n")
                                aux = False

def partida():
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        if (n % (m+1)) == 0:
                print("\nVoce começa! \n")
                usuario_escolhe_jogada(n,m)
        else:
                print("\nComputador começa! \n")
                computador_escolhe_jogada(n,m)
                

def usuario_escolhe_jogada(n,m):
        aux = False
        while not(aux):
                x = int(input("Quantas peças você vai tirar? "))
                if x > m:
                        print("Oops! Jogada inválida! Tente de novo.")
                        aux = False
                else:
                        print("Voce tirou",x,"peças.")
                        y = n - x
                        n = y
                        print("Agora resta apenas",y,"peça no tabuleiro.\n")
                        if y <= m:
                                print("O computador tirou",y,"peça.")
                                print("Fim do jogo! O computador ganhou!")
                                aux = True
                        else:
                                z = y - m
                                n = z
                                print("O computador tirou",m,"peça.")
                                print("Agora resta apenas",z,"peça no tabuleiro.\n")
                                aux = False
        
        
def computador_escolhe_jogada(n,m):
        z = n - m
        if z == 0:
                print("O computador tirou",m,"peça.")
                print("Fim do jogo! O computador ganhou!")
        else:
                n = z
                print("O computador tirou",m,"peça.")
                print("Agora resta apenas",z,"peça no tabuleiro.\n")
                aux2 = False
                while not(aux2):
                        x = int(input("Quantas peças você vai tirar? "))
                        if x > m:
                                print("Oops! Jogada inválida! Tente de novo.\n")
                                aux2 = False
                        else:
                                print("Voce tirou",x,"peças.")
                                y = n - x
                                n = y
                                print("Agora resta apenas",y,"peça no tabuleiro.\n")
                                if y <= m:
                                        print("O computador tirou",y,"peça.")
                                        print("Fim do jogo! O computador ganhou!")
                                        aux2 = True
                                else:
                                        w = y - m
                                        n = w
                                        print("O computador tirou",m,"peça.")
                                        print("Agora resta apenas",w,"peça no tabuleiro.\n")
                                        aux2 = False
                                
                        
