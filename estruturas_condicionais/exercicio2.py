porcentagem = int(input("Qual foi percentual de crescimento de produção da empresa: "))

if porcentagem > 0:
    print("Houve crescimento.")
elif porcentagem == 0:
    print("Não houve nem crescimento nem decrescimento")
else:
    print("Houve decrescimento.")