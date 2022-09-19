num = int(input('Inira um valor na base 10: '))
print('1. DECIMAL para HEXADECIMAL')
print('2. DECIMAL para OCTAL')
print('3. DECIMAL para BINARIO')

escolha = int(input())

if escolha == 1:
    print(f'Hexadecimal de {num} é: {hex(num).lstrip("0x").rstrip("L")}')

if escolha == 2:
    print(f'Octal de {num} é: {oct(num).lstrip("0o").rstrip("L")}')

if escolha == 3:
    print(f'Binario de {num} é: {bin(num).lstrip("0b").rstrip("L")}')
