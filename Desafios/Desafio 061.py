print("PROGRESSÃO ARITIMÉTICA")
pt = int(input('Insira o valor do primeiro termo: '))
rz = int(input('Insira o valor da razão: '))
termo = pt
c = 1

while c <= 10:
    print(f'| {termo}', end='')
    termo += rz
    c += 1
