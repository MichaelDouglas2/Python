numero = input('Digite um número inteiro: ')

try:
     #casting: str -> int
    numero_inteiro = int(numero)

    numero_par = (numero_inteiro % 2) == 0
    
    if numero_par:
        print(f'{numero_inteiro} é par')
    else:
        print(f'{numero_inteiro} é impar')

except:
    print('Não é um número inteiro')

