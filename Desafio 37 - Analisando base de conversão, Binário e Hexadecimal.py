'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
conversão! '''

nu = int(input('Digite um número qualquer!'))
print('Qual será a base de conversão?\nDigite 1 para'
      ' Binário!\nDigite 2 para octal!\nDigite 3 para hexadecimal!')

op = int(input('Digite uma opção:'))
if op == 1:
    print('O número {} convertido para a base binária é igual a {}'.format(nu, bin(nu)[2:]))
elif op == 2:
    print('O número {} convertido para a base octal é igual a {} !'.format(nu, oct(nu)[2:]))
elif op == 3:
    print('Onúmero {} convertido para a base exadecimal é igual a {} !'.format(nu, hex(nu)[2:]))
else:
    print('Opção invalida! tente novamente!')


