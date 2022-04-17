'''crie umprograma que leia um número inteiro qualquer e moastre na tela sua sequência de fibonacci!'''

n = int(input('Digite um número qualquer!'))
t1 = 0
t2 = 1
cont = 3
print('{} -> {} -> '.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    cont += 1
    t1 = t2
    t2 = t3
print('FIM')
