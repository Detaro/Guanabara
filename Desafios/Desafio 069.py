while True:
    sx = resp = " "

    idad = int(input("Insira o valor da idade: "))
    while sx not in 'MF':
        sx = input("Qual o Sexo [M/F]: ").strip().upper()[0]

    while resp not in 'SN':
        resp = input("Deseja continuar [S/N]? ").strip().upper()[0]

        if resp != 'N':
            print('teste')
        else:
            print('teste2')
            break





