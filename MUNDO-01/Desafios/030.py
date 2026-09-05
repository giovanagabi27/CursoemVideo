# crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou ÍMPAR 

 
print('Vamos descobrir se o número é par ou ímpar!')
numero = int(input('Digite um número inteiro:'))
if numero % 2 == 0:
    print('O número {} é PAR!'.format(numero))
else:
    print('O número {} é ÍMPAR!'.format(numero))
