#Escreva um programa que leia um valor em metros
# e o exiba convertido em centimetros e milímetros.

me = float(input('Quantos metros ?'))
ce = me * 100
mi = me * 1000
print('    {}, metros são {:.0f} centimetros, e {:.0f} milímetros.'.format(me, ce, mi))