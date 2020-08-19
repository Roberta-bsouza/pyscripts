a = 3
b = 5
'''print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[0;33;44mOlá, Mundo!\033[m')
print('\033[7;33;44mOlá, Mundo!\033[m')
print('Os valores são \033[32m{}\033]m e \033[31m{}!!!'.format(a, b))'''

nome = 'Roberta'
cores = {'limpa':'\033[m',
          'azul': '\033[34m',
          'amarelo': '\033[33m',
          'pretoebranco':'\033[7;30m'} 
       
print('Ola! Muito parzer em te conhecer, {}{}{}!!'.format(cores ['pretoebranco'], nome, cores['azul']))
