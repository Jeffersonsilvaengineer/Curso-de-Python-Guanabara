'''Um professor quer sortear um dos seus quatros alunos para apagar o quadro.'
      'faça um programa que embalhare os nomes e mostre na tela a nova ordem!'''

from random import shuffle

a1 = str(input('Nome do primeiro aluno?'))
a2 = str(input('Nome do segundo aluno?'))
a3 = str(input('Nome do terceiro aluno?'))
a4 = str(input('Nome do quarto aluno?'))
nome = [a1, a2, a3, a4]
ordem = shuffle(nome)
print('A ordem dos alunos escolhidos para apagar o quadro será!')
print(nome)

