'''Faça um programa que converta uma temperatura digitada em ºc e converta para ºf'''

c = float(input('Digite uma temperatura em gráus ºc!'))
conv = ((9*c)/5)+32
print('A temperatura digitada em ºc é {1} , convertida em ºf é {0} !'.format(conv,c))
