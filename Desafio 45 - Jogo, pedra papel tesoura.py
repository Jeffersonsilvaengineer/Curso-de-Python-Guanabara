'''Faça um programa que jogue pedra papel tesoura com o usuário!'''

print('{:=^80}'.format( '\033[31;40;7mPEDRA PAPEL TESOURA\033[m'))
print('SUAS OPÇÕES:\n[0] PEDRA \n[1] PAPEL \n[2] TESOURA')
import random
from time import sleep
itens = ( 'PEDRA', 'PAPEL', 'TESOURA')
maquina = random.randint(0,2)
jogador = int(input('DIGITE A SUA OPÇÃO!'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('{:=^80}'.format('\033[31;40;7m$$$$$$$$$$$$$$$$$$$$\033[m'))
print('JOGADOR JOGOU {}'.format(itens[jogador]))
print('MAQUINA JOGOU {}'.format(itens[maquina]))
print('{:=^80}'.format('\033[31;40;7m$$$$$$$$$$$$$$$$$$$$\033[m'))
if jogador == maquina:
    print('EMPATOU!')
elif jogador == 0 and maquina == 1 or jogador == 1 and maquina == 2 or jogador == 2 and maquina == 0:
    print('Maquina ganhou!')
elif jogador == 0 and maquina == 2 or jogador == 1 and maquina == 0 or jogador == 2 and maquina == 1:
    print('Jogador ganhou!')




