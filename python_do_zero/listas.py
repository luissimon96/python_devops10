
# variaveis isoladas, cada pastel possue o seu sabor.
pastel1 = 'Carne'
pastel2 = 'Queijo'
pastel3 = 'Frango'
pastel4 = 'Calabresa'

# lista onde posso agrupar uma sequencia de dados e quando eu imprimir o valor me retornara o conteudo
cardapio = ['Carne', 'Queijo', 'Frango', 'Calabresa']

print(cardapio)  # imprime o conteudo da lista, o que existe armazenado nela.

# imprime o tamanho da lista iniciando em 1234 pois e a quantidade de elementos e nao a posicao da ordenacao
print(f'Tamanho da lista {len(cardapio)}')
print(f'Acessando o primeiro indice da lista: {cardapio[0]}')
# para acessar o penultimo [-2] e assim por diante
print(f'Acessando o ultimo indice da lista: {cardapio[-1]}')

# Alterando um valor da lista Queijo para Mussarela
cardapio[1] = 'Mussarela'
print(cardapio)

print('----------------')
print('')

novo_cardapio = []  # criando uma lista vazia
print(len(novo_cardapio))
print(type(novo_cardapio))


print('----------------')
print('')
print('Adicionando um novo elemento na lista')
novo_cardapio.append('Carne')
novo_cardapio.append('Queijo')
novo_cardapio.append('Frango')
novo_cardapio.append('Calabresa')
print(novo_cardapio)

print('----------------')
print('')
print('Acessando trechos da lista')
print(novo_cardapio[1:3])  # acessando o segundo ate o quarto elemento
# comeca a listagem apos o segundo elemento ate o final
print(novo_cardapio[2:])
print(novo_cardapio[:3])  # mostra 3 elementos do final para o comeco

print('----------------')
print('')
print('Organizando uma lista em ordem  alfabetica')
print(sorted(novo_cardapio, key=str.lower))

print('----------------')
print('')
print('Removendo um valor exato da lista')
novo_cardapio.remove('Calabresa')
print(novo_cardapio)

print('----------------')
print('')
novo_cardapio.append('Frango')
novo_cardapio.append('Frango')
print(novo_cardapio)

print(f'Quantos elementos especifico a lista possui',
      novo_cardapio.count('Frango'))

print('----------------')
print('')
print('Adicionando um valor a lista')
# Adiciona no inicio da lista o valor Palmito
novo_cardapio.insert(0, 'Palmito')
# Adiciona no indice 2 o valor Pizza
novo_cardapio.insert(2, 'Pizza')
print(novo_cardapio)

print('----------------')
print('')
print('Removendo um indice da lista')
novo_cardapio.pop(4)
print(novo_cardapio)
print('')
print('Removendo o ultimo indice da lista pois o default é last')
novo_cardapio.pop()
print(novo_cardapio)

# remove os indices 4 em diante
del novo_cardapio[3:]
print(novo_cardapio)


print('----------------')
print('')
print('Trabalhando com valores dentro de uma lista')
vendas = []
# acrescentando valores na lista
vendas.append(12.00)
vendas.append(16.00)
vendas.append(24.00)
print(vendas)
# somando todos os valores da lista
print(sum(vendas))
# qual o maior valor da lista
print(max(vendas))
# menor valor da lista
print(min(vendas))
# media de vendas onde irei somar todos os valores dividindo pelo total de vendas realizadas
print(f'{sum(vendas)/len(vendas)}')
# limitando a saida em apenas 2 casas decimais
print(f'{sum(vendas)/len(vendas):.2f}')

print('----------------')
print('')
print('Trabalhando com lista onde irá criar um range de 1 a 100')
numeros = list(range(1, 101))
print(numeros)
print(len(numeros))
#
print('')
del numeros[:10]
print(f'Comeca do 11: {numeros}')
#
print('')
del numeros[:10]
print(f'Comeca do 21: {numeros}')
#
print('')
del numeros[:10]
print(f'Comeca do 31: {numeros}')
#
print('')
print(f'Me lista do indice 1 ao 10 na lista: {numeros[1:10]}')
