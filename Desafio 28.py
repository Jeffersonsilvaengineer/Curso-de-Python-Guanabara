'''Faça um progama que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça o usuário tentar
descobrir qual foi o número escolhido pelo computador (o progama deverá escrever na tela se o usuário acertou ou errou)'''

import random

n = int(input('Digite um número entre 0 e 5!'))
a = random.randint(0,5)
print('O número pensado pelo computador foi',a)
if n == a:
    print('PARABÉNS! VOÇÊ ACERTOU O NÚMERO.')
else:
    print('PERDEU! VOÇÊ ERROU O NÚMERO.')
    