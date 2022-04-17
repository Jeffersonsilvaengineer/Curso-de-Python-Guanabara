'''Crie um programa que leia um número de quatro digitos e mostre: sua unidade, dezena, centene e milhar.'''

a = int(input('Digite um numero de 0 a 9999!'))
print('O número digitado foi -->',(a))
u = a //1 % 10
d = a //10 % 10
c = a //100 % 10
m = a //1000 % 10
print('Unidade :[{}]'.format(u))
print('Dezena  :[{}]'.format(d))
print('Centena :[{}]'.format(c))
print('Milhar  :[{}]'.format(m))
