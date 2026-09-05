# Escreva um programa que converta uma temperatura digitada em °C e converta para °F. 
# A fórmula da conversão é: F = (9 * C) / 5 + 32

c = float (input('Informe a temperatura em °C:  '))
f = (9 * c) / 5 + 32
print(f'A temperatura de {c:.1f}°C corresponde a {f:.1f}°F')    