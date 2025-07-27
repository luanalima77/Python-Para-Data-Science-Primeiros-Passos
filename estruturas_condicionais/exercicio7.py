turno = input("Em qual turno você estuda (manhã, tarde ou noite)? ").lower()

if turno == "manha" or turno == "manhã":
    print("Bom dia!")
elif turno == "tarde":
    print("Boa tarde!")
elif turno == "noite":
    print("Boa noite!")
else:
    print("Valor inválido!")