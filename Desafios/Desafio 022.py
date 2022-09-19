# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite um nome completo:')).strip()
nome2 =(nome.split())
Y = ' '.join(nome2)
print('Olá',Y.title())

print('Seu nome em maiusculo é: {}'.format(Y.upper()))

print('Seu nome em minusculo é: {}'.format(Y.lower()))

Tupla = (nome.split())
x = ''.join(Tupla)
print('Seu nome Possui {} letrsas'.format(len(x)))


print('Seu primeiro nome é {} e possui {} letras'.format(Tupla[0].capitalize(),len(Tupla[0])))