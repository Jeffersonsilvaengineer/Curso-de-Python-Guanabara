'''  Crie um programa que leia uma frase pelo teclado e mostre:
     Quantas vezes aparece a letra A:
     Em que momento aparece a primeira vez:
     Em que momento aparece pela última vez:'''

x = str(input('Digite uma frase qualquer!')).upper().strip()
print('A letra A aparece {} vezes na frase!'.format(x.count('A')))
print('A letra A aparece pela primeira vez na posição {}!'.format(x.find('A')))
print('A letra A aparece pela última vez na posição {}!'.format(x.rfind('A')))



