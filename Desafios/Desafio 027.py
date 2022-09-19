# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite um nome completo:')).strip().title()
print(nome)

i = nome.split()
pn = i[0]
print('Primeiro Nome: {}'.format(pn))

un = i[-1]
print('Ultimo nome: {}'.format(un))

