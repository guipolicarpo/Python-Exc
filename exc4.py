qqc = input('Digite qualquer coisa: ')

print('O tipo deste valor é {}'.format(type(qqc)))
print('Só tem espaços? {}'.format(qqc.isspace()))
print('É um número? {}'.format(qqc.isnumeric()))
print('É alfabético? {}'.format(qqc.isalpha()))
print('É alfanúmerico? {}'.format(qqc.isalnum()))
print('Está em maíusculas? {}'.format(qqc.isupper()))
print('Está em minúsculas? {}'.format(qqc.islower()))
print('Está capitalizada? {}'.format(qqc.istitle()))



