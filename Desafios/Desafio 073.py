tupla = ('Flamengo', 'Fluminense', 'Botafogo', 'Vasco', 'Cruzeiro', 'Atletico-Mg', 'São Paulo', 'Corinthians', 'Santos',
         'Palmeiras', 'Internacional', 'Gremio', 'Chapecoense', 'Bahia', 'Athletico PR', 'Bragantino', 'Coritiba', 'Cuiaba',
         'Avaí', 'America Mg')
print("OS QUATRO PRIMEIROS SÃO:")
for pos, time in enumerate(tupla[0:5]):
    print(pos + 1, time)

print("\nOS QUATRO ULTIMOS SÃO:")
for pos, time in enumerate(tupla[-4:]):
    print(pos + 17, time)

print('\nOS TIMES ORDENADOS SÃO:')
nova = sorted(tupla)
for pos, time in enumerate(nova):
    print(pos + 1, time)

print("\nO CLUBE CHAPECOENSE ESTA NA POS:")
print(tupla.index('Chapecoense') + 1)

