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

print('Concatenação')
print('')
mensagem = 'O nome do estabelecimento é: ' + nome_estabelecimento
print(mensagem)

mensagem2 = 'O pastel ' + pastel1 + 'custa R$: ' + str(valor_pastel1)
