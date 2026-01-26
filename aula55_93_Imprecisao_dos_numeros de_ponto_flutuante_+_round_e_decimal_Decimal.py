"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

# Mais usado

# numero_1 = 0.1
# numero_2 = 0.7
# numero_3 = numero_1 + numero_2
# print(numero_3)
# print(f'{numero_3:.2f}')


#Usar o import quando precisar de precisão nos float ex: 2.46464684654564654564564654

import decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')

