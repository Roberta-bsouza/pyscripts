x = input('Digite qualquer informação: ')
print('O tipo primitivo desse valor é:', type(x))
print('Só tem espaços?', x.isspace())
print('É um número?', x.isalpha())
print('É alfanumérico?', x.isalnum())
print('Está em maiúsculo?', x.isupper())
print('Está em minússcula?', x.islower())
print('Está capitalizada?', x.istitle())