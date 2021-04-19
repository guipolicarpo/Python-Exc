salario = float(input('Digite o valor do salário do funcionário: R$'))

if salario > 1250:
    print('Recebeu um aumento de 10%. O novo salário é R${:.2f}'.format(salario*1.10))
else:
    print('Recebeu um aumento de 15%. O novo salário é R${:.2f}'.format(salario * 1.15))
