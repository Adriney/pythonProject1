#Desenvolva um programa que leia as duas notas de um aluno,
# calcule a média.
n1 = float(input('Digite a primeira nota :'))
n2 = float(input('Digite a segunda nota :'))
m = (n1 + n2)/2
print('A média entre as duas notas é {:.1f}'.format(m))
#:.1f  =>uma casa decimal após o ponto
