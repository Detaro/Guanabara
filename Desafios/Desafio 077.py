tupla = ('Teste', 'flamengo', 'Guanabara')

for itens in tupla:
    print(f'\nNa palavra {itens.upper()} temos: ', end=' ')
    for letra in itens:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')