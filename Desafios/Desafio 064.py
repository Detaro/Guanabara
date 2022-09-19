flag = 0
soma = 0
contador = 0
while flag != 999:
    v1 = int(input("Insira um valor ou digite '999' para finalizar: "))
    soma += v1
    contador += 1
    if v1 == 999:
        break

print(f"Numeros digitados: {contador - 1}")
print(f"Soma dos valores: {soma - 999}")
