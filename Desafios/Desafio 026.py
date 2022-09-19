#  Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
#  em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

f = str(input('Digite uma frase: ')).strip()
print(f.capitalize())

m = f.lower()
print('A letra A aparece {} vezes na frase.'.format(m.count('a')))


p1 = m.find('a')+1
print('A letra A aparece a primeira vez na posição {} '.format(p1))


p2 = m.rfind('a')+1
print('A letra A aparece a ultima vez na posição {}'.format(p2))

# o '+1' foi usado para a contagem de posições começar de 1 ao invés do padrão q é 0