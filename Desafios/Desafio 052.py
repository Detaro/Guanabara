n = int(input('Insira um numero: '))
t = 0

for c in range(1, n + 1):
    if n % c == 0:
        t += 1
if t == 2:
    print(f"{n} é um numero primo")
else:
    print(f"{n} não é um numero primo")
