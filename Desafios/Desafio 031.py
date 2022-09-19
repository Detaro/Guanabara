km = float(input('Insira a quantidade de Km: '))

if km <= 200:
    print(f'Valor da passagem : R$:{km * 0.5 :.2f}')
elif km > 200:
    print(f'Valor da passagem : R$:{km * 0.45 :.2f}')