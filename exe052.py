casa = float(input('Informe o valor do imóvel que quer comprar: R$  '))
salario = float(input('Informe o valor do seu salário atual:R$  '))
qtdanos = int(input('Informe a quantidade de parcelas que você pode pagar:  '))
vparc = salario*0.3
prestcasa = casa/(qtdanos*12)
print('Para pagar uma casa de R$ {:.2f} em {}  anos'.format(casa, qtdanos),end='')
print('\n A prestação será de R$: {:.2f}'.format(prestcasa))
if vparc > prestcasa:
   print('Parabéns, você pode fazer o financiamento! Sua renda de R$ {} não compromete o valor das parcelas.'.format(salario))
else:
   print('Infelizmente seu financiamento não pode ser liberado,\nsua renda não comporta este financiamento:')