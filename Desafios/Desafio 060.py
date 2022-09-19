resultado = 1
c = 1
v1 = int(input('Insira um valor: '))

while c <= v1:
    resultado *= c
    c += 1
print(f'Fatorial de {v1}! é: {resultado}')



numero = int(input("Fatorial de: "))

resultado = 1
for n in range(1, numero + 1):
    resultado *= n

print(f'Fatorial de {numero}! é: {resultado}')
