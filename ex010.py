#Crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos dólares ela pode comprar
# (considere US$1,00=R$3,27)
real = float(input("quantos R$ você tem ?  R$"))
dolar = real / 3.27
print("Com \033[34mR${}\033[m você consegue comprar \033[36mUS${:.2f}  ".format(real, dolar))