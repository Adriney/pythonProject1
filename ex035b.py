#Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.(r1,r2,r3)
print("-="*20)
print("\033[35mAnalisador de Triângulos\033[m")
print("-=-"*20)
r1 = float(input("Primeiro segmento :"))
r2 = float(input("Segundo segmento :"))
r3 = float(input("Terceiro segmento :"))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("os segmentos acima \033[32mPODEM FORMAR\033[m triângulo!")
else:
    print("os segmentos acima \033[31mNÃO PODEM FORMAR\033[m triângulo!")