sal = float(input('Informe o salário do funcionário: '))
aumsal = sal + (sal * 0.15)
print('O salário do funcionário que era de R${:2}, com aumento de 15% de aumento ele passará a receber R${:2}'.format(sal,aumsal))