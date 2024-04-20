#Elabore um programa que calcule o valor a ser
# pago por um produto, considerando o seu preço
# normal e condição de pagamento:
# - À vista, dinheiro/cheque:10% de desconto
# - À vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
valor = int(input("Qual o valor do produto R$:"))
print("condição de pagamento:\033[36m\n (1) À vista, dinheiro/cheque,\n (2) À vista no cartão,"
     "\n(3) em até 2x no cartão,\n (4) 3x ou mais no cartão:\033[m ")
condição = int(input("Qual a forma de pagamento :"))

v1 = valor - (valor * 10/100)
v2 = valor - (valor * 5/100)
v3 = valor + (valor * 20/100)
if condição == 2:
    print("O valor do produto R${} á vista no cartão com 5% de desconto fica R${} !".format(valor, v2))
elif condição == 1 :
    print("O valor do produto R${} á vista no dinheiro/cheque com 10% de desconto fica R${} !".format(valor,v1))
elif condição == 3:
    print("O valor do produto R${} á prazo no cartão com 20% de juros fica R${} !".format(valor, v3))
elif condição == 4:
    print("O valor do produto R${} não tem alteração do valor na opção selecionada! ".format(valor))
else:
    print("Não foi identificado a forma de pagamento")

