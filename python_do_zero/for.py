# trabalhando com Controle de Fluxo com FOR
# For é uma estrutura de repeticao em Python projetada para percorrer listas
# Para cada elemento na lista efetua uma acao.
print('----------------')
print('')
print('Trabalhando com cada indice separado')
cardapio = ['Carne', 'Queijo', 'Frango', 'Calabresa', 'Pizza', 'Carne Seca']
print(f'Valor do indice 1: {cardapio[0]}')
print(f'Valor do indice 2: {cardapio[1]}')
print(f'Valor do indice 3: {cardapio[2]}')

# Utilizando o For para percorrer a lista
print('#####################')
print('#-Pastelaria DevOps-#')
print('#####################')

for recheio in cardapio:
  print(f'O recheio do pastel e de: {recheio}')
