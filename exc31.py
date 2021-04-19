dist = float(input('Quantos Km de distância é o seu destino: '))

if dist > 200:
    print('O valor da sua passagem é R${}'.format(dist*0.45))
else:
    print('O valor da sua passagem é R${}'.format(dist * 0.50))
