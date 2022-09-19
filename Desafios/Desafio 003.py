print('=============== DESAFIO 03=============== ')
valor1 = input('DIGITE UM VALOR:')
valor2 = input('DIGITE UM VALOR A SER ADICIONADO:')
soma = int(valor1) + int(valor2)
print('A soma entre', valor1, 'e', valor2, 'vale', soma)

#OU

valor1 = int(input('DIGITE UM VALOR:'))
valor2 = int(input('DIGITE UM VALOR A SER ADICIONADO:'))
soma = valor1 + valor2
print('A soma entre {} e {} vale {}'.format(valor1,valor2,soma))
#OU
print('A soma entre {0} e {1} vale {2}'.format(valor1,valor2,soma))
soma = float(valor1) + float(valor2)
print('A soma entre {0} e {1} vale {2}'.format(valor1,valor2,soma))