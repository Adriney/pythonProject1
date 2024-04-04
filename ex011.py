#Faça um rograma que leia a largura e a altura de uma
# parede em metros, calcule a sua área e a quantidade
# de tita necessária para pintá-la, sabendo que cada
# litro de tinta, pinta uma área de 2m².
larg = float(input("Qual é a largura da parede:  "))
alt = float(input("Qual é a altura da parede:  "))
mt4 = larg * alt
quant = mt4 * 0.5
print("com {} metros de largura  mais {} metros de altura serão = {}M² e sera necessario {} litros de tinta.".format(larg, alt, mt4, quant))