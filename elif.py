meta = 20000
vendas = float(input("Qual o seu valor de vendas desse mês ?"))
bonus = 0

if vendas < meta:
    print("Você não ganhou bonus")
elif vendas > (meta * 2):
    bonus  = vendas * 0.07 
    print(f"Você ganhou bônus de {bonus}")
else:
    bonus = vendas * 0.03
    print(f"Você ganhou bônus de {bonus:.2f}")