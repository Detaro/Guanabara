opcao = 0
soma = 0
mult = 0
maior = 0
while opcao != 5:
      v1 = int(input('Insira um valor: '))
      v2 = int(input('Insira um valor: '))
      print('\nSelecione uma das Opções abaixo:\n'
            '[1] SOMAR\n'
            '[2] MULTIPLICAR\n'
            '[3] MAIOR\n'
            '[4] NOVOS NÚMEROS\n'
            '[5] SAIR DO PROGRAMA\n')

      opcao = int(input())

      while opcao == 4:
            print('[Novos Números]')
            v1 = int(input('Insira um valor: '))
            v2 = int(input('Insira um valor: '))
            print('Selecione uma das Opções abaixo:\n'
                  '[1] SOMAR\n'
                  '[2] MULTIPLICAR\n'
                  '[3] MAIOR\n'
                  '[4] NOVOS NÚMEROS\n'
                  '[5] SAIR DO PROGRAMA\n')
            opcao = int(input())

      while opcao == 1:
            soma = v1 + v2
            print(f"Soma dos termos: {soma}\n")
            break

      while opcao == 2:
            mult = v1 * v2
            print(f'Multiplicação dos termos: {mult}\n')
            break
      while opcao == 3:
            if v1 > v2:
                  maior = v1
            else:
                  maior = v2
            print(f"O maior número é: {maior}")
            break

print('Obg por usar meu programa!')
