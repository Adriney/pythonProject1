#Desenvolva um programa que pergunte a distância de uma
# viagem em km. Calcule o preço da passagem, cobrando
# R$0,50 por km para viagem de até 200km e R$0,45 para
# viagens mais longas.
km = int(input("Quantos KM:"))
if km <= 200:
    km1 = km * 0.5
    print("Uma viagem de {}KM custara R${}!".format(km, km1))
else:
    km2 = km * 0.45
    print("Uma viagem de {}KM custara R${}!".format(km,km2))