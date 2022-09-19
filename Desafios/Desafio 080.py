numeros = list()
while True:
    n = (int(input('Insira um valor: ')))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado')
    else:
        print('Valor duplicado, não adicionado')

    numeros.sort()

    continuar = input('Deseja continuar? [S/N]').upper()[0].strip()
    if continuar == 'N':
        break
print(numeros)

