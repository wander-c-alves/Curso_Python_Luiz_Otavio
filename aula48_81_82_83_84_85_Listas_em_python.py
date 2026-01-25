"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
    
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
    
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)


del lista[2]                - Deleta um item da lista
lista.append(60)            - Adiciona um item a sua lista
lista.pop()                 - Deleta o ultimo item da sua lista ou o item informado, (2) por exemplo.
lista.clear()               - Limpa a lista
lista.insert(0, 5)          - Adiciona um item informando o indice e o elemento a ser incluido na lista
lista_a.extend(lista_b)     - Junta a lista a com a lista b
lista_c = lista_a + lista_b - Concatena a lista a com  lista b em uma nova lista c

"""
#        +01234
#        -54321
# string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))
#        0    1      2              3    4
#       -5   -4     -3             -2   -1
# lista = [123, True, 'Luiz Otávio',  1.2, []]
# lista[-3] = 'Maria'
# print(lista)
# print(lista[2], type(lista[2]))


#        0   1   2   3   4   5
# lista = [10, 20, 30, 40]
# # lista[2] = 300
# # del lista[2]
# # print(lista)
# # print(lista[2])
# lista.append(50)
# lista.pop()
# lista.append(60)
# lista.append(70)
# ultimo_valor = lista.pop(3)
# print(lista, 'Removido,', ultimo_valor)


# #        0   1   2   3
# lista = [10, 20, 30, 40]
# lista.append('Luiz')
# nome = lista.pop()
# lista.append(1233)
# del lista[-1]
# # lista.clear()
# lista.insert(100, 5)
# print(lista[4])


# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b
# lista_a.extend(lista_b)
# print(lista_a)


# lista_a= [2, 4, 6 , 8]
# lista_b= [10, 12, 14 ,16]
# del lista_a[0]
# lista_a.insert(0, 2)
# print(lista_a)


"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)