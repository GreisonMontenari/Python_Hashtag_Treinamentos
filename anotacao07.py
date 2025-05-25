""" Tratando a condição falsa:
Quando usamos o if, nem sempre queremos apenas analisar o caso verdadeiro, em boa parte das veses queremos fazer alguma coisa caso a condição seja verdadeira e fazer outra coisa caso a condição seja falsa.

Nesse caso queremos:
if condição:
    o que eu quero fazer caso a condição seja verdadeira
else:
    o que eu quero fazer caso a condição seja falsa
          
Voltando ao exemplo da Amazon e do Iphone, agora nosso programa deve avisar nos 2 casos:
- Caso o produto tenha batido a meta, devemos exibir a mensagem: 'Batemos a meta de vendas de Iphone, vendemos {} unidade
- Se ele não bateu a meta do mês, devemos exibir a mensagem: 'Infelizmente não batemos a meta, vendemos {} unidades A meta era de {} unidades"""

meta = 50.000
qtde_vendas = 5.3000

if qtde_vendas > meta:
    print('Batemos a meta de vendas de Iphone, vendemos {} unidades'.format(qtde_vendas))
else:
    print('Infelizmente não batemos a meta, vendemos {} unidades. A meta era de {} unidades'.format(qtde_vendas, meta))    