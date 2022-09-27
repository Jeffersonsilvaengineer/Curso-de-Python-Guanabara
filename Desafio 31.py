'''Crie um progama que leia a distância em km de uma viagem, calcule o valor da passagem cobrando
 R$ 0,50 por km para viagens até 200 km e R$ 0,45 por km para viagens acima de 200 km!'''

d = float(input('Digite a distância em km da viagem!'))
if (d <= 200):
    print('O valor da passagem foi',d * 0.50)
print('O valor da passagem foi',d * 0.45)
    