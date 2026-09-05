#desenvolva um programa que pergunte a distância de uma viagem em km e a velocidade média esperada para a viagem. 
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.


distancia = float(input('Qual é a distância da viagem em km? '))
velocidade_media = float(input('Qual é a velocidade média esperada para a viagem? '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da passagem será de R${:.2f}'.format(preco))
