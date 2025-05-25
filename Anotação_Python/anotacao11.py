""" Outro exemplo
Agora vamos levar essa análise mais a fundo. 
Nessa empresa, existe um outro caso também que garante que o funcinário ganhe um bônus, independenete das vendas que ele fez naquele mês.

Todo mês os diretores da empresa fazem uma avaliação qualitativa de todos os funcionários. Nessa avaliação os diretos dão uma nota de 0 a 10 para cada funcionário. Se a nota do funcionário for 9 ou 10, ele também ganha o bônus de 3% do valor de vendas. (os bônus não sao acumulativos) """

meta_funcionario = 10000
meta_loja = 250000
vendas_funcionario = 15000
vendas_loja = 200000

if vendas_funcionario > meta_funcionario and vendas_loja > meta_loja:
    bonus = 0.03 * vendas_funcionario
    print('Bônus do funcinário foi de {}'.format(bonus))
else:
    print('Funcionário não ganhou bônus')  

nota_funcionario = 9
meta_nota = 9

if nota_funcionario >= meta_nota or (vendas_funcionario > meta_funcionario and vendas_loja > meta_loja):
    bonus = 0.03 * vendas_funcionario
    print('Bônus do funcionário foi de {}'.format(bonus))
else:
    print('Funcionário não ganhou o bônus')    
