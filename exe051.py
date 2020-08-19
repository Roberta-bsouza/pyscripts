#Teoria
#condições aninhadas
#carro.siga():                 if carro.esquerda():
  #secarro.direita()           elif carro.direira(): 
    #carro.siga()              
    #carro.esquerda()          elif carro.direira():
                               #else
nome = str(input('Qual é o seu nome?'))   
if nome == 'Roberta':      
    print('Que nome bonito!') 
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
#else:
    #print('Seu nome é bem normal.')  
print('Tenha um bom dia!, {}'.format(nome))                