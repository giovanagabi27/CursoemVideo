#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# exemplo: Digite seu nome completo: Ana Maria de Souza
# primeiro nome: Ana    
# último nome: Souza

nome = str(input('Digite seu nome completo: ')).strip()
print(f'Primeiro nome: {nome.split()[0]}')
print(f'Último nome: {nome.split()[-1]}')
