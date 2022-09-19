from random import randint
print('PAR OU IMPAR!\n'
      '[1] Impar\n'
      '[2] Par\n')

vit = derrotas = res = 0

while derrotas != 1:
    escolha = int(input('Digite uma opção: '))
    if escolha == 1:
        v1 = randint(1, 2)
        v2 = int(input('Insira um numero: '))
        res = v2 + v1
        if res % 2 == 0:
            derrotas += 1
            print("Derrota!")
        else:
            vit += 1
            print("Vitória !")

    if escolha == 2:
        v1 = randint(1, 2)
        v2 = int(input('Insira um numero par: '))
        res = v2 + v1
        if res % 2 == 0:
            vit += 1
            print("Vitória !")
        else:
            derrotas += 1
            print("Derrota!")

print(f'Vc conseguiu {vit} vitórias consecutivas ')