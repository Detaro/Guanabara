from math import radians, sin, cos, tan

''' A biblioteca math por padrao usa a unidade de medida radianos e nao graus, logo, é necessario fazer a conversao do valor inserido 
usando math.radians importanto a toda biblioteca ou somente radians citando os itens importados  sobre a variavel. Nesse exemplo ele 
foi usado de forma aninhada com insersao da variavel seno'''

angulo = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(angulo))
coseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o COSENO de {:.2f}'.format(angulo, coseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))