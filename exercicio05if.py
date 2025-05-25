""" Cálculo de bônus com uma nova regra
- Crie um novo código que calcule e dê print do bônus dos funcionários novamente. Porém há uma nova regra nesse caso 2:
A meta é 1000 vendas
Agora, os funcionários que venderem muito acima da meta ganham mais bônus do que os outros. Então o bônus é definido da seguinte forma:
- Se vendas funcionário for maior ou igual a 2000, então o bônus é de 15% sobre o valor de vendas.

- Se vendas funcionários for menos do que 2000 e maior ou igual a 1000, então o bônus é de 10% sobre o valor de vendas.

- Se vendas funcionário for menos do que 1000 então o bônus do funcionário é de 0.
Use as mesmas variáveis de vendas_funcionários """ 

if vendas_funcionario1 >= 1000:  # type: ignore
    if vendas_funcionario1 >= 2000: # type: ignore
        bonus = 0.15 * vendas_funcionario1 # type: ignore
    else:
        bonus = 0.1 * vendas_funcionario1  # type: ignore
else:
    bonus = 0
print('O funcionário 1 ganhou {} de bônus'.format(vendas_funcionario1 * 0.1))                 # type: ignore
    
if vendas_funcionario2 >= 1000: # type: ignore
    bonus = vendas_funcionario2 * 0.1 # type: ignore
else:
    bonus = 0
print('O funcionário 2 ganhou {} de bônus'.format(bonus))

if vendas_funcionario3 >= 1000: # type: ignore
    bonus = vendas_funcionario3 * 0.1 # type: ignore
else:
    bonus = 0
print('O funcionário 3 ganhou {} de bônus'.format(bonus))        