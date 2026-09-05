# Desafio 017 - faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
#  calcule e mostre o comprimento da hipotenusa.


from math import hypot #hypot significa hipotenusa 
c1 = float(input('Digite o comprimento do cateto oposto:'))
c2 = float(input('Digite o comprimento do cateto adjacente:'))
print('O comprimento da hipotenusa vai medir {:.2f}'.format(hypot(c1,c2 )))

# ou nem todo programa tem o import de hypot, então podemos fazer assim:
# c1 = float(input('Digite o comprimento do cateto oposto:'))   
# c2 = float(input('Digite o comprimento do cateto adjacente:'))
# h = (c1 ** 2 + c2 ** 2) ** (1/2)  # ou h = (c1 ** 2 + c2 ** 2) ** 0.5
# print('O comprimento da hipotenusa vai medir {:.2f}'.format(h)) 

