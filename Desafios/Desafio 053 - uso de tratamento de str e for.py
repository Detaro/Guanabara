f = str(input('Insira uma frase')).strip().upper().split()
f2 = ''.join(f)
inv = ''

for letra in range(len(f2) - 1, -1, -1):
    # len(f2) - 1 == numero de letras de f2 -1 (O -1 é pq começa sempre da pos
    # 0, então se uma frase conter 20 letras vai ser do 0 ao 19 = 20
    # O SEGUNDO -1 SIGNIFICA VAI ATÉ A POSIÇÃO 0
    inv = inv + f2[letra]

if inv == f2:
    print(f'Palindromo encontrado: {f}, {inv}')
else:
    print(f'Palindromo não encontrado: {f}, {inv}')
