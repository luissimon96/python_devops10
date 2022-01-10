
print("Seja bem vindo a pastelaria DevOps")
print('Faça seu pedido')
'''
0 - Estabelecimento Fechado
1 - Estabelecimento Aberto
'''

'''
status = 1
while status == 1:
    item_pedido = input('Qual o sabor do pastel que você deseja? ')
    print(f'Pedido Confirmado)
    status = int(
        input('Digite 1 para aceitar novos pedidos e 0 para encerrar: '))
'''
contador = 0
quantidade_de_pedidos = 3
while contador < quantidade_de_pedidos:
    item_pedido = input('Qual o sabor do pastel que você deseja? ')
    print(f'Pedido Confirmado')
    contador += 1
