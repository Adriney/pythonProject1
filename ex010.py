#Crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos dólares ela pode comprar
# (considere US$1,00=R$3,27)
real = float(input("quantos R$ você tem ? "))
dol = real / 3.27
print("com R${} você consegue comprar US${}  ".format(real, dol))