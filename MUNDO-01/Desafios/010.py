#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar,
#  considerando a cotação do dólar como US$ 1,00 = r$ 5,20

n = float(input('Digite quanto dinheiro você tem na carteira: R$:'))
print('Com R${:.2f} você pode comprar US${:.2f}'.format(n, (n/5.20)))   
