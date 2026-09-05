#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
n = int(input('Digite um número inteiro:'))
print('A tabuada do número {} é:'.format(n))
for c in range(1, 11):                          
    print('{} x {} = {}'.format(n, c, (n*c)))

    

   # For significa "para" e é usado para criar um loop que itera sobre uma sequência de valores.
   # A função range() é usada para gerar uma sequência de números, que pode ser usada para controlar o loop.
   # in significa "em" e é usado para verificar se um valor está presente em uma sequência ou coleção.
 