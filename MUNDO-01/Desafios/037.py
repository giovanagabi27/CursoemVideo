'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a 
Base de conversão:
- 1 para Binário
- 2 para Octal
- 3 para Hexadecimal'''

import math

print('Vamos converter os números')
print('---' * 10 )

numero = int(input('Digite um número inteiro :'))
binario = bin(numero)
octal= oct(numero)
hexadecimal = hex(numero)

print('---' * 20)

print('Conversão para Binário: {}'.format(binario)) 
print('Conversão para Octal : {}'.format(octal))
print('Conversão para Hexadecimal : {}'.format(hexadecimal))