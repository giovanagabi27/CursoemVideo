#crie um programa que leia um número, real qualquer pelo teclado e mostre na tela a sua porção inteira.
# exemplo digite o número 6.127 e o programa vai mostrar apenas 6.

from math import trunc
n = float(input('Digite um número real: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, trunc(n)))



