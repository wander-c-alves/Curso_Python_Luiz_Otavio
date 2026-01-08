num1 = float(input('Digite o primeiro numero: '))
operador = input('Digite o operador ( + - * / ): ')
num2 = float(input('Digite o segundo numero: '))

if operador == '+':
    resultado = num1 + num2
    print(f'O resultado da soma é: {resultado}')
elif operador == '-':
    resultado = num1 - num2
    print(f'O resultado da subtração é: {resultado}')
elif operador == '*':
    resultado = num1 * num2
    print(f'O resultado da multiplicação é: {resultado}')
elif operador == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f'O resultado da divisão é: {resultado}')
    else:
        print("Erro: Não é possível dividir por zero.")
else:
    print('Operador inválido!')
    


