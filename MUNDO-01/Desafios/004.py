# Faça um programa que leia algo pela teclado 
# e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('Digite algo:')
print('O tipo primitivo desse valor é:', type(n))
print('Só tem espaços?', n.isspace())   # espaço normal do teclado
print('É um número?', n.isnumeric())     # numeros 1,2,3...
print('É alfabético?', n.isalpha())     # letras
print('É alfanumérico?', n.isalnum())   # letras e números
print('Está em maiúsculas?', n.isupper())   # letras MAIUSCULAS
print('Está em minúsculas?', n.islower())   # letras minusculas
print('Está capitalizada?', n.istitle())    # Letra inicial maiuscula e o resto minusculas
