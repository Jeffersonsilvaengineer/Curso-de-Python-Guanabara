'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa e calcule seu IMC, e mostre seu estatus!
ABAIXO DE 18.5 = ABAIXO DO PESO!
ENTRE 18.5 E 25 = PESO IDEAL!
25 ATE 30 = SOBRE PESO!
30 A 40 = OBESIDADE!
ACIMA DE 40 = OBESIDADE MORBIDA!'''

p = float(input('Digite seu peso! (KG):'))
al = float(input('Digite sua altura!'))
imc = p / al**2
print('O imc dessa pessoa é {:.1f} !'.format(imc))
if imc <= 18.5:
    print('Você esté abaixo do peso!')
elif 18.5 < imc <= 25:
    print('Parabéns você está no peso ideal!')
elif 25 < imc <= 30:
    print('Cuidado você está com sobre peso!')
elif 30 < imc <= 40:
    print('URGENTE  se cuida você está com obesidade!')
elif imc > 40:
    print('URGENTE PROCURE ATENDIMENTO MÉDICO, VOCÊ ESTA COM OBESIDADE MORBIDA!')
    
