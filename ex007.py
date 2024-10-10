nome = input('Digite seu nome: ')

numero_letras = len(nome)

if numero_letras > 1:
    
    if numero_letras < 5:
        print('Seu nome é curto')
    elif numero_letras < 7:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')

else:
    print('Digite mais de uma letra')
