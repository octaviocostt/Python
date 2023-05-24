def primo(x):
        i = 1
        while i != x:
                i = i + 2
                if i == x:
                        return True
                else:
                        if (x % i) == 0:
                                return False
                        else:
                               if (x % 2) == 0:
                                       return False




def maior_primo(x):
        aux = primo(x)
        if aux == True:
                return x
        else:
                while (aux == False):
                        x = x -1
                        if primo(x):
                                return x
                        


                
