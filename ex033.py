#Faça um programa que leia três números e mostre qual
# é o maior e qual é o menor.
n1 = float(input("Digite um número:"))
n2 = float(input("Digite segundo número:"))
n3 = float(input("Digite o terceiro número:"))

maxi = max(n1,n2,n3)
mini = min(n1,n2,n3)

print("O maior número é {:.0f}!".format(maxi))
# :.0f arredonda o digito
print("O menor número  é {:.0f}!".format(mini))
