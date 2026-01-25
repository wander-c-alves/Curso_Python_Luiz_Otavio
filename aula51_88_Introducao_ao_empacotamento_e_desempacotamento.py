
nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes
print(nome2)

nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
print(nome1)


nome1, *resto = ['Maria', 'Helena', 'Luiz']
print(nome1, resto)

nome1, *_ = ['Maria', 'Helena', 'Luiz']
print(nome1)

_, nome2, *_ = ['Maria', 'Helena', 'Luiz']
print(nome2)

_, _, nome3, *_ = ['Maria', 'Helena', 'Luiz']
print(nome3)