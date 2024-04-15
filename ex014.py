c = float(input("Informa a temperatura em °C: "))
f = 9 * c / 5 + 32
print("A temperatura de \033[31m{}°C\033[m corresponde a \033[31m{}ºF\033[m!".format(c,f))