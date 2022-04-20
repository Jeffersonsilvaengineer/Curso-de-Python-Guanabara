'''Faça um progama que leia em metros a altura e largura de uma parede e calcule sua área e quanto de tinta será '
      'nescessario para pintar a parede! considere para cada litro de tinta voçê pinta 2 m²!'''

al = float(input('Digite a altura da parede!'))
lar = float(input('Didite a largura da parede!'))
area = float(al * lar)
c = area ** 1/2
print(f'A área da parede é {area} m²!')
print(f'Será nescessário {c} litros de tinta para pintar a parede!')



