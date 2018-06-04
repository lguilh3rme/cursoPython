import random   #Modulo randomizador

n1 = str(input('Individuo: '))
n2 = str(input('Individuo: '))
n3 = str(input('Individuo: '))
n4 = str(input('Individuo: '))

lista =[n1, n2, n3, n4]     #colchetes para listas

e = random.choice(lista)    #.choice escolha randomica dentro da lista

print('O infeliz escolido para faxina foi: {}'.format(e))


