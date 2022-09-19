nome = input('qual o seu nome?')

# variavel replicada
print(nome *3)
# uso do .format
print('olá {}!'.format(nome))

# em n caracteres
print('olá {:20}!'.format(nome))

# alinhado a direita
print('olá {:>20}!'.format(nome))

# alinhado a esquerda
print('olá {:<20}!'.format(nome))

# centralizado
print('olá {:^20}!'.format(nome))

#QUEBRA DE LINHA \N
print('OlÁ\n{}'.format(nome))
#JUNÇÃO DE LINHAS ,end=''
print('OLÁ',end=' ')
print('{}!'.format(nome))