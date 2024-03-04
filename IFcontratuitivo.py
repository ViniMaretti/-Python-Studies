faturamento = input('Qual foi o faturamento da loja nesse mês?')
custo = input('Qual foi o custo da loja nesse mês?')

if faturamento and custo:
    lucro = int(faturamento) - int(custo)
    print(f"O lucro foi de {lucro}")
else:
    print("Preencha corretamente o faturamento ou lucro")