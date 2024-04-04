#criar um algiritmo que leia um numero e mostre o seu dobro,
# triplo e a raiz quadrada.

n = int(input('Digite um número:'))
d = n * 2
t = n * 3
ra = n ** 0.5 # o correto é usar = n ** (1/2)
print('Você digitou : {}.\n seu dobro é : {}.\n seu triplo é : {}.\n e sua raiz-quadrada é : {:.2f}' .format(n, d, t, ra))
#:.2f significa 2 casas flutuantes

