'''Refaça o desafio 51 , lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
utilizando a estrutura while!'''

print('='*30)
print('{: ^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = p
cont=1
while cont <10:
    termo+=r
    cont+=1
    print(termo, end=' -> ')
print('ACABOU!')
