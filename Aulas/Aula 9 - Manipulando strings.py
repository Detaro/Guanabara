22,05
# FATIAMENTO DE STRING
''' frase     [CURSO EM VIDEO PYTHON]
    POSIÇÕES   0123456789...        20
         
EX: frase [9:13]     Pegara os caracteres do 9 até o 12        
    frase [9:21]     Pegara os caracteres do 9 até o 20 msm não existindo o 21 
    frase [9:21:2]   Pegara os caracteres do 9 até o 20 pulando de 2 em 2 (resposta: VdoPto )
    frase [:5]       Pegara os caracteres do 0 até o 4
    frase [15:]      Pegara os caracteres do 15 até o final
    frase [9::3]     Pegara os caracteres do 9 até o final de 3 em 3   
       '''


# ANALISE DE STRING


len(frase) 
' comprimento da frase ' R:  21 caracterers (de 0 a 20 )

frase.count('o')  
' qts vezes tem o caractere 'o' (minusculo) na frase ' R: 3

frase.count('o',0,13)
' qts vezes tem o caractere 'o' (minusculo) na frase do 0 até o 12' R: 1 

frase.find('deo') 
' ira apontar as posições q começam com essa string' R: 11

frase.find('Android') 
' ira apontar -1 que significa não encontrado ' R: -1

'Curso'in frase 
' retornará True ou False ' R: True



# TRANSFORMAÇÂO

frase.replace('Python','Androide')
'ira substituir uma string pela outra'

frase.upper()
'ira tranformar tds os caracteres da string em maiusculo'

frase.lower()
'ira tranformar tds os caracteres da string em minusculo'

frase.captalize()
'ira tranformar tds os caracteres da string em minusculo e colacar a pos 0 em maiusculo'

frase.title()
'ira tranformar tds os caracteres da string em minusculo e colacar a pos 0 em maiusculo e cada posição apos uma posição 'vazia' em maiusculo '
'colocando assim cada palavra com sua primeira letra em maiusculo'

frase.strip()
'remove os espaços 'inuteis' da string do lado direito e esquerdo'

frase.rstrip()
'remove os espaços 'inuteis' da string do lado direito'

frase.lstrip()
'remove os espaços 'inuteis' da string do lado esquerdo'

# DIVISÂO

frase.split()
'Gera uma lista com tdas as palavras de uma cadeia de caracteres gerando nova indexação para elas'
'[Curso][em][Video][Python]'
' 01234  01  01234  012345 '

'-'.join(frase)
'Faz a Junção e adicinona o caractere citado entre aspas'
'[Curso][em][Video][Python]'
'[Curso-em-Video-Python]'


