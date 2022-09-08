'''Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio pergunte
ao usuário será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas
de cada valor será entregue. obs: considere que o caixa tenha cédulas de R$50, R$20, R$10 E R$1.'''

print('{:=^30}'.format(' BANCO JEFFERSON '))
sac = int(input('Que valor você quer sacar? R$ '))
if sac < 10:
    d = sac*1
    print(f'O total {d} cedulas de 1 real!')
elif 10 < sac < 20:
    d1 = sac - 10
    d = sac*1
    print('O total de 1 cédula de 10 reais')
    print(f'O total de {d1} cédulas de 1 real')
elif sac == 20:
    print('O total de 1 cédula de 20 reais')
elif 20 < sac < 30:
    d3 = sac - 20
    d4 = d3*1
    print('O total de 1 cédula de 20 reais')
    print(f'O total de {d4} cédulas de 1 real')
elif sac == 30:
    print('O total de 1 cédula de 20 reais')
    print('O total de 1 cédula de 10 reais')
elif 30 < sac < 40:
    print('O total de 1 cédula de 20 reais')
    print('O total de 1 cédula de 10 reais')
    d5 = sac - 30
    d6 = d5*1
    print(f'O toal de {d6} cédulas de 1 real')
elif sac == 40:
    print('O total de 2 cédulas de 20 reais' )
elif 40 < sac < 50:
    print('O total de 2 cédulas de 20 reais')
    d7 = sac - 40
    d8 = d7*1
    print(f'O total de {d8} cédulas de 1 real')
elif sac == 50:
    print('O total de 1 cédula de 50 reais')


