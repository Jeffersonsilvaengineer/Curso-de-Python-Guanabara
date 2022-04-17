'''Faça um programa que leia o sexo de uma pessoa mas só aceite os valores "m ou f" caso esteja errado
peça a digitação novamente até ter um valor correto!'''

sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MFmf':
        sexo = str(input('Dados inválidos, digite novamente! ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
