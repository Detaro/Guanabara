import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print(' A raiz de {} é igual a {}'.format(num, raiz))

# com arredondamento pra cima
print(' A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))

# com arredondamento pra baixo
print(' A raiz de {} é igual a {}'.format(num, math.floor(raiz)))

# com casas decimais determinadas
print(' A raiz de {} é igual a {:.3f}'.format(num, raiz))

# ## ------------------------------------------------------ ## #

