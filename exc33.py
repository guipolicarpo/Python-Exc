primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))

maior = primeiro
if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro
print('O maior número é {}'.format(maior))

menor = primeiro
if segundo < menor:
    menor = segundo
if terceiro < menor:
    menor = terceiro
print('O menor número é {}'.format(menor))
