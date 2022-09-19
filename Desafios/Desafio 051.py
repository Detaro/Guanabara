print("PROGRESSÃO ARITIMÉTICA")
pt = int(input('Insira o valor do primeiro termo: '))
rz = int(input('Insira o valor da razão: '))
dec = pt + (10 - 1) * rz

for c in range(pt, dec + rz, rz):
    print(c, end=' |')
