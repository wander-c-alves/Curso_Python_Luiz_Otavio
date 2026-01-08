# digite um nome e faça ele ficar conforme abaixo:
# *w*a*n*d*e*r*

# nome = input('Digite seu nome: ')

# indice = 0
# novo_nome = ''

# while indice < len(nome):
#     letra = nome[indice]  
#     novo_nome += f'*{letra}'
#     indice += 1

# novo_nome += '*'
# print(novo_nome)


nome = input('Digite seu nome: ')
indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice+=1
novo_nome+="*"
print(novo_nome)
    