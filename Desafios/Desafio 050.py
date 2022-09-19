soma = 0
for c in range (1, 7):
    v1 = int(input("insira um valor inteiro: "))
    if v1 % 2 == 0:
        soma = v1 + soma
print(f'A soma dos numeros pares é: {soma}')


