12
def abertura():
    print('============================================')
    print('             HOUSE OF GENIUS                ')
    print('                by MD                       ')
    print('============================================')


#main

def jogo():
    abertura()

    secretNumber = 12

    tentativa = int(input("Digite um número entre 1 a 100: "))

    if tentativa == secretNumber: 
        print('Parabéns, voce acertou!')
    else: 
        print('Você errou, tente novamente!')

    continua = input('Deseja continuar? [S/N]: ') 


if __name__ == '__main__':
    
    jogo()

