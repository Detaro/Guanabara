tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')


while True:
    v1 = int(input('Insira um valor entre 0 e 10: '))
    if 10 >= v1 >= 0:
        break
print(tupla[v1])
