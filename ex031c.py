#Desenvolva um programa que pergunte a distância de uma
# viagem em km. Calcule o preço da passagem, cobrando
# R$0,50 por km para viagem de até 200km e R$0,45 para
# viagens mais longas.
distância = float(input("qual é a distância da sua viagem? "))
print("Você está prestes a começar uma viagem de {}KM.".format(distância))
preço = distância * 0.50 if distância <=200 else distância *0.45
print("E o preço da sua passagem será de \033[31mR${:.2f}".format(preço))