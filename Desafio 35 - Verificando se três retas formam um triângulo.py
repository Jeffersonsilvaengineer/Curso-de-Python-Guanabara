'''Crie um progama que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo!'''

p = float(input('Digite o comprimento da primeira reta!'))
s = float(input('Digite o comprimento da segunda reta!'))
t = float(input('Digite o comprimento da terceira reta!'))
if p < s+t and s < p+t and t < p+s:
    print('Éssas retas formam um triângulo!')
print('Essas retas não formam um triângulo!')
