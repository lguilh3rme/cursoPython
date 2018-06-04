import math
an = int(input('Digite o angulo: '))
s = math.sin(an)
c = math.cos(an)
t = math.tan(an)

print('O seno de {} é {:.2f}; o cosseno é {:.2f}; a tangente é {:.2f}'.format(an, s, c, t))
