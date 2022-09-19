n = int(input("Insira um valor para sequencia: "))
print('|0 ', end='')
resultado = 1
fibonacci = 1
antecessor = 0
for c in range(1, n+1):
    print(f'|{resultado} ', end='')
    resultado = fibonacci + antecessor
    antecessor = fibonacci
    fibonacci = resultado
    c +=1




