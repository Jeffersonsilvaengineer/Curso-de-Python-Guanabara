'''Faça um programa que leia o ano de nascimento de uma pessoa e mostre de acordo com sua idade;
SE ELE AINDA VAI SE ALISTAR: SE É A HORA DELE SE ALISTAR: OU SE JÁ PASSOU O TEMPO DE SE ALISTAR:
seu programa deve mostrar também quanto tempo já passou ou ainda falta!'''

import datetime

nasc = int(input('Qual é seu ano de nascimento?'))
ano = datetime.datetime.now()
if ano.year - nasc < 18:
    print('Quem nasceu em {} tem {} anos em {} ! ainda faltam {} anos para seu alistamento'.format(nasc,ano.year - nasc, ano.year, (nasc - ano.year) + 18))
elif ano.year - nasc == 18:
    print('Quem nasceu em {} tem {} anos! você deve se alistar este ano {} !!'.format(nasc, ano.year - nasc, ano.year))
else:
    print('Quem nasceu em {} tem {} anos em {} ! já passou {} anos do seu alistamento,'
          ' você deveria ter se  alistado em'.format(nasc, ano.year - nasc, ano.year,(ano.year - nasc) - 18), ano.year - (ano.year - nasc) + 18)
