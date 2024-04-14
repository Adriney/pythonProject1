#Faça um programa que leia um ano qualquer e
# mostre se ela é BISSEXTO.

ano = int(input("Digite um ano:"))
def is_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False
if is_bissexto(ano):
    print("O ano {} é Bissexto".format(ano))
else:
    print("O ano {} não é Bissexto".format(ano))
    
    