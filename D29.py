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
vel = float(input('Velocidade: '))
c = float((vel-80)*7)
if vel > 80:
    print('Multado em: R${:.2f}'.format(c))
else:
    print('Suave!') 