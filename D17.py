from math import sqrt

ca = int(input('Cateto adjacente ao angulo: '))
co = int(input('Cateto oposto ao angulo: '))
hp = sqrt((co ** 2) + (ca ** 2))
# ou posso importar math e usar math.hypot(co, ca)
print('A hipotenusa desse triangulo é {}'.format(hp))
