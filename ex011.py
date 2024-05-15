largura =float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))
tinta = (largura * altura) / 2
print('Sua parede tem uma área total de {:.2f}m² e precisará de {:.2f} litros de tinta para pintar-la'.format(largura * altura, tinta))