from random import choice

v1 = str(input('Digite um nome:'))
v2 = str(input('Digite outro nome:'))
v3 = str(input('Digite outro nome:'))
v4 = str(input('Digite outro nome:'))
v5 = choice([v1, v2, v3, v4])
print('O aluno escolhido foi {}'.format(v5))