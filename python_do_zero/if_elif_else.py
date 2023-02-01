# Calculo do IMC

'''
O IMC e calculado dividindo o pose (em kg) pela altura ao quadrado (em metros)

- MENOR QUE 18.5 = MAGREZA;
- ENTRE 18.5 E 24.9 = NORMAL;
- ENTRE 25.0 E 29.9 = SOBREPESO;
- ENTRE 30.0 E 39.9 = OBESIDADE;
- MAIOR QUE 40.0 = OBESIDADE GRAVE
'''

print('******* Calculo IMC *******')

altura = float(input('Digite sua altura (Ex,: 1.72): '))
peso = float(input('Digite seu peso (Ex.: 72): '))
print('')

# IMC

imc = round(peso / (altura**2), 2)  # Função round() define as casas decimais.
# ** = operador de potencia


# Condição do IMC

#imc_status = ' '

if imc < 18.5:
    print(f'Seu IMC {imc}, seu peso esta categorizado como Magreza')

elif imc >= 18.5 and imc <= 24.9:
    print(f'Seu IMC {imc}, seu peso esta categorizado como Normal')

elif imc >= 25.0 and imc <= 29.9:
    print(f'Seu IMC {imc}, seu peso esta categorizado como Sobrepeso')

elif imc >= 30.0 and imc <= 39.9:
    print(f'Seu IMC {imc}, seu peso esta categorizado como Obesidade')

elif imc > 40:
    print(f'Seu IMC {imc}, seu peso esta categorizado como Obesidade Grave')

else:
    print('Padrão não definido')
