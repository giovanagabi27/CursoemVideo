#Faça um progama que leia um número e mostre na tela o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número:'))
print('O número digitado foi:{}\nseu dobro é {}\nseu triplo é {}\nsua raiz quadrada é {:.2f}'.format(n, (n*2), (n*3), (n**(1/2)))) 


#{:.2f} - formata o número para duas casas decimais
# \n - quebra de linha
