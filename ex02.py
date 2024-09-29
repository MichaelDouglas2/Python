gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 400, 500, 700]

soma_joao = sum(gastos_joao)
soma_pedro = sum(gastos_pedro)

if soma_joao > soma_pedro:
    print('João gastou mais dinheiro esse mês')
elif soma_pedro > soma_joao:
    print('Pedro gastou mais dinheiro esse mês')
else:
    print('Os dois gastaram a mesma quantidade')