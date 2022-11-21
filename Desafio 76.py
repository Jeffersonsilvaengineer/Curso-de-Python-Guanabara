'''Crie um programa que tenha um tupla única com nomes de produtos e seus respectivos preços, na sequeência mostre:
a lista organizada de forma tubolar!'''

lista = ('Corsa', 15000, 'Astra', 25000, 'Civic', 45000, 'Corola', 90000, 'Jeep', 150000, 'Sw4', 340000, 'Land Rover', 460000)

print('=='*20)
print('{: ^40}'.format('LISTAGEM DE PREÇOS'))
print('=='*20)
for pos in range(0,len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:.>7.2f}')