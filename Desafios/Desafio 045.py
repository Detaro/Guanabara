from random import randint
from time import sleep
print('''JOKENPÔ
ESCOLHA ENTRE AS OPÇÕES:
[0] - PEDRA
[1] - PAPEL
[2] - TESOURA''')

choice = int(input("Qual a sua jogada? "))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('%%%'*12)


lista = ('Pedra', 'Papel', 'Tesoura')

pc = randint(0, 2)

print(f'o Computador escolheu {lista[pc]} ')
print(f'o Jogador escolheu {lista[choice]} ')
print('%%%'*12)

if pc == 0:
    if choice == 0:
        print("EMPATE")

    elif choice == 1:
        print("JOGADOR VENCEU")

    elif choice == 2:
        print("COMPUTADOR VENCEU")
if pc == 1:
    if choice == 0:
        print("COMPUTADOR VENCEU")

    elif choice == 1:
        print("EMPATE")

    elif choice == 2:
        print("JOGADOR VENCEU")

if pc == 2:
    if choice == 0:
        print("JOGADOR VENCEU")

    elif choice == 1:
        print("COMPUTADOR VENCEU")

    elif choice == 2:
        print("EMPATE")
