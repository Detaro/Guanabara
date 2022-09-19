tupla = ('Produto 1', 2.00, 'Produto 2', 2.00, 'Produto 3', 2.00)

print('-' * 60)
print(f'{"LISTAGEM DE PREÇO":^60}')
print('-' * 60)


for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end=' ')
    else:
        print(f'R$:{tupla[pos]:>6.2f}')
