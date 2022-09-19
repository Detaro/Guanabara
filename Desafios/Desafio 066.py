s = []
s2 = []
while True:
    try:
        n = int(input('Digite um número a ser somado ou [999 para sair]: '))
    except:
        print('Erro: Valor incorreto.')
        continue
    if n == 999:
        break
    s2 += [str(n)]
    s += [n]
print(f"Foram digitados {len(s)} números.\nA soma entre {' + '.join(s2)} = {sum(s)}.")
