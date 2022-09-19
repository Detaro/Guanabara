n = 0
soma = 0
v1 = int(input("Insira um valor: "))
soma += v1
n += 1
maior = v1
menor = v1
r = input('Deseja Comtiuar (S/N): ').upper()

while r != 'N':
    v1 = int(input("Insira um valor: "))
    soma += v1
    n += 1
    if v1 > maior:
        maior = v1
    if v1 < menor:
        menor = v1
    r = input('Deseja Comtiuar (S/N): ').upper()

media = soma / n
print(f'Valor da média: {media}')
print(f'Maior numero lido: {maior}')
print(f'menor número lido: {menor}')


