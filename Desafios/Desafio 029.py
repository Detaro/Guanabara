v1 = int(input('Insira a velocidade do carro em KM/h: '))
limite =  v1 - 80
multa = limite * 7

if limite > 0:
    print(f'valor da multa R$:{multa}')
else:
    print('Sem multa a ser aplicada')

