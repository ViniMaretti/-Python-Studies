metaVendas = 50.000
qtdVendas = float(input('Digite a quantidade de vendas do iphone'))

if qtdVendas >= metaVendas:
    print("A empresa vendeu {:.2f} e batemos a meta de vendas, parabéns".format(qtdVendas))
else:
    print("A empresa vendeu {:.2f} e por isso não bateu a meta esse mês, mais sorte na próxima".format(qtdVendas))