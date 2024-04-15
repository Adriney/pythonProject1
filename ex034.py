#Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores
# a R$1.125,00 calcule um aumento de 10%.
# Para inferiores ou iguais, o aumento é de 15%.
salário = float(input("Digite o valor do seu salário R$"))
#base = 1126
aum1 = 0.10
aum2 = 0.15
ns1 = salário *(1 + aum1)
ns2 = salário *(1 + aum2)
if salário >= 1126 :
    print("Seu  salário com 10% de aumento ficara em R${}".format(ns1))
else:
    print("Seu salário com aumento de 15%  ficara R${}".format(ns2))
