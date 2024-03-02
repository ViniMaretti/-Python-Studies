meta_funcionario = 2000
meta_loja = 5000
bonusFunc = 0
vendasFunc = float(input("Digite aqui as suas vendas"))
vendasLoja = float(input("Digite aqui a quatidade de vendas total da empresa"))

if vendasFunc > meta_funcionario and vendasLoja > meta_loja:
    bonusFunc = vendasFunc * 0.03
    print(f"Parabéns, você ganhou {bonusFunc} de bônus, pois tanto você quanto a loja bateram a meta de vendas")
else:
    bonusFunc = 0
    print("O funcionario não ganhou bonus, pois a loja ou o funcionario não bateram a meta")