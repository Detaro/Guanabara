
maiorpeso = 0
menorpeso = 0

for c in range(1, 6):
    v1 = float(input(f"{c}- Insira o valor do peso: "))
    menorpeso = v1
    if v1 > maiorpeso:
        maiorpeso = v1
        v2 = c

    if v1 < menorpeso:
        menorpeso = v1


print(f"O Maior peso é o da {v2} pessoa com {maiorpeso}Kg")
print(f"O Menor peso é: {menorpeso}Kg")
