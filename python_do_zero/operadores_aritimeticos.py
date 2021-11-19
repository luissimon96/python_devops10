nome_estabelecimento = 'Pastelaria DevOps'
pastel1 = 'Carne'
pastel2 = 'Queijo'
pastel3 = 'Frango'
pastel4 = 'Calabresa'
status = True
valor_pastel1 = 6.0
valor_pastel2 = 6.0
valor_pastel3 = 6
valor_pastel4 = 6
print(nome_estabelecimento)
print(pastel1, valor_pastel1, status)
print(pastel2, valor_pastel2, status)
print(pastel3, valor_pastel3, status)
print(pastel4, valor_pastel4, status)

print('------------------')
# SOMA
pedido1 = valor_pastel1 + valor_pastel2
print('Valor total pedido 1: ', pedido1, type(pedido1))

pedido2 = valor_pastel1 + valor_pastel3
print('O valor do pedido 2: ', pedido2, type(pedido2))

# SUBTRAÇÂO
custo = 5.0
subtracao1 = pedido1 - custo
print('Exemplo 1 subtração:', subtracao1, type(subtracao1))

# DIVISÂO
ticket_medio = (pedido1 + pedido2)/2
print('O ticket médio é: ', ticket_medio)

# MULTIPLICAÇÃO
dias_mes = 22
faturamento = ticket_medio * dias_mes
print('Previsão de faturamento: ', faturamento)
