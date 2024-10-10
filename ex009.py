### calculadora while

while True:

    print(" -----  CALCULADORA ----- ")
    n1 = input("Digite o primeiro número: ")
    primeiro_numero = int(n1)

    n2 = input("Digite o segundo número: ")
    segundo_numero = int(n2)

    escolha = input('Escolha a operação: \n[1] adição\n[2] subtração\n[3] multiplicação\n[4] divisão\n Escolha: ')
    operacao = int(escolha)

    if operacao == 1:
        print(f' a soma entre {primeiro_numero} e {segundo_numero} é {primeiro_numero + segundo_numero}')
    elif operacao == 2:
        print(f' a subtração entre {primeiro_numero} e {segundo_numero} é {primeiro_numero - segundo_numero}')
    elif operacao == 3:
        print(f' a multiplicação entre {primeiro_numero} e {segundo_numero} é {primeiro_numero * segundo_numero}')
    elif operacao == 4:
        print(f' a divisão entre {primeiro_numero} e {segundo_numero} é {primeiro_numero / segundo_numero}')
    else: 
        print('Operação inválida...')
        continue

    sair = input('Deseja sair? [s/n]: ')

    if sair == 's':
        break
