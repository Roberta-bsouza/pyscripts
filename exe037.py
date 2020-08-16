#analise de string
n = str(input('Informe seu nome completo: '))
nome = n.split()#fatia o nome informado
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
