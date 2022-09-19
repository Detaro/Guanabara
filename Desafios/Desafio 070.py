print('-' * 40)
print('             Desafio 70')
print('-' * 40)
res = None
produtos = []
preco = []


while res != 'N':
    produtos.append(input('Nome do produto: '))
    preco.append(float(input('Preço do produto: ')))
    res = input('Quer Continuar? [S/N]').upper().strip()[0]

v2 = 0
for c in preco:
    if c > 1000:
        v2 += 1

v1 = preco.index(min(preco))

print(f'O Total da compra foi {sum(preco):.2f}')
print(f'Temos {v2 } produto(s) custando mais de R$1000,00')
print(f'O Prodtuto mais barato foi: {produtos[v1]} que custa R${min(preco):.2f}')
