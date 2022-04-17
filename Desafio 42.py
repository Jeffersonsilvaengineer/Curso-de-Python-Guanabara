'''Crie um progama que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo!
e mostre se forma um triângulo equilátero , isósceles ou escaleno!'''

p = float(input('Digite o comprimento da primeira reta!'))
s = float(input('Digite o comprimento da segunda reta!'))
t = float(input('Digite o comprimento da terceira reta!'))
if p < s+t and s < p+t and t < p+s and p == s == t:
    print('Essas retas formam um triângulo EQUILÁTERO!')
elif p < s+t and s < p+t and t < p+s and p == t or p == s:
    print('Essa retas formam um triângulo ISÓSCELES!')
elif p != s != t and p < s+t and s < p+t and t < p+s:
    print('Essas retas formam um triângulo ESCALENO!')
else:
    print('Essas retas não formam um triângulo!')

