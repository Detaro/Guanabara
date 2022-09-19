lista = []

for n in range(1, 6):
    lista.append(int(input('Insira um valor: ')))

lista.sort()

for i, n in enumerate(lista):
    if n == i + 1:
        lista.pop(n)


print(lista)

