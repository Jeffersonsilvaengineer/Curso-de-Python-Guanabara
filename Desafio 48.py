'''Crie umprograma que faça a soma entre todos os números impares multiplos de três no intervalo de 1 a 500!'''

cont = 0
soma = 0
for impar in range(3, 501, 2):
    if impar % 3 == 0:
        cont = cont + 1
        soma = soma + impar
print('A soma de todos os {} números é igual a {} !'.format(cont,soma))


