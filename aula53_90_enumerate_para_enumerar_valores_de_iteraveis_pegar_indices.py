'''
enumerate - enumera iteraveis (indices)

'''

lista = ['Maria', 'Helena', 'Luiz']
lista.append('joao')

lista_enumerada = enumerate(lista)
for item in lista_enumerada:
    print(item)
    
    