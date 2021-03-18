import math
ang = float(input('Digite o valor de um ângulo: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print('O ângulo de {} possui cosseno {:.2f}, seno {:.2f} e tangente {:.2f}'.format(ang, cos, seno, tg))
