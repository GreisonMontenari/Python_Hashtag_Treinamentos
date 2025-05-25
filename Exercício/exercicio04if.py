""" Exercícios com if
Cálculo de bônus: Crie um programa que calcule e dê um print no bônus que os funcionários devem receber segundo a regra:

A meta é 1000 vendas.
Se o valor de vendas for maior ou igual a meta, o valor do bônus do funcionário é 10% do valor de vendas. Caso contrário o valor de bônus do funcionário é 0. Print o bônus dos 3 funcionários. """

vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

if vendas_funcionario1 >= 1000:
    print('O funcionário 1 ganhou {}. de bônus'.format(vendas_funcionario1 * 0.1))

if vendas_funcionario2 >= 1000:
    bonus = vendas_funcionario2 * 0.1
else:
    bonus = 0
print('O funcionário 2 ganhou {} de bônus'.format(bonus))

if vendas_funcionario3 >= 1000:
    bonus = vendas_funcionario3 * 0.1
else:
    bonus = 0 
print('O funcionário 3 ganhou {} de bônus'.format(bonus))        
