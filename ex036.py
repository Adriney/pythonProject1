#Escreva um programa para aprovar um empréstimo bancário para
# a compra de uma casa. O programa vai perguntar o valor da
# casa, o salário do comprador, e em quantos anos ele vai
# pagar. Calule o valor da prestação mensal, sabendo que ele
# não pode exceder 30% do salário ou então o empréstimo será negado.
print("==="*11)
print("Empréstimo bancário(para imóvel)")
print("==="*11)
casa = float(input("Qual o valor da casa:"))
salario = float(input("Qual é o seu salário:"))
prazo1 = int(input("Em quantos anos pretende pagar:"))
prazo2 = prazo1 * 12
parcela = casa / prazo2
calc = salario -(salario * 70 /100)

if calc >= parcela:
    print("Na condição do salário de R${} com prazo de {} anos({} meses) "
          "\na parcela fica R${:.2f} e o Banco \033[31mAPROVOU\033[m seu emprestimo "
          "\npara aquisição de seu imovel! ".format(salario,prazo1,prazo2,parcela))
elif calc < parcela:
    print("Na condição do salário de R${} com prazo de {} anos({} meses) "
          "\na parcela fica R${:.2f} e o Banco \033[31mNEGOU\033[m seu emprestimo "
          "\n!".format(salario, prazo1, prazo2, parcela))
else:
    print("Não foi possivel identificar as condições necessarias para analise!")
print("Parcela máxima nessa condição é {}".format(calc))