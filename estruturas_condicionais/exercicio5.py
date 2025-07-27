preco_1 = float(input("Digite o preço do primeiro produto: "))
preco_2 = float(input("Digite o preço do segundo produto: "))
preco_3 = float(input("Digite o preço do terceiro produto: "))

if preco_1 > preco_2 and preco_1 > preco_3:
    if preco_2 < preco_3:
        print(f"{preco_1} é mais caro e {preco_2} é o mais barato.")
    else:
        print(f"{preco_1} é mais caro e {preco_3} é o mais barato.")
    
elif preco_2 > preco_1 and preco_2 > preco_3:
    if preco_1 < preco_3:
        print(f"{preco_2} é mais caro e {preco_1} é o mais barato.")
    else:
        print(f"{preco_2} é mais caro e {preco_3} é o mais barato.")

elif preco_3 > preco_2 and preco_3 > preco_1:
    if preco_2 < preco_1:
        print(f"{preco_3} é mais caro e {preco_2} é o mais barato.")
    else:
        print(f"{preco_3} é mais caro e {preco_1} é o mais barato.")