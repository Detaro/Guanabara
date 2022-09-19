ano = int(input('insira o ano de nascimento do nadador: '))

i = 2022 - ano

if i <= 9:
    print('CATEGORIA: MIRIM')
elif i >= 10 and i <= 14:
    print('CATEGORIA: Infantil')
elif i >= 15 and i <= 19:
    print('CATEGORIA: JUNIOR')
elif i >= 20 and i < 21:
    print('CATEGORIA: SÊNIOR')
elif i > 21:
    print('CATEGORIA: MASTER')

