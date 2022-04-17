'''crie um progama que leia um valor em metros e converta em centimetros e milimetros!'''

v = int(input('digite um valor!'))
print('\033[31;46m{}\033[m metros é igual a  \033[30;45m{}\033[m centimetros e igual'
      ' a \033[42;31m{}\033[m milimetros'.format(v, v*100, v*1000))
