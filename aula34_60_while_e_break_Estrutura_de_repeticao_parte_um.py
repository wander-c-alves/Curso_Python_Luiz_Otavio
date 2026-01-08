"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

#condicao = True
# while condicao:
#     nome = input('Qual o seu nome: ')
#     print(f'Seu nome é {nome}')

#     if nome == 'sair':
#         break
# print('Acabou')

# while True:
#     nome = input('Digite seu nome: ')
#     if nome.lower() == 'sair':
#         break
#     print(f'{nome}, seja bem vindo!')
# print('Até logo')

while True:
    nome = input('Digite seu nome: ')
    if nome.lower() == 'sair':
        break
    print(f'{nome}, seja bem vindo!')
print('Até logo')
