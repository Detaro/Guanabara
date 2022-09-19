n1 = float(input('Insira o valor da primeira nota: '))
n2 = float(input('Insira o valor da segunda nota: '))

media = (n1 + n2) / 2

if media >= 7:
    print(f"aprovado com media {media:.1f}")
elif media < 5:
    print(f"reprovado com media {media:.1f}")
elif media >= 5 and media <= 6.9:
    print(f"Em recuperação com media {media:.1f}")

