nome = str(input('Digite um nome completo'))

M = (nome.lower())

print('Verificando se o nome {} possui SILVA...'.format(nome))
print('Resultado: {}'.format('silva'in M))