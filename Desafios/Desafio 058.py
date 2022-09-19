from random import randint
print("JOGO DE ADVINHAÇÂO 2.0")
num = randint(1, 5)
palpite = 1

v1 = int(input('Insira um valor entre 1 e 5: '))
while v1 > 5 or v1 < 1:
    v1 = int(input('Valor fora dos parametros! Insira um valor entre 1 e 5: '))

while v1 != num:
    palpite += 1
    v1 = int(input('Outra Chance! Insira um valor entre 1 e 5: '))



print(f"Arcertou Miseravi! com {palpite} Palpites! ")
