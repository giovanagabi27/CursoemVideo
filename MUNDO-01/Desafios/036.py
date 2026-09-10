'''Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa .
    O  programa vai perguntar o valor da casa , o sálario do comprador e em qauntos anos ele vai pagar.
calcule o valor da prestação mensal m sabendo queela não pode exercer 30% do salário ou então o empréstimo será negado. '''

import math 
nome = 'Financiamento Habitacional'
cores = {'limpa':'\033[m',
        'azul':'\033[34m', 
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;30m'}
print(' {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))

print('====' * 20)

nome = str(input('Digite seu nome:'))
valor_imovel = int(input('Digite o Valor do Imovel R$ '))
salario = int(input('Digite o valor do seu salário R$ '))
ano = int(input('Digite quantos anos você pretende pagar :  '))
meses = ano * 12
pretencao = valor_imovel / (ano * 12)
limite = salario * 0.30 

print('==='*10)
print(f'Valor do imóvel: R${valor_imovel:.2f}')
print(f'Prazo: {ano:.0f} anos')
print(f'Valor da prestação: R${pretencao:.2f}')
print(f'Limite de 30% do salário: R${limite:.2f}')
print ('===' * 20)

if pretencao <= limite:
    print(f'{nome}\nEmprestimo\033[30;42mAPROVADO!\033[0;0;0m')
else:
    print(f'{nome}\n\033[0;30;41mNEGADO!\033[0;0;0m')