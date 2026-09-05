# escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento. 
# Para salarios superiores a R$1250,00,
#  calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

funcionario = str(input('Digite o nome do funcionário: '))
salario = float(input('Digite o salário do funcionário: R$'))   
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('O funcionário {} tinha um salário de R${:.2f} e com o aumento passará a receber R${:.2f}'.format(funcionario, salario, novo))
    

