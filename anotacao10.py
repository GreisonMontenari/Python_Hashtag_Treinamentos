""" Casos com várias condições/comparações
Estrutura: Quando temos várias comparações, ao invés de criar if dentro do if podemos usar os operadores "and" e "or" para tratar esssas condições.

if condicao_1 and condicao_2:
      vai ser executado se as 2 condições forem verdadeiras ao mesmo tempo
        
outro caso:
if condicao_1 or condicao_2:
                vai ser executado se pelo menos uma das condiçoes forem verdadeiras
                            
EXEMPLO: Cálculo de meta de vendas dos funcionários. Muitas empresas atribuem bonificação do salário dos funcionários de acordo com o resultado do funcinário e também com o resultado da empresa como um todo.

Nesse caso, a regra funciona da seguinte forma:
- Se o funcionário vendeu mais do que a meta de vendas e a loja bateu a meta de vendas da loja, o funcionário ganha 3% do que ele vendeu em forma de bônus.

- Caso o funcionário tenha batido a meta de vendas individual dele, mas a loja não tenha batido a meta de vendas da loja como um todo, o funcionário não ganha bônus"""

meta_funcionario = 10000
meta_loja = 250000
vendas_funcionario = 15000
vendas_loja = 200000

if vendas_funcionario > meta_funcionario and vendas_loja > meta_loja:
    bonus = 0.03 * vendas_funcionario
    print('Bônus do funcinário foi de {}'.format(bonus))
else:
    print('Funcionário não ganhou bônus')    