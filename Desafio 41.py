'''Faça u  programa que leia o ano de nascimento de u a pessoa e mostre sua categoria de acordo com sua idade!
 até 9 anos = mirim
 até 14 anos = infantil
 até 19 anos = junior
 até 20 anos = senior
 acima de 20 anos = master'''

import datetime

nasc = int(input('Qual seu ano de nascimento!'))
ano = datetime.datetime.today()
idade = ano.year - nasc
if idade < 9:
    print('Categoria MIRIM!')
elif 9 < idade < 14:
    print('Categoria INFANTIL!')
elif 14 < idade <= 19:
    print('Categoria JUNIOR')
elif idade == 20:
    print('Categoria SENIOR!')
elif idade > 20:
    print('Categoria MASTER!')


