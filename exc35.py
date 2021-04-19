a = float(input('Qual o comprimento em cm do lado A: '))
b = float(input('Qual o comprimento em cm do lado B: '))
c = float(input('Qual o comprimento em cm do lado C: '))

if (a + b) > c and (a + c) > b and (c + b) > a:
    print('As medidas podem formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')
