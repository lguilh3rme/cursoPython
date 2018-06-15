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
#___D22___
var = raw_input('Nome: ')
div = var.split()
print(len(var))
print(var.upper())
print(var.lower())
print(div)
print(len(''.join(div))) #AAAA \O/
print(len(div[0]))