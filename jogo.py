import random

#variáveis globais
secretNumber = random.randint(1, 100) #O número secreto varia entre 1 e 100

def abertura():
    print('============================================')
    print('             HOUSE OF GENIUS                ')
    print('                by MD                       ')
    print('============================================')


def nivel():

    print('[1] Fácil')
    print('[2] Médio')
    print('[3] Difícil')
    escolhaNivel = int(input('Escolha o nível de dificuldade: '))

    dificuldade = 0

    if escolhaNivel == 1:
        dificuldade = 15 # 15 tentativas no nivel fácil
    elif escolhaNivel == 2:
        dificuldade = 10 # 10 tentativas no nível médio
    elif escolhaNivel == 3:
        dificuldade = 5 # 5 tentativas no nível difícil

    return dificuldade


def jogo():

    numeroTentativas = nivel()

    while numeroTentativas > 0:

        tentativa = int(input("Digite um número entre 1 a 100: "))

        if tentativa == secretNumber:
            print('\nParabéns, voce acertou!')
            break
        else: 
            if tentativa > secretNumber:
                print('Seu chute foi maior que o número secreto\n')
            else:
                print('Seu chute foi menor que o número secreto\n')

        numeroTentativas -= 1


if __name__ == '__main__':
    
    abertura()
    jogo()
