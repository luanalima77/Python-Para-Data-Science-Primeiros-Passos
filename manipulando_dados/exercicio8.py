numerador = int(input("Insira o numerador: "))
denominador = int(input("Insira o denominador: "))

if denominador != 0:
    print(f"{numerador}/{denominador} = {int(numerador/denominador)}")

while denominador == 0:
    print("O denominador deve ser diferente de 0.")
    denominador = int(input("Digite um valor diferente de zero para o denominador: "))
    print(f"{numerador}/{denominador} = {int(numerador/denominador)}")
