#Faça um programa que leia o peso de cinco pessoas.
# no final, mostre qual foi o maior e o menor peso lidos.
p1 = float(input("Qual o peso da 1° pessoa:"))
p2 = float(input("Qual o peso da 2° pessoa:"))
p3 = float(input("Qual o peso da 3° pessoa:"))
p4 = float(input("Qual o peso da 4° pessoa:"))
p5 = float(input("Qual o peso da 5° pessoa:"))

max_peso = max(p1,p2,p3,p4,p5)
min_peso = min(p1,p2,p3,p4,p5)

print("O \033[31m maior \033[m peso lido foi: {}Kg.  "
      "\nO \033[31m menor \033[m peso lido foi: {}Kg."
      " ".format(max_peso,min_peso))
