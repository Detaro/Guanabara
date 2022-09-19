lista = []

for n in range(1, 6):
    lista.append(int(input('Insira um valor: ')))

print(lista)

print(f'O maior valor foi: {max(lista)} e seu indice foi: ', end='')

for v, i in enumerate(lista):
    if i == max(lista):
        print(f'{v}...', end='')

print(f'\nO menor valor foi: {min(lista)} e seu indice foi: ', end='')

for v, i in enumerate(lista):
    if i == min(lista):
        print(f'{v}...', end='')
