while True:
    tab = int(input("Quer ver a tabuada de qual valor: "))
    if tab > 0:
        for c in range(1, 11):
            res = tab * c
            print(f'{tab} x {c} = {res}')
    else:
        print("Fim")
        break