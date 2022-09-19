from datetime import date
somaid = 0
maiorid = 0
qtdmenor = 0

for c in range(1, 5):
    nom = input(f'{c}- Insira o nome: ')
    ano = int(input(f"{c}- Insira o ano de nascimento: "))
    idade = date.today().year - ano
    sex = input(f"{c}- Insira o sexo (M/F): ").upper()
    somaid = idade + somaid

    if idade > maiorid and sex == 'M':
        maiorid = idade
    if idade < 20 and sex == 'F':
        qtdmenor += 1





media = somaid/4
print(f'A Media de idade é de {media:.1f} anos')
print(f'Existem {qtdmenor} mulheres com menos de 20 anos')
print(f'O homem mais velho tem {maiorid} anos')
