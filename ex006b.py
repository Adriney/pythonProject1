#criar um algiritmo que leia um número e mostre o seu dobro,
# triplo e a raiz quadrada.

n = int(input('Digite um número:'))
print('Você digitou : {}.\n seu dobro é : {}.\n seu triplo é : {}.\n e sua raiz-quadrada é : {:.2f}' .format(n, (n*2), (n*3), (n**(1/2))))
#:.2f significa 2 casas flutuantes

