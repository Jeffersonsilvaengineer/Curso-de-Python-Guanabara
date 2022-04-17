'''Faça um programa que leia duas notas de um aluno e calcule sua média, mostrando no final uma mensagem,
média abaixo de 5 reprovado!  média entre 5 e 6.9 recuperação!  média 7 ou superior aprovado!'''

n1 = float(input('Digite a primeira nota!'))
n2 = float(input('Digite a segunda nota!'))
media = (n1 + n2) / 2
print('Sua média é igual a',media)
if media <= 5:
    print('REPROVADO!')
elif media >=7:
    print('APROVADO!')
else:
    print('RECUPERAÇÃO!')
