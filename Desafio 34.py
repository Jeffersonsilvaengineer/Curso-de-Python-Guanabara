'''Faça um programa que pergunte o salário de uma pessoa e cálcule seu aumento, para salários acima de 1.250,00
aumento de 10%, para salários iguais ou inferiores a 1.250,00 aumento de 15%.'''

sa = float(input('Qual o seu salário?'))
if sa > 1250:
    print('Seu aumento foi de R$ {}, e seu novo salário é de R$ {}!'.format(sa*10/100, sa+(sa*10/100)))
else:
    print('Seu aumento foi de R$ {}, e seu novo salário é de R$ {}!'.format(sa*15/100, sa+(sa*15/100)))
