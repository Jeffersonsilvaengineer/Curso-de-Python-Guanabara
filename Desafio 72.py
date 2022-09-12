'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte
seu programa deverá ler um número pelo teclado entre zero e vintee mostralo por extenso.'''

contagem = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'catorze', 'qinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um numero! '))
    while 0 > numero > 20:
        numero2 = int(input('NÚMERO INVÁLIDO!, Digite um numero entre 0 e 20! '))
        if 0 <= numero2 <= 20:
            break
        # print(f'Você digitou o número {contagem[numero]} ')
    # continuar = str(input('Quer continuar? [S] SIM  [N] NÃO')).strip().upper()
    # while not continuar in 'SN':
    #     continuar = str(input('Quer continuar? [S] SIM  [N] NÃO')).strip().upper()


