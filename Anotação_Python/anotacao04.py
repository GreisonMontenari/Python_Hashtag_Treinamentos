""" F-string e mudança de tipos e variáveis """

faturamento = 1000
custo = 400

lucro = faturamento - custo

# com format
print('O faturamento foi de {} e o lucro de {}'.format(faturamento, lucro))

# com f-string
print(f'O faturamento foi de {faturamento} e o lucro de {lucro}')

# Não tem diferença usando format ou f-string, aí é questão de qual você prefere usar, pois o resultado da no mesmo
