horario = input('Digite o horário: ')

try:
    horario_int = int(horario)

    bom_dia = horario_int >= 0 and horario_int < 12
    boa_tarde = horario_int >= 12 and horario_int < 18
    #boa_noite = horario_int >= 18 and horario_int < 24

    if bom_dia:
        print('Bom dia!')
    elif boa_tarde:
        print('Boa tarde!')
    else: 
        print('Boa noite!')

except:
    print('Você não digitou um número')
