print("Seja bem vindo a pastelaria DevOps")
print('Faça seu pedido')
# Solicitando para que o usuário digite a sua entrada
# Neste exemplo a entrada sempre vai ser String
# Caso precisarmos de outro tido de dados precisamos tratar isso
item_pedido = input('Qual o sabor do pastel que você deseja? ')
# imprimindo o que foi digitado e qual o valor digitado e o tipo de dado
print(f'O pastel pedido foi: {item_pedido} - {type(item_pedido)}')
# solicitando para que o usuário digite quanto ele quer de troco sem realizar operações aritmeticas
troco = float(input('O valor do pedido é de R$ 6.00, digite o troco: '))
print(f'O tipo de dado armazenado em troco é: {type(troco)}')
