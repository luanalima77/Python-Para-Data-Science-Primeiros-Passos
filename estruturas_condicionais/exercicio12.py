combustivel = input("Qual é o tipo de combustível a ser usado?" + "\n" + "(e) etanol  (d) diesel" + "\n" + "Digite aqui a LETRA correspondente: ").upper()
quantidade_litros = float(input("Qual foi a quantidade de litros comprada pelo cliente? Digite aqui: "))

def verificar_desconto_para_o_cliente(combustivel, litros_comprados_pelo_cliente):
    preco_por_litro_do_etanol = 1.7
    preco_por_litro_do_diesel = 2

    if combustivel == "E" and litros_comprados_pelo_cliente <= 15:
        desconto_por_litro = 0.2
        valor_final_da_compra = preco_por_litro_do_etanol * litros_comprados_pelo_cliente * desconto_por_litro
        return f"Combustível escolhido pelo cliente: etanol\nQuantidade de litros comprada pelo cliente: {litros_comprados_pelo_cliente:.2f} litros\nTotal a ser pago pelo cliente: {valor_final_da_compra:.2f} reais"
    elif combustivel == "E" and litros_comprados_pelo_cliente > 15:
        desconto_por_litro = 0.4
        valor_final_da_compra = preco_por_litro_do_etanol * litros_comprados_pelo_cliente * desconto_por_litro
        return f"Combustível escolhido pelo cliente: etanol\nQuantidade de litros comprada pelo cliente: {litros_comprados_pelo_cliente:.2f} litros\nTotal a ser pago pelo cliente: {valor_final_da_compra:.2f} reais"
    elif combustivel == "D" and litros_comprados_pelo_cliente <= 15:
        desconto_por_litro = 0.3
        valor_final_da_compra = preco_por_litro_do_diesel * litros_comprados_pelo_cliente * desconto_por_litro
        return f"Combustível escolhido pelo cliente: diesel\nQuantidade de litros comprada pelo cliente: {litros_comprados_pelo_cliente:.2f} litros\nTotal a ser pago pelo cliente: {valor_final_da_compra:.2f} reais"
    elif combustivel == "D" and litros_comprados_pelo_cliente > 15:
        desconto_por_litro = 0.5
        valor_final_da_compra = preco_por_litro_do_diesel * litros_comprados_pelo_cliente * desconto_por_litro
        return f"Combustível escolhido pelo cliente: diesel\nQuantidade de litros comprada pelo cliente: {litros_comprados_pelo_cliente:.2f} litros\nTotal a ser pago pelo cliente: {valor_final_da_compra:.2f} reais"
    else:
        return "Valores inválidos."
    
print(verificar_desconto_para_o_cliente(combustivel, quantidade_litros))
