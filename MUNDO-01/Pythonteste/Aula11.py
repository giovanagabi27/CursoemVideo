# CORES NO TERMINAL
# ANSI escape codes são sequências de caracteres que permitem controlar a formatação, 
# cor e estilo do texto exibido em terminais compatíveis. 
# Eles são amplamente utilizados em sistemas Unix/Linux e também podem ser usados em alguns terminais do Windows.
# \033[0;33;44M

#CORES 
# STYLE 
# 0 - None (NADA)
# 1 - Bold  (NEGRITO)
# 4 - Underline (Sublinhado)
# 7 - Negative (Inverte a cor do fundo e do texto)


## TEXT
# 30 - Branco
# 31 - Vermelho
# 32 - Verde
# 33 - Amarelo
# 34 - Azul
# 35 - Roxo
# 36 - Ciano
# 37 - Cinza

## BACKGROUND
# 40 - Branco
# 41 - Vermelho
# 42 - Verde
# 43 - Amarelo
# 44 - Azul
# 45 - Roxo
# 46 - Ciano
# 47 - Cinza

#teste 1 
'''
print('\033[0;30;41mOlá, Mundo!\033[0;0;0m') # fundo vermelho e cor branca
print('\033[4;33;44mOlá, Mundo!\033[0;0;0m') # fundo azul e cor amarela
print('\033[1;35;43mOlá, Mundo!\033[0;0;0m') # fundo amarelo e cor roxa
print('\033[30;42mOlá, Mundo!\033[0;0;0m') # fundo verde e cor branca
print('\033[1;30;45mOlá, Mundo!\033[0;0;0m') # fundo roxo e cor branca
print('\033[3;7;30mOlá, Mundo!\033[0;0;0m') # fundo branco e cor preta
'''

#teste 2
'''
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b)) # cor verde e vermelha
'''
#teste 3
nome = 'Giovana'
cores = {'limpa':'\033[m',
        'azul':'\033[34m', 
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa'])) # cor azul
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa'])) # cor amarela
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa'])) # cor preta e branca           
