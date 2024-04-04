#Faça um algorito que leia o o valor do produto,
# mostre com desconto 7.5% desconto avista,
# e com 5% de juros a prazo.
preço = float(input("Qual é o valor do produto? R$"))
avista = preço - (preço * 7.5 / 100)
prazo =  preço + (preço * 5 / 100)
print("O valor do produto é {}".format(preço))
print("O valor R${} avista é R${:.2f}".format(preço,avista))
print("O valor R${} a prazo fica R${:.2f}".format(preço, prazo))