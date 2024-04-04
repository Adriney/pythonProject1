#Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com  5% de desconto.
valor = int(input("Valor do produto: "))
desc = 0.05
valorf = valor * (1- desc)
print("O valor R${} com desconto de 5% ficara R${}".format(valor, valorf))