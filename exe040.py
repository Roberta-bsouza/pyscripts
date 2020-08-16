veloc = float(input('Informe a velocidade que seu carro atingiu:'))
print('Seu carro atingiu a velocidade de : {} km/h'.format(veloc))
if veloc >= 80:
    print('Você ultrapassou a velocidade permitida. Você será multado!')
    multa = veloc*7
    print('O valor da sua multa é de R$:{:2}'.format(multa))
else:
    print('Parabéns! Você não ultrapassou a velocidade permitida.')