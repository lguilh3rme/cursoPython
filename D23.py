#encoding: utf-8
#   Fatiamento de cadeia
#var string -> Organizado como cadeia
#var=('Ola mundo')//10 posições de 0 a 9
#var(:3)//mostra ate a posiçao 3 (Ola)
#len(frase)//conta as posiçoes
#frase.count('o') quantas letras o
#'mundo' in var // se sim r:True
#   transformaçao
#var.replace('mundo','Brasil!' )
#var.upper() // OLA MUNDO
#var.lower() // ola mundo
#var.title() // Ola Mundo
#var.strip() // elimina espaços inuteis
#      divisão
#var.split() // separa os nomes
#'-'.join(var) // ola-mundo
#___D23___
nmr = int(input('Digite um nmr: '))
#nst = str(nmr)
u = nmr // 1 % 10
d = nmr // 10 % 10
c = nmr // 100 % 10
m = nmr // 1000 % 10
print('Unidade:{}'.format(u))
print('Dezena :{}'.format(d))
print('Centena:{}'.format(c))
print('Milhar :{}'.format(m))