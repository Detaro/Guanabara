'''
    PADRÂO ANSI

 \033[STYLE;TEXT;BACK m
 STYLE -> tipo de texto (negrito, sublinhado ...)
 0 == None
 1 == Bold
 4 == underline
 7 == Negative

 TEXT -> Cor do texto
 30 ==  Branco
 31 == Vermelho
 32 == Verde
 33 == Amarelo
 34 == Azul
 35 == Roxo
 36 == Cian
 37 == Cinza (Padrao)

 BACK -> Cor do fundo
 40 ==  Branco
 41 == Vermelho
 42 == Verde
 43 == Amarelo
 44 == Azul
 45 == Roxo
 46 == Cian
 47 == Cinza (Padrao)

'''
print('\033[1;31;44mTeste')
print('\033[1;31;44mTeste\033[m') # DEIXAR O FUNDO SOMENTE NA STRING

a = 1
b = 2
print(f'Os Valores são \033[4;30;44m{a}\033[m e \033[31m{b}\033[m!!!!! ') # DEFININDO CORES DA VARIAVEL



