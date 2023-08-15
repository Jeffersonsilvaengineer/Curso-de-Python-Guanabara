'''Crie um programa que leia uma frase qualquer e diga se ela é um polindromo, desconsedere os espaços'''

frase = str(input('Digite uma frase! ')).strip().upper()
palavras = frase.split()
juntos = (''.join(palavras))
inverso = ''
for letra in range(len(juntos) -1, -1, -1):
    inverso += juntos[letra]
print('O inverso de {} é {}'.format(juntos, inverso))
if inverso == juntos:
    print(frase)
    print('TEMOS UM PALINDROMO!')
else:
    print('Afrase digitada não é um palindromo!')
