from datetime import date
ano = int(input('Informe o ano atual: '))
if ano == 0:
    ano = date.today().year
if (ano % 400 == 0) or (ano % 4 == 0) and (ano % 100 != 0): 
    print('Você informou o ano: {}, ele é bissexto '.format(ano))
else:
    print('Você informou o ano: {}, ele não é bissexto '.format(ano))