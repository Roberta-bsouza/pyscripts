from datetime import date
print('BEM VINDO AO SERVIÇO MILITAR!')
atual = date.today().year
nasc = int(input('Informe o ano de seu nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} ano(s) para você se alistar.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em: {}'. format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado a {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento deveria ter acontecido em: {}'. format(ano))
