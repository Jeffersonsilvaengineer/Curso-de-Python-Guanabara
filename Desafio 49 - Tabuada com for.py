'''Crie uma tabuada usando o laço for!'''

numero = int(input('DIGITE UM NÚMERO PARA TER ACESSO A SUA TABUADA:'))
for cont in range(1, 11):
    print('{} X {} = {}'.format(numero,cont,numero*cont))


