#Faça um algorito que leia o salário e mostre seu, com 15% de aumento.
salário = float(input("qual é o salário do Funcionário? R$"))
novo = salário + (salário * 15 / 100)
print("Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(salário,novo))