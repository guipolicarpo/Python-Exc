from random import randint
from time import sleep
ran = randint(0, 5)
print('-=-' * 20)
num = int(input('Tente adivinhar o número que estou pensando entre 0 e 5: '))
print('Processando...')
print('-=-' * 20)
sleep(3)

if num == ran:
    print('Você acertou, estava pensando no {}!!!'.format(ran))
else:
    print('Você errou, estava pensando no {}!!!'.format(ran))

