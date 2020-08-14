from math import hypot
catop = float(input('Informe comprimento do cateto oposto: '))
catad = float(input('Informe comprimento do cateto adjacente: '))
#hi = (catop**2 + catad**2) **(1/2)
hi = hypot(catop, catad)
print('A hipotenusa vai medir {:.2f}'.format(hi))