#Escreva um programa que pergunte a quantidade de km percorridos
# por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo qua o
# carro custa R$60  por dia e R$0,15 por km rodado.
dias = float(input("Quantos dias :"))
dia = dias * 60
km = float(input("Qual o km:"))
kms = km * 0.15
tot = kms + dia
print("Valor dos dias locados R${:.2f}".format(dia))
print("Valor por km rodado R${:.2f}".format(kms))
print("Valor total dos dias locados mais o km rodado foi de R${:.2f}".format(tot))
