#trabalhando com manipulação de strings
#fatiamento de string
frase = 'Curso em vídeo python'
print(frase[::2])
print(frase.count('0'))
print(frase.upper().count('0'))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print(frase.strip())
print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.lower().find('vídeo'))
divido = frase.split()
print(divido[2][3])
