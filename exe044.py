salario = float(input('Informe o valor do salário do funcionário: '))
if salario >= 1250:
    aumento = (salario*0.10)+ salario
    print('Com o salário informado de R$: {}, você recebeu um aumento de 10% \n e seu salário atual agora é: {}'.format(salario,aumento))
else:
    aumento2 = (salario*0.15) + salario
    print('Com o salário informado de R$: {}, você recebeu um aumento de 15% \n e seu salário atual agora é: {}'.format(salario,aumento2))
    