print('-**-'*20)
print('Analizador de triangulos:')
print('-**-'*20)
seg1 = float(input('Informe o tamanho da primeira reta: '))
seg2 = float(input('Informe o tamanho da segunda reta: '))
seg3 = float(input('Informe o tamanho da terceira reta: '))
if (seg1< seg2) and (seg2< seg1 + seg3) and (seg3<seg1 + seg2):
    print('Os seguimentos acima Podem formar triângulo.')
else:
    print('Os seguimentos acima NÂO podem formar triângulo.')