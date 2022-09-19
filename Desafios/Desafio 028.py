from random import randint
print("JOGO DE ADVINHAÇÂO 1.0")
num = randint(1, 5)


v1 = int(input('Insira um valor entre 1 e 5: '))
while v1 < 1 or v1 > 5:
    v1 = int(input('Valor fora dos parametros! Insira um valor entre 1 e 5: '))

if v1 == num:
    print("Arcertou Miseravi")
else:
    print(f"ERRRROOOOU o numero escondido era {num}")
