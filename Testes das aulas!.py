'''crie um programa que tenha duas variaveis inteiras, a primeira vai ter o dia inicial
 e a segunda vai ter dia da semana a acrescentar a primeira'''
'ex: se a primeira variavel tiver o valor de 0 e a segunda com o valor 2, o programa deve mostar terça feira'

dias = ['Domingo', 'Segunda feira', 'Terça feira', 'Quarta feira', 'Quinta feira', 'Sexta feira', 'Sabado']

va1 = str(input('Digite um dia da semana: ')).upper()
va2 = int(input('Digite um valor: '))
if va1 == 'DOMINGO':
    va1 = 0
elif va1 == 'SEGUNDA FEIRA':
    va1 = 1
elif va1 == 'TERÇA FEIRA':
    va1 = 2
elif va1 == 'QUARTA FEIRA':
    va1 = 3
elif va1 == 'QUINTA FEIRA':
    va1 = 4
elif va1 == 'SEXTA FEIRA':
    va1 = 5
elif va1 == 'SABADO':
    va1 = 6
z = va2 % 6
print(z)
if z == 0:
    print(dias[0])
elif z == 1:
    print(dias[1])
elif z == 2:
    print(dias[2])
elif z == 3:
    print(dias[3])
elif z == 4:
    print(dias[4])
elif z == 5:
    print(dias[5])
elif z == 6:
    print(dias[6])

