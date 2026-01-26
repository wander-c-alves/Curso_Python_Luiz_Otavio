# Iterável -> str, range, etc (__iter__)
# Iterador -> Quem sabe entregar um valor por vez
# next -> Me entregue o próximo valor
# iter -> Me entregue seu iterador

# texto = 'wander'.__iter__()
texto = iter('wander') # __iter()

# print(texto)


print(next(texto))
print(texto.__next__())

