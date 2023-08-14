'''Faça um programa que leia o ano de nascimento de uma pessoa e mostre de acordo com sua idade;
SE ELE AINDA VAI SE ALISTAR: SE É A HORA DELE SE ALISTAR: OU SE JÁ PASSOU O TEMPO DE SE ALISTAR:
seu programa deve mostrar também quanto tempo já passou ou ainda falta!'''

import datetime

nasc = int(input('Qual é seu ano de nascimento?'))
ano = datetime.datetime.now()
if ano.year - nasc < 18:
    print(
        f'Quem nasceu em {nasc} tem {ano.year - nasc} anos em {ano.year} ! ainda faltam {(nasc - ano.year) + 18} anos para seu alistamento')
elif ano.year - nasc == 18:
    print(f'Quem nasceu em {nasc} tem {ano.year - nasc} anos! você deve se alistar este ano {ano.year} !!')
else:
    print(
        f'Quem nasceu em {nasc} tem {ano.year - nasc} anos em {ano.year}! já passou {(ano.year - nasc) - 18} anos do seu alistamento, '
        f'você deveria ter se  alistado em {(ano.year - nasc) + 18}')
