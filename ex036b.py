#Escreva um programa para aprovar um empréstimo bancário para
# a compra de uma casa. O programa vai perguntar o valor da
# casa, o salário do comprador, e em quantos anos ele vai
# pagar. Calule o valor da prestação mensal, sabendo que ele
# não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input("Valor da casa : R$"))
salário = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento? "))
prestação = casa/ (anos * 12)
mínimo = salário * 30 / 100
print("para pagar uma casa de R${:.2f} em {} anos".format(casa, anos),end='')
print(" a prestação será de {:.2f}".format(prestação))
if prestação <= mínimo:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")