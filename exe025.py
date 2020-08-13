'''mostrar porção inteira de um número
from math import trunc
a = float(input('Informe um valor decimal: '))
print('O valor digitado foi de {}, e a prção inteira é: {}'.format(a, trunc(a)))'''

num = float(input('Digite um número decimal: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))#sem usar múdulos