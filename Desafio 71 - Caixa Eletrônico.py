'''Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio pergunte
ao usuário será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas
de cada valor será entregue. obs: considere que o caixa tenha cédulas de R$50, R$20, R$10 E R$1.'''
print('='*30)
print('{:=^30}'.format(' BANCO JEFFERSON '))
print('='*30)
sac = int(input('Que valor você quer sacar? R$ '))
print('='*30)
total = sac
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'O total de {totalced} cédulas de {ced} reais')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('='*30)
print('VOLTE SEMPRE AO BANCO JEFFERSON!')

