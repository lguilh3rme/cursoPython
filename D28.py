#encoding: utf-8
'''# Comentario multiline#
 Condições

-if e else
    /ESTRUTURA COMPOSTA
 if condição(): #dois pontos
    comando()
else:           #dois pontos
    comando()
print('FIM')    #sempre executa
    /ESTRUTURA SIMPLIFICADA
print('um' if m=1 else 'nao um')
'''
import random
pc = random.randint(0,5)
me = raw_input('Escolha um numero entre 0 e 5:')
if me == pc:
    print('Acertou!!')
else:
    print('Eroooou!!')
print('O numero era: {}'.format(pc))

