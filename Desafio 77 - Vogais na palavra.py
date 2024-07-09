''' Crie um programa que tenha uma tupla com várias palavras, no final mostre todas as palavras e suas vogais'''

tupla = ('amor', 'beijo', 'coraçao', 'aprender', 'python', 'palmeiras', 'casa', 'trabalho', 'motor',
         'telegrama', 'artistas', 'protetor', 'caramelo', 'morango', 'pescaria', 'praticar', 'ler', 'viver')
for c in tupla:
    print(f'\nNa Palavra {c.upper()} temos ', end=' ')
    for x in c:
        if x in 'aeiou':
            print(x, end=' ')

