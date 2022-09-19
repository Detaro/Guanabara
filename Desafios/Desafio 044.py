valor = float(input('Insira o valor do Produto: '))

print('FORMA DE PAGAMENTO')
print('1 - A vista em dinheiro')
print('2 - A vista no cartão')
print('3 - A Prazo no cartão (2x)')
print('4 - A Prazo no cartão acima de 2x')

choice = int(input())

if choice == 1:
    print(f'Valor a ser pago: {valor - valor * 0.1:.2f}')
if choice == 2:
    print(f'Valor a ser pago: {valor - valor * 0.05:.2f}')
if choice == 3:
    print(f'Valor a ser pago: {valor:.2f}')
if choice == 4:
    print(f'Valor a ser pago: {valor + valor * 0.2:.2f}')


