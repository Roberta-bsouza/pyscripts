import math
ang = float(input('Digite um ângulo qualquer: '))
sen = math.sin(math.radians(ang))
print('O ângulo de {} tem o Seno de {:.2f}'.format(ang, sen))
coss = math.cos(math.radians(ang))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(ang, coss))
tang = math.tan(math.radians(ang))
print('O ângulo de {} tem o Tangente de {:.2f}'.format(ang, tang))
