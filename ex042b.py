#Refaça o DESAFIO 035 dos triângulos, acrescentando
# o recurso de que tipo de triângulo sera formado:
# - Equilátero:todos os lados iguais
# - Isósceles:dois lados iguais
# - Escaleno:todos os lados diferentes
r1 = float(input("Primeiro segmento :"))
r2 = float(input("Segundo segmento :"))
r3 = float(input("Terceiro segmento :"))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("os segmentos acima PODEM FORMAR um triângulo ", end='')
    if r1 == r2 == r3 :
        print("EQUILÁTERO")
    elif r1 != r2 != r3 != r1 :# !=  diferente
        print('ESCALENO')

    else:
        print('ISÓCELES')

else:
    print("os segmentos acima NÃO PODEM FORMAR triângulo!")
