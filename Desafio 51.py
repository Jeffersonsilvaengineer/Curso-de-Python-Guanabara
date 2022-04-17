'''Crie um programa que leia o primeiro termo e a razão de uma PA, no final mostre os dez primeiros termos dessa PA!'''

print('='*30)
print('{: ^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dec = p + (10 - 1) * r
for cont in range(p, dec + r, r):
    print(cont, end=' -> ')
print('ACABOU!')
