v1 = float(input('Insira o valor do salario: '))

if v1 > 1250:
    print(f'Salario aumentado para R$:{v1 + (v1 * 0.10):.2f}')

if v1 <= 1250:
    print(f'Salario aumentado para R$:{v1 + (v1 * 0.15):.2f}')
