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

# print(nome_estabelecimento)

'''
Antes
print(pastel1, valor_pastel1, status)
print(pastel2, valor_pastel2, status)
print(pastel3, valor_pastel3, status)
print(pastel4, valor_pastel4, status)
'''
print('')
print('Concatenação')
mensagem = 'O nome do estabelecimento é: ' + nome_estabelecimento
print(mensagem)
mensagem2 = 'O pastel de ' + pastel1 + ' custa R$: ' + str(valor_pastel1)
print(mensagem2)

print('')
# este metodo ainda é utilizado mas ficou defasado e o que mais estão utilizando é o format
print('Interpolação')
# somente retorna o String de forma reduzido assim fica mais limpo o código
print('O nome do estabelecimento é: %s' % nome_estabelecimento)
# retorna várias casas decimais no Float e muitas vezes isso não pode acontecer se tratando de valores e numeros
print('O pastel de %s custa R$: %f' % (pastel1, valor_pastel1))
# definindo apenas 2 casas decimais para o Float
print('O pastel de %s custa R$: %.2f' % (pastel1, valor_pastel1))
# Desta forma só irá retornar valores inteiros sem as casas decimais
print('O pastel de %s custa R$: %d' % (pastel3, valor_pastel3))
# Desta forma só irá retornar valores inteiros sem as casas decimais
print('O pastel de %s custa R$: %d' % (pastel1, valor_pastel1))
# Desta forma ele completará 3 digitos incluindo 0 a Esquerda até completar
print('O pastel de %s custa R$: %.3d' % (pastel3, valor_pastel3))

print('')
print('Metodo Format')
print('O nome do estabelecimento é: {}'.format(nome_estabelecimento))
print('O valor de {} custa R$: {}'.format(pastel1, valor_pastel1))
print('O valor de {} custa R$: {:f}'.format(
    pastel1, valor_pastel1))  # Convertendo para Float
# Convertendo para Float e setando somente 2 casas decimais
print('O valor de {} custa R$: {:.2f}'.format(pastel1, valor_pastel1))
# Desta forma só irá retornar valores inteiros sem as casas decimais
print('O pastel de {} custa R$: {}'.format(pastel3, valor_pastel3))
# Desta forma só irá retornar valores inteiros sem as casas decimais
print('O pastel de {} custa R$: {}'.format(pastel1, valor_pastel1))
# Desta forma ele completará 3 digitos incluindo 0 a Esquerda até completar
print('O pastel de {} custa R$: {:03}'.format(pastel3, valor_pastel3))

print('')
print('Metodo f-string')  # mais utilizado atualmente
print(f'O nome do estabelecimento é: {nome_estabelecimento}')
print(f'O valor de {pastel1} custa R$: {valor_pastel1}')
# Convertendo para Float
print(f'O valor de {pastel1} custa R$: {valor_pastel1:f}')
# Convertendo para Float e setando somente 2 casas decimais
print(f'O valor de {pastel1} custa R$: {valor_pastel1:.2f}')
# Desta forma só irá retornar valores inteiros sem as casas decimais
print(f'O pastel de {pastel3} custa R$: {valor_pastel3}')
# Desta forma só irá retornar valores inteiros sem as casas decimais
print(f'O pastel de {pastel1} custa R$: {valor_pastel1}')
# Desta forma ele completará 3 digitos incluindo 0 a Esquerda até completar
print(f'O pastel de {pastel3} custa R$: {valor_pastel3:03}')
