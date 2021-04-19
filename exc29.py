velo = int(input('Digite a velocidade que o carro passou: '))

if velo > 80:
    multa = (velo - 80)*7
    print('Você será multado por exceder o limite de velocidade! A multa é no valor de R${} '.format(multa))
else:
    print('Você estava dentro do limite de velocidade!')
