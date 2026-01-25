"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# primeira solução:
# numero = input('Digite um numero inteiro: ')
# try:
#     numero = int(numero)
#     if numero %2 == 0:
#         print(f'O numero{numero} é par')
#     else:
#         print(f'O numero {numero} é impar')
# except:
#     print('Você não digitou um numero inteiro')


   # outra solução:
#entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


# hora = input('Que horas são: ')
# try:
#     hora = int(hora)
#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora <= 17:
#         print('Boa tarde')
#     elif hora <= 23:
#         print('Boa noite')
#     else:
#         print('Não conheço essa hora')
# except:
#     print('Você não digitou um numero inteiro')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input('Digite seu primeiro nome: ')
primeiro_nome = len(primeiro_nome)

if primeiro_nome >1:
    if primeiro_nome <= 4:
        print('nome curto')
    elif primeiro_nome > 6:
        print('Seu nome é muito grande')
    else:
        print('Seu nome é normal')
else:
    print('Digite mais de uma letra')