meta = 1000
i=0;
bonus = 0
vendas1 = float(input(f"Qual a quantidade de vendas que o funcionario {i+1} fez ?"))
vendas2 = float(input(f"Qual a quantidade de vendas que o funcionario {i+2} fez ?"))
vendas3 = float(input(f"Qual a quantidade de vendas que o funcionario {i+3} fez ?"))

if vendas1  >= meta:
    funcionario1 = vendas1 * 0.1
    print(f"O funcionario 1 ganhou {funcionario1} de bonus")
else:
    print("Funcionario 1 não ganhou bonus pois não atingiu a meta")
    
if vendas2  >= meta:
    funcionario2 = venda2s * 0.1
    print(f"O funcionario 2 ganhou {funcionario2} de bonus")
else:
    print("Funcionario 2 não ganhou bonus pois não atingiu a meta")

if vendas3  >= meta:
    funcionario3 = vendas3 * 0.1
    print(f"O funcionario 3 ganhou {funcionario3} de bonus")
else:
    print("Funcionario 3 não ganhou bonus pois não atingiu a meta")