#condições em python 
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
   print('Carro Novo')
else:
    print('Carro Velho')
print('--FIM--')
#condição simplificada
tempo = int(input('Quantos anos tem seu carro?'))
print('Carro Novo' if tempo <=3 else 'Carro velho')
print('--FIM--')    

