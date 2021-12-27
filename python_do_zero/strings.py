nome_estabelecimento = 'Pastelaria DevOps'
pastel1 = 'Carne'
pastel2 = 'Queijo'
pastel3 = 'Frango'
pastel4 = 'Calabresa'
pastel5 = "Carne com queijo"
pastel6 = " Carne com frango "

print("----------------")
print("")
print('Substituindo Caracteres')
# trocando visualização da palavra queijo por frango, neste momento não altero nada na
print(pastel5.replace('queijo', 'frango'))
# variável, ela continua com o mesmo conteúdo
novo_sabor = pastel5.replace('queijo', 'frango')
print('Nova varável contendo o resultado adulterado com base em uma variável já existente: ', novo_sabor)
print('Valor da variável sem mutação Pastel5: ', pastel5)

print('')

# Deixando todo o texto em caixa alta e no segundo exemplo tudo em caixa baixa
# é usado muito em casos de V ou F e Y ou N, quando vamos validar se o usuário digitou alguma entrada de Y ou N.
print(pastel5.upper())
print(pastel5.lower())

print('')

# buscando se o conteúdo da variável inicia com de terminado conjunto de caracteres
print(pastel5.startswith('Queijo'))
print(pastel5.startswith('Carne'))
# buscando se o conteúdo da variável termina com de terminado conjunto de caracteres
print(pastel5.endswith('Frango'))
print(pastel5.endswith('queijo'))
# para facilitar em uma busca de palavras podemos unir os validadores de upper ou lower com esses startwith ou endwith

print('')

# Eliminando os espaços no conteúdo da string
print('Pastel 6: ', pastel6)
print('Pastel 6: ', pastel6.replace(' ', '-'))

# Elimina os caracteres do inicio e final da string
novo_pastel6 = pastel6.strip()
novo_pastel6 = novo_pastel6.replace(' ', '-')
print('Novo Pastel 6: ', novo_pastel6)

# Elimina os caracteres do inicio da string
novo_pastel6 = pastel6.lstrip()
novo_pastel6 = novo_pastel6.replace(' ', '-')
print('Novo Pastel 6: ', novo_pastel6)

# Elimina os caracteres do final da string
novo_pastel6 = pastel6.rstrip()
novo_pastel6 = novo_pastel6.replace(' ', '-')
print('Novo Pastel 6: ', novo_pastel6)

print('')

print('##### FUNÇÃO LEN #####')  # Conta quantos caracteres existe na string
print('Quatidade de caracteres no Pastel 5: ', len(pastel5))

print('')

print('##### Fatiamento #####')
print(pastel5[0])  # Busca no String o primeiro caracter e retorna.
print(pastel5[-1])  # Busca no String o ultimo caracter e retorna.
# Endereços em uma string de
# Frente para tras: 0  1   2   3   4
# Frente para tras: C  A   R   N   E
# Tras para frente:   -5    -4    -3    -2    -1
# Tras para frente:    E     N     R     A     C
# Busca partes dentro da string, muito usado em códigos de produtos ou usuários.
print(pastel5[0:3])
print(pastel5[0:5])
print(pastel5[2:])
print(pastel5[:2])

print('')

# Consultando se o conjunto de caracteres existe na string, retornando True ou False
print('##### Operadores IN e NOT IN #####')
result = 'Frango' in pastel5
print(result)

result = 'Frango' not in pastel5
print(result)
