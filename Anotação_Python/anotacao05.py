""" Mudança de tipo de variável """

faturamento = float(input('Insira o faturamento'))
custo = float(input('Insira o custo'))

print(type(faturamento))
print(type(custo))

lucro = faturamento - custo
print(lucro)

# str -> muda para string
# int -> muda para inteiro
# float -> muda para float
