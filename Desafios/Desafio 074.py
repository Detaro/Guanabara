from random import randint

n = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print(f'Numeros sorteados:', end=' ')
for c in n:
    print(c, end=' ')


print(f'\nMaior numero {max(n)}')
print(f'Menor numero {min(n)}')

