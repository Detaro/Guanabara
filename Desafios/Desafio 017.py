'''  modo matematico 
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adjacente:'))
hi = (co **2 + ca **2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

''' modo import math'''

from math import hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adjacente:'))
hi = hypot(co, ca)
print('A hipotenusa va medir {:.2f}'.format(hi))