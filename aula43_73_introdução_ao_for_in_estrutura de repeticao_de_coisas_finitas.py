# texto = 'python'
# i=0
# tamanho_string = len(texto)
# while i < tamanho_string:
#     print(texto[i])
#     i+=1


    
# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')
#     repeticoes+=1
#     print(repeticoes)
#     print('Aquele laço acime pode ter repetiçoes infinmitas')


texto = 'python'
novo_texto = ''
for letra in texto:
    novo_texto+= f'*{letra}'
    print(letra)
print(novo_texto + '*')
    