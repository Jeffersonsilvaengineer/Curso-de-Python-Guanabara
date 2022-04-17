'''Crie um programa que leia nome idade e sexo de 4 pessoas e no final mostre a média de idade de todo o grupo,
 qual é o nome do homem mais velho e quantas mulheres tem menos de 20 anos!'''
homemvelho = 0
nomevelho = 0
mulher20 = 0
id = 0
for n in range(1, 5):
    print('======= {} PESSOA ======'.format(n))
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO M/F: '))
    id += (idade) / 4
    if n == 1 and sexo in 'Mm':
        homemvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > homemvelho:
        homemvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <20:
        mulher20 += 1
print('A média de idade das 4 pessoas é {}! '.format(id))
print('O homem mais velho tem {} anos e se chama {}! '.format(homemvelho,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos! '.format(mulher20))
