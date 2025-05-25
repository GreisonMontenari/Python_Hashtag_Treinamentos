""" Crie um programa que imprima (print) os principais indicadores da loja Hashtah&Drink no último ano. Obs: faça tudo usando vairávies. 
Valores do último ano:

Quantidade de Vendas de Coca = 150
Quantidade de Vendas de Pepsi = 130
Preço Unitário da Coca = 1,50
Preço Unitário da Pepsi = 1,50
Custo da Loja: 2.500,00 """

qtd_coca = 150
preco_coca = 1.50

qtd_pepsi = 130
preco_pepsi = 1.50

custo = 2500

input('Qual foi o faturamento de Coca da loja?')
print(qtd_coca * preco_coca)

input('Qual foi o faturamento da Pepsi na loja?')
print(qtd_pepsi * preco_pepsi)

faturamento = qtd_coca * preco_coca + preco_pepsi * preco_pepsi

print('Qual foi o lucro da loja?')
print(faturamento - custo)

input('Qual foi a margem da loja?')
print(custo / faturamento)
