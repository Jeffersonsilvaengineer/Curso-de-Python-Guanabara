'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte
seu programa deverá ler um número pelo teclado entre zero e vintee mostralo por extenso.'''

from num2words import num2words

contagem = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'catorze', 'qinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
     numero = int(input('Digite um numero! '))
     if 0 > numero > 20:
         print('NÚMERO INVÁLIDO!, TENTE NOVAMENTE!')
     elif 0<= numero <=20:
         print(f'Você digitou o número {contagem[numero]} ')
         continuar = str(input('Quer continuar? [S] SIM  [N] NÃO')).strip().upper()
         if continuar in 'N':
                break
print('Obrigado! programa finalizado!')


