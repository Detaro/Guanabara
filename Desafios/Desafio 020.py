from random import shuffle

v1 = str(input('Digite um nome:'))
v2 = str(input('Digite outro nome:'))
v3 = str(input('Digite outro nome:'))
v4 = str(input('Digite outro nome:'))

v5 = [v1, v2, v3, v4]
shuffle(v5)
print('A ordem de apresentação será {}'.format(v5))