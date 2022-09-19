#  Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
nome = str(input('Digite o nome de uma cidade: ')).strip()

x = nome.split()
J = ' '.join(x)
M = (x[0].upper())
print('verificando se a cidade {} começa com SANTO em seu nome...'.format(J.title()))
print('Resultado: {}'.format('SANTO'in M))


