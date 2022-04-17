'''crie um progama que leia quanto de dinheiro possui na carteira e mostre quantos dolares ela pode comprar! 1 dolar = 3,27'''

n = int(input('Digite um valor!'))
c = n / 3.27
print('você tem {} reais na cateira e pode comprar {:.2f} dolares!'.format(n,c))
