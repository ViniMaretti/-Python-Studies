meta = 0.05
taxa = 0
qtdFundo = float(input("Qual a quantidade de fundo entregue esse ano ?"))

if qtdFundo > meta:
    if qtdFundo > 0.20:
        taxa = 0.04
        print("A taxa foi de {} ".format(taxa))
    else:
        taxa = 0.05
        print("A taxa foi de {} ".format(taxa))
else:
    taxa = 0
    print("Não foi cobrado taxa, pois o fundo não atingiu a meta")