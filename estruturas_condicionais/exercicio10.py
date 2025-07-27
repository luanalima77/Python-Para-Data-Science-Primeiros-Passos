def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero."


def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return f"{numero} é um número par."
    else:
        return f"{numero} é um número ímpar."


def verificar_decimal_ou_inteiro(numero):
    if numero == int(numero):
        return f"O número {numero} é inteiro."
    else:
        return f"O número {numero} é decimal."


def verificar_negativo_ou_positivo(numero):
    if numero < 0:
        return f"O número {numero} é negativo."
    else:
        return f"O número {numero} é positivo."



# Realiza a operação.
n1 = float(input("Por favor, digite um número: "))
n2 = float(input("Por favor, digite um número: "))

operacao = int(input("Por favor, escolha um dos números a seguir correspondente à operação que você deseja aplicar aos números que você digitou anteriormente:" + "\n" + "1. (+)   2. (-)   3. (*)   4.(/)" + "\n" + "Digite aqui: "))

match operacao:
    case 1:
        resultado_soma = somar(n1,n2)
        print(f"{n1} + {n2} = {resultado_soma}")
        print(verificar_par_ou_impar(resultado_soma))
        print(verificar_decimal_ou_inteiro(resultado_soma))
        print(verificar_negativo_ou_positivo(resultado_soma))

    case 2:
        resultado_subtracao = subtrair(n1, n2)
        print(f"{n1} - {n2} = {resultado_subtracao}")
        print(verificar_par_ou_impar(resultado_subtracao))
        print(verificar_decimal_ou_inteiro(resultado_subtracao))
        print(verificar_negativo_ou_positivo(resultado_subtracao))

    case 3:
        resultado_multiplicacao = multiplicar(n1, n2)
        print(f"{n1} * {n2} = {resultado_multiplicacao}")
        print(verificar_par_ou_impar(resultado_multiplicacao))
        print(verificar_decimal_ou_inteiro(resultado_multiplicacao))
        print(verificar_negativo_ou_positivo(resultado_multiplicacao))

    case 4:
        resultado_divisao = dividir(n1, n2)
        if isinstance(resultado_divisao, str):
            print(resultado_divisao)
        else:
            print(f"{n1} / {n2} = {resultado_divisao}")
            print(verificar_par_ou_impar(resultado_divisao))
            print(verificar_decimal_ou_inteiro(resultado_divisao))
            print(verificar_negativo_ou_positivo(resultado_divisao))
    case _:
        print("Operação inválida!")
    



