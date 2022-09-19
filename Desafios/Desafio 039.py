ano = int(input('Insira o ano de nascimento: '))

idade = 2022 - ano

if idade < 18:
    print('Ainda vai de alistar')
elif idade > 18:
    print('Passou do tempo do alistameto')
else:
    print('Hora de se alistar!')
