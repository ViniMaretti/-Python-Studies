meta = 1000
VendasF1 = float(input("F1 Digite aqui a venda feita esse mês:"))
VendasF2 = float(input("F2 Digite aqui a venda feita esse mês:"))
VendasF3 = float(input("F3 Digite aqui a venda feita esse mês:"))

if VendasF1 >= 1000:
    if VendasF1 >= 2000:
        print(f"Funcionario1 ganhou {VendasF1 * 0.2} de bônus")
    else:
        print(f"Funcionario1 ganhou {VendasF1 * 0.1} de bônus")
else:
    print("Funcionario1 não ganhou bônus")
    
if VendasF2 >= 1000:
    if VendasF2 >= 2000:
        print(f"Funcionario2 ganhou {VendasF2 * 0.2} de bônus")
    else:
        print(f"Funcionario2 ganhou {VendasF2 * 0.1} de bônus")
else:
    print("Funcionario2 não ganhou bônus")
    
if VendasF3 >= 1000:
    if VendasF3 >= 2000:
        print(f"Funcionario3 ganhou {VendasF3 * 0.2} de bônus")
    else:
        print(f"Funcionario3 ganhou {VendasF3 * 0.1} de bônus")
else:
    print("Funcionario3 não ganhou bônus")


