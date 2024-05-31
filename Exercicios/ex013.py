salario = float(input('Qual o salário do Funcionário?R$'))
aumento = 15
reajuste = salario*(100+15)/100

print('Um funcionário que ganhava R${:.2f}, com {:.2f}% de aumento, passa a receber R${:.2f}.'.format(salario,aumento,reajuste))