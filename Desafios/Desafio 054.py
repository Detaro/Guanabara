from datetime import date
atual =  date.today().year

totmaior = 0
totmnenor = 0

for pess in range(1, 8):
    nasc = int(input(f"{pess}- Insira o ano de Nascimento: "))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmnenor +=1
print(f"Total de maiores: {totmaior}")
print(f"Total de menores: {totmnenor}")
