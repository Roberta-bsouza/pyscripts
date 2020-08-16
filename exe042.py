dist = float(input('Informe a distãncia que será percorrida durante a viagem: '))
print( 'Você informou que a distância percorrida foi de: {} km.'.format(dist))
if dist <=200:
    valorpass1 = (dist*0.50)
    print('Você deve pagar o valor de R$: {}'.format(valorpass1))
    print('Boa viagem!')
else:
    valorpass2 = (dist*0.45)
    print('Você deve pagar o valor de R$: {}'.format(valorpass2))
    print('Boa viagem!')
#ou pode ser resolvido de forma simplificada: preço = dist * 0.50 if dist <= 200 else dist *0.45