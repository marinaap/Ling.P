# Faca um progama que leia a largura e a altura de uma parede em metros, 
# calcule a area e a quantindade de tinta necessária para pintá-la
# sabendo que cada litro de tinta pinta uma área de 2m2.

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
tinta = area / 2
print('A área total da parede é {} metros'.format(area))
print('Serão necessários {} Litros de tinta para pintar a parede.' .format(tinta))
