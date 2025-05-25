""" Estrutura do if - Condições no Python
Digamos que você trabalha na Amazon ( que tem milhares, se não milhões de produtos) e está analisando o resultado de vendas dos produtos. 

Você precisa criar um programaque vai analisar o resultado de vendas dos produtos da Amazon em um mês. Para simplificar vamos pensar em um único produto: IPHONE.

Meta de vendas do Iphone = 50.000 unidades
Quantidade de vendas no mês = 65.300 unidades

O seu programa deve avisar (usaremos o print por enquanto) caso o produto tenha batido a meta do mês. Então devemos fazer:
- Caso o produto tenha batido a meta, devemos exibir a mensagem: 'Batemos a meta de vendas de Iphone, vendemos {} unidade
- Se ele não bateu a meta do mês, o seu programa não deve fazer nada """

meta = 50.000
qtde_vendas = 65.300

if qtde_vendas > meta:
    print('Batemos a meta de vendas de Iphone, vendemos {} unidades'.format(qtde_vendas))
    print('Fim do programa')
