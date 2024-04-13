#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$7,00 por
# cada km acima do limite.
vel = int(input("Qual a velocidade:" ))
if vel <= 80.00:
    print("Velocidae dentro do limite estabelecido")
else:
    v2 = vel-80
    v3 = v2 * 7
    print("Voce está {}km acima do limite de velocidade e será multado em R${}.00!".format(v2, v3))