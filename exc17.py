import math
catetoo = float(input('Comprimento do cateto oposto: '))
catetoa = float(input('Comprimento do cateto adjacente: '))
hipot = (catetoo**2) + (catetoa**2)
print('O comprimento da hipotenusa é {:.2f}'.format(math.sqrt(hipot)))
