'''Faça um programa que mostre na tela uma contagem regrassiva de 10 a 0 , com pausa de 1 segundo entre os numeros'''

import emoji

from time import sleep
print('{:#^60}'.format('\033[40;34;7mCONTAGEM REGRESSIVA!\033[m'))
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print(emoji.emojize('FELIZ ANO NOVO!:fireworks:',use_aliases=True))
