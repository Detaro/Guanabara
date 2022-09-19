n = (int(input('Insira um valor: ')), int(input('Insira um valor: ')), int(input('Insira um valor: ')),
     int(input('Insira um valor: ')))
print(n)

a = (n.count(9))
print(f'O numero nove apareceu {a} veze(s)')

if 3 in n:
    b = n.index(3)
    print(f'O valor 3 foi digitado pela primeira vez na pos: {b + 1}')
else:
    print(f'O valor 3 não foi digitado')

print('Os Numeros pares foram:', end=' ')
for x in n:
    if x % 2 == 0:
         print(f'{x}', end=', ')


