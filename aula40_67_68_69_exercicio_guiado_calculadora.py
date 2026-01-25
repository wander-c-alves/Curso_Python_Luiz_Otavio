''' Calculadora com while'''
while True:
    numero1 = input('Digite o Primeiro número: ')
    operador = input('Digite um operador (+-*/): ')
    numero2 = input('Digite o Segundo número: ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(numero1)
        num_2_float = float(numero2)
        numeros_validos = True
    
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos numeros digitados são invalidos.')  
        continue

    operadores_permitidos = '+-*/'

    # if len(operador) != 1 or operador not in operadores_permitidos:
    #     print('Operador invalido.')  
    #     continue

    if len(operador) > 1:
        print('Digite apenas 1 operador.')  
        continue

    if operador not in operadores_permitidos:
        print('Operador invalido.')  
        continue

    print('Realizando sua conta, confira o resultado abaixo: ')

    if operador == '+':
        print(f'{num_1_float} + {num_2_float} =',num_1_float + num_2_float)

    if operador == '-':
        print(f'{num_1_float} - {num_2_float} =',num_1_float - num_2_float)

    if operador == '*':
        print(f'{num_1_float} * {num_2_float} =',num_1_float * num_2_float)
        
    if operador == '/':
        print(f'{num_1_float} / {num_2_float} =',num_1_float / num_2_float)

    sair = input('Quer sair? [S]im ').lower().startswith('s')

    if sair is True:
        break
