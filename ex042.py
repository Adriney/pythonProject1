#Refaça o DESAFIO 035 dos triângulos, acrescentando
# o recurso de que tipo de triângulo sera formado:
# - Equilátero:todos os lados iguais
# - Isósceles:dois lados iguais
# - Escaleno:todos os lados diferentes
print("-="*20)
print("Analisador de Triângulos")
print("-=-"*20)
r1 = float(input("Primeiro segmento :"))
r2 = float(input("Segundo segmento :"))
r3 = float(input("Terceiro segmento :"))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3 :
        tipo = "Equilatero"
    elif r1 == r2 or r2 == r3 or r1 == r3:
        tipo ="Isóceles"
    else:
        tipo = "Escaleno"
    print("os segmentos acima PODEM FORMAR um triângulo {}!".format(tipo))
else:
    print("os segmentos acima NÃO PODEM FORMAR triângulo!")