'''Melhore o desafio 61, perguntando se elequer mostrar mais termos, o programa termina quando o usuário digitar 0!'''

print('='*30)
print('{: ^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = p
cont=1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        termo+=r
        cont+=1
        print(termo, end=' -> ')
    print('Pausa!')
    mais = int(input('Mais quantos termos?'))
print('Fim da progreção! depois de {} termos!'.format(total))
