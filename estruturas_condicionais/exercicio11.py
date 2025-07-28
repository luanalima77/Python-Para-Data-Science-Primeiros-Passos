lado_1 = float(input("Escreva uma valor para o primeiro lado do triângulo: "))
lado_2 = float(input("Escreva uma valor para o segundo lado do triângulo: "))
lado_3 = float(input("Escreva uma valor para o terceiro lado do triângulo: "))

def verificar_se_um_triangulo_existe(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return classificar_triangulo_com_base_nos_lados(a, b, c)
    else:
        return "O triângulo não existe."

def classificar_triangulo_com_base_nos_lados(a, b, c):
    if a == b and a == c:
        return "Triângulo equilátero"
    elif a == b or a == c or b == c:
        return "Triângulo isósceles"
    elif a != b and a != c:
        return "Triângulo escaleno"

print(verificar_se_um_triangulo_existe(lado_1, lado_2, lado_3))