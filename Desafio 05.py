print('faça um progama que leia um numero e mostre seu antecessor e seu sucessor!')
n = int(input('digite um numero!'))
a = n - 1
s = n + 1
print('o numero é \033[7;30;45m{}\033[m seu antecessor é \033[30;44m{}\033[m e seu sucessor é \033[31;42m{}\033[m'.format( n, a, s))

