'''Um professor quer sortear um dos seus quatros alunos para apagar o quadro.'
      'faça um programa que ele, lendo o nome dos alunos  escolha um!'''

from random import choice

a1 = input('Nome do primeiro aluno?')
a2 = input('Nome do segundo aluno?')
a3 = input('Nome do terceiro aluno?')
a4 = input('Nome do quarto aluno?')
nome = choice([a1, a2, a3, a4])
print('O aluno escolhido para apagar o quadro foi {}!'.format(nome))
