'''nome = str(input('Informe seu nome:'))
if nome == 'Roberta':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'. format(nome))'''
#condicional simples apenas uma condição, mais de uma é condicional composta;
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi: {:1}'.format(m))
if m >= 6.0:
    print('Sua média foi boa. Parabéns, você está aprovado!')
else:
    print('Sua nota não foi suficiente. Estude mais!')

