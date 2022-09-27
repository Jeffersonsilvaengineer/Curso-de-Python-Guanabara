'''Faça um programa que leia a velocidade de um automovel, se ele ultrapassar 80/km mostre uma mensagem
dizendo que ele foi multado e o valor da multa! considerar 7 reais para cada km ultrapassado do limite.'''

v = float(input('Digite a velocidade de um automovel!'))
multa = (v - 80)*7
exedido = (v - 80)
if v >=80.0:
    print('Voçê ultrapassou a velocidade maxíma de 80.0 km em {}km e  foi multado em {} reais!'.format(exedido,multa))
print('PARABÉNS! voçê esta dentro da velocidade maxíma permitida.')

