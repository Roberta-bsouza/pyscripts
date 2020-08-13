base = float(input('Informe a largura da sua parede: '))
altura = float(input('Informe a altura da sua parede: '))
area = base * altura
litrostinta = area / 2
print('A quantidade de litros de tinta necessária para pintar sua area de:', area,'m² é de {:.2} litros'.format(litrostinta))