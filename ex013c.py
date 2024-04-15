#Faça um algorito que leia o o valor do produto,
# mostre com desconto 7.5% desconto avista,
# e com 5% de juros a prazo.
preço = float(input("Qual é o valor do produto? R$"))
avista = preço - (preço * 7.5 / 100)
prazo =  preço + (preço * 5 / 100)
print("O valor do produto é {}".format(preço))
print("O valor R${} \033[32mavista\033[m é R${:.2f}".format(preço,avista))
print("O valor R${} a \033[31mprazo\033[m fica R${:.2f}".format(preço, prazo))