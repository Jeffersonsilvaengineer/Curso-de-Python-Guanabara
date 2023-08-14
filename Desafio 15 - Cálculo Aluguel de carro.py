'''Faça um programa que pergunte a quantidade de km rodados pelo carro e a quantidade de dias o carro foi alugado e
calcule o preço a pagar, sabendo que: a diária do carro custa 60 reais e 0,15 centavos por km rodado!'''

km = float(input('Quantos km o carro percorreu?'))
dias = int(input('Por quantos dias o carro foi alugado?'))
print('O valor a ser pago pelo aluguel do carro é de {} ! '.format((dias*60)+(km*0.15)))
