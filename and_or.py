meta_funcionario = 2000
meta_loja = 5000
bonusFunc = 0
vendasFunc = float(input("Digite aqui as suas vendas"))
vendasLoja = float(input("Digite aqui a quatidade de vendas total da empresa"))
metaNota = 9

nota = int(input("Qual a  nota você da pro seu funcionario ?"))
vendasFunc = float(input("Qual a quantidade de vendas que o funcionario fez esse mês ?"))

if nota >= metaNota or (vendasFunc > meta_funcionario and vendasLoja > meta_loja):
    bonus = vendasFunc * 0.03
    print(f"Parabéns, sua nota foi {nota}, e por isso você ganhou {bonus} de bônus")
else:
    print(f"infelizmente sua nota foi {nota}, e por isso você não ganhou bonificação")
    
    