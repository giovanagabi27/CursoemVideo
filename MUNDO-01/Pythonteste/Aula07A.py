# Operações Aritméticas
# + Adição                   
# - Subtração   
# * Multiplicação
# / Divisão 
# // Divisão Inteira
# ** Potência   
# % Resto da Divisão 

# Operadores 
# 5 + 2 == 7 (número mais outro número)
# 5 - 2 == 3 (número menos outro número)
# 5 * 2 == 10 (número vezes outro número)
# 5 / 2 == 2.5 (número dividido por outro número)
# 5 // 2 == 2 (divisão inteira)
# 5 ** 2 == 25  (número elevado a outro número)
# 5 % 2 == 1 (resto da divisão)


#Ordem de Precedência
# 1º () (parênteses) 
# 2º ** (potência)
# 3º * / // % (multiplicação, divisão, divisão inteira e resto da divisão)
# 4º + - (adição e subtração)

# 5 + 3 * 2 == 11 (primeiro a multiplicação e depois a adição)
# 3 * 5 + 4 ** 2 == 31 (primeiro a potência, depois a multiplicação e por último a adição)
# 3 * (5 + 4) ** 2 == 243 (primeiro o que está dentro do parênteses,
#  depois a potência e por último a multiplicação)

n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2 
print('A soma é {},\n o produto é {} e a\n divisão é {:.3f}'.format(s, m, d), end='')
print(' \n Divisão inteira {} \n potência {} '.format(di, e))