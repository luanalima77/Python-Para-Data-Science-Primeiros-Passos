valor_1 = 35500
valor_2 = 40000
valor_3 = 50600.50

if valor_1 > valor_2 and valor_1 > valor_3:
    if valor_2 < valor_3:
        print(f"{valor_1} é mais alto e {valor_2} é o mais baixo.")
    else:
        print(f"{valor_1} é mais alto e {valor_3} é o mais baixo.")
    
elif valor_2 > valor_1 and valor_2 > valor_3:
    if valor_1 < valor_3:
        print(f"{valor_2} é mais alto e {valor_1} é o mais baixo.")
    else:
        print(f"{valor_2} é mais alto e {valor_3} é o mais baixo.")

elif valor_3 > valor_2 and valor_3 > valor_1:
    if valor_2 < valor_1:
        print(f"{valor_3} é mais alto e {valor_2} é o mais baixo.")
    else:
        print(f"{valor_3} é mais alto e {valor_1} é o mais baixo.")
