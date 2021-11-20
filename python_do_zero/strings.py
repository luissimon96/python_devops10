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
print('Nova varável contendo o resultado adultedado com base em uma variável já existente: ', novo_sabor)
print('Valor da variável sem mutação Pastel5: ', pastel5)
