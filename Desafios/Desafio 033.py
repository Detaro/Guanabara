# Faça um programa que receba 3 numeros e mostre qual é o maior

v1 = int(input('insira um número:'))
v2 = int(input('insira outro número: '))
v3 = int(input('insira outro número: '))
print(v1, v2, v3)

menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
print(f'O menor valor é: {menor}')

maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
print(f'O maior valor é: {maior}')