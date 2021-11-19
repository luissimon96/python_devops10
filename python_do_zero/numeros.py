print(4)
print(type(4))


print('-----------------')

print(14.70)
print(type(14.70))

print('=======================================')
print('Numeros apartir das funcoes int e float')
print('=======================================', end='\n\n')

preco_ingredientes = 14.70
print('Preco do Ingreditente Float: ',
      preco_ingredientes, type(preco_ingredientes))

print('Preco do Ingreditente int: ',
      int(preco_ingredientes), type(int(preco_ingredientes)))

print('')  # Criando minha variável de Estoque Total
total_estoque = 54
print('Estoque int: ', total_estoque, type(total_estoque))
print('Estoque float: ', float(total_estoque), type(float(total_estoque)))

print('')  # Criando minha variável de Faturamento Total
faturamento = '10_000'
print('Faturamento String', faturamento, type(
    faturamento))  # Convertendo int para String
print('Faturamento int', int(faturamento), type(
    int(faturamento)))  # Convertendo de String para Int
print('Faturamento Float', float(faturamento), type(
    float(faturamento)))  # Convertendo de Int para Float

# Fluxo de conversao String para Float e depois de Float para Int, caso contrario vai gerar erro.
print('')
imposto = '29.50'
print('Imposto Sting: ', imposto, type(imposto))
print('Imposto Int: ', int(float(imposto)), type(int(float(imposto))))
