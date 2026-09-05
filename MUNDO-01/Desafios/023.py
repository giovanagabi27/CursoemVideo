#Crie um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# exemplo: Digite um número: 1834
# unidade: 4    
# dezena: 3
# centena: 8
# milhar: 1

n = int(input('Digite um número de 0 a 9999: '))
unidade = n // 1 % 10
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10
print(f'Analisando o número {n}...')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')  
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
