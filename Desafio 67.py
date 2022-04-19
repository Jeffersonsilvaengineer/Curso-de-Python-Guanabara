'''Faça um programa que mostre a tabuada de varios números, um de cada vez, para cada número digitado
pelo usuário. O programa será interrompido quando o número digitado for negativo.'''
nome = '='
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print(f'{nome:=^33}')
    for cont in range(1,11):
        print(f'{n} X {cont} = {n*cont}')
    print(f'{nome:=^33}')
print('Programa encerrado! volte sempre!')
