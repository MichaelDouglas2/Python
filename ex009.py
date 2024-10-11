### calculadora while

while True:

    print(" -----  CALCULADORA ----- ")

    #tratando a entrada
    try:
        n1 = input("Digite o primeiro número: ")
        primeiro_numero = float(n1)

        n2 = input("Digite o segundo número: ")
        segundo_numero = float(n2)
    except:
        print('Você não digitou um número')
        continue

    escolha = input('Escolha a operação: \n[1] adição\n[2] subtração\n[3] multiplicação\n[4] divisão\n Escolha: ')
    
    try: 
        operacao = int(escolha)
    except:
        print('Você não escolheu um operador')
        continue

    if operacao == 1:
        print(f'a soma entre {primeiro_numero} e {segundo_numero} é {primeiro_numero + segundo_numero}')
    
    elif operacao == 2:
        print(f'a subtração entre {primeiro_numero} e {segundo_numero} é {primeiro_numero - segundo_numero}')
    
    elif operacao == 3:
        print(f'a multiplicação entre {primeiro_numero} e {segundo_numero} é {primeiro_numero * segundo_numero}')
    
    elif operacao == 4:
    
        try:
            print(f'a divisão entre {primeiro_numero} e {segundo_numero} é {primeiro_numero / segundo_numero}')
        except ZeroDivisionError:
            print("Divisao por zero nao existe")
            continue
    else: 
        print('Operação inválida...')
        continue

    sair = input('Deseja sair? [s/n]: ')

    if sair in 'Ss':
        break
    elif sair in 'Nn':
       continue
    else:
        print('Opção invalida')
        continue
   
