# TÓPICO 01 – FUNÇÕES (def)
# 📌 O que é uma função?
# Uma função é um bloco de código que executa uma tarefa específica.
# Pense nela como uma “ máquina”:
# • Você dá uma entrada
# • Ela processa
# • Ela devolve um resultado
# ________________________________________
# 🧠 Por que usar funções?
# • Evita repetição de código
# • Organiza o programa
# • Facilita manutenção
# • Deixa o código mais profissional
# ________________________________________
# 🔹 Estrutura básica
# def nome_da_funcao():
#     print("Olá mundo")
# Para executar:
# nome_da_funcao()
# ________________________________________
# 🔹 Função com parâmetros
# def saudacao(nome):
#     print("Olá,", nome)
# Uso:
# saudacao("Maria")
# ________________________________________
# 🔹 Função com retorno (return)
# def soma(a, b):
#     return a + b
# Uso:
# resultado = soma(5, 3)
# print(resultado)
# ________________________________________
# 🔹 Exercícios
# 1.    Crie uma função que mostre seu nome.

# def saudar_usuario(nome_recebido: str) -> str:
#     return f'Ola {nome_recebido}! Seja bem vindo.'
# def main():
#     nome_usuario = input('Digite seu nome: ')
#     mensagem_final = saudar_usuario(nome_usuario)
#     print(mensagem_final)
# if __name__ == '__main__':
#     main()


# 2.    Crie uma função que receba dois números e mostre a multiplicação.

# def multiplicacao (n1: float, n2: float) -> float:
#     return n1 * n2
# def main():
#     try:
#         n1 = float(input('Digite o primeiro numero: '))
#         n2 = float(input('Digite o segundo numero: '))
#         resultado = multiplicacao(n1, n2)
#         print(f'O resultado da multiplicação é {resultado}')
#     except ValueError:
#         print('Erro: Por favor, digite apenas Numeros,')

# if __name__ == '__main__':
#     main()


# 3.    Crie uma função que calcule a média de três notas.

# def calculo_notas(n1: float, n2: float, n3: float) -> float:
#     return (n1 + n2 + n3) / 3
# def main():
#     try:
#         n1 = float(input('Digite a primeira nota: '))
#         n2 = float(input('Digite a segunda nota: '))
#         n3 = float(input('Digite a terceira nota: '))

#         media = calculo_notas(n1,n2,n3)
#         print(f'A media do aluno é {media:.2f}')

#     except ValueError:
#         print('Erro: Digite apenas numeros')

# if __name__ == '__main__':
#     main()


#4.a Crie um programa que receba o ano de nascimento de uma
# pessoa e retorne se ela é "Maior de Idade" ou "Menor de Idade".

# def idade_atual(ano_nasc: int) -> str:
#     calculo =  2026 - ano_nasc
#     if calculo >= 18:
#         return 'Maior de idade'
#     else:
#         return 'Menor de idade'


# def main():
#     try:
#         ano_nasc = int(input('Digite seu ano de nascimento: '))
#         idade = idade_atual(ano_nasc)
#         print(idade)

#     except ValueError:
#         print('Erro: Digite apenas numeros')


# if __name__ == '__main__':
#     main()



# 4.b   Faça uma função que diga se um número é par.

# def par_impar(numero: int) -> str:
#     if numero % 2 == 0:
#         return 'Par'
#     else:
#         return 'Impar'


# def main():
#     try:
#         numero = int(input('Digite um numero: '))
#         resultado = par_impar(numero)
#         print(f' O numero {numero} é {resultado}')

#     except ValueError:
#         print('Erro: Digite apenas numeros')


# if __name__ == '__main__':
#     main()


# 5.    Crie uma função que converta Celsius para Fahrenheit.

# def temp (celsius: float) -> float:
#     return (celsius * 1.8) + 32


# def main():
#     try:
#         celsius = float(input('Digite a temperatura em graus celsius: '))
#         resultado = temp(celsius)
#         print(f' {celsius} Graus celsius são {resultado:.2f} graus fahrenjeit')

#     except ValueError:
#         print('Erro: digite apenas numeros')


# if __name__ == '__main__':
#     main()


# 06. [NOME: saudar_aluno]
# Enunciado: Escreva uma função que, ao ser chamada,
# imprima a frase: "Olá! Bem-vindo ao curso de Python."

# def saudar_aluno() -> str:
#     return 'Olá, bem vindo ao curso de Python!!'


# def main():
#     mensagem = saudar_aluno()
#     print(mensagem)


# if __name__ == '__main__':
#     main()




# 07. [NOME: saudar_usuario]
# Enunciado: Crie uma função que receba um nome como parâmetro (argumento)
# e exiba: "Olá, [nome]! Prazer em te ver."

# def saudar_usuario(nome: str) -> str:
#     return  f'Olá {nome}! Prazer em te ver.'


# def main():
#     nome = input('Digite seu nome: ')
#     resultado = saudar_usuario(nome)
#     print(resultado)


# if __name__ == '__main__':
#     main()


# 08. [NOME: calcular_dobro]
# Enunciado: Escreva uma função que receba um número e imprima o resultado do seu dobro.

# def calcular_dobro(n1: float) -> float:
#     return n1 * 2


# def main():
#     try:
#         n1 = float(input('Digite um numero: '))
#         resultado = calcular_dobro(n1)
#         print(f'O dobro de {n1} é {resultado}')
#     except ValueError:
#         print('Erro: digite apenas numeros')


# if __name__ == '__main__':
#     main()


# 09. [NOME: somar_dois_numeros]
# Enunciado: Crie uma função que receba dois números como parâmetros e mostre a soma entre eles.

# def somar_dois_numeros(n1: float, n2: float) -> float:
#     return n1 + n2


# def main():
#     try:
#         n1 = float(input('Digite o primeiro número: '))
#         n2 = float(input('Digite o segundo número: '))

#         soma = somar_dois_numeros(n1, n2)
#         print(f'A soma de {n1} e {n2} é {soma}')
#     except ValueError:
#         print('Erro, digite apenas números.')


# if __name__ == '__main__':
#     main()


# 10. [NOME: calcular_area_quadrado]
# Enunciado: Escreva uma função que receba o valor do lado
# de um quadrado e exiba a área (Lado * Lado) ou (lado ** 2).

# def area_quadrado(lado: float) -> float:
#     return lado ** 2


# def main():
#     try:
#         lado = float(input('Digite a medida do lado do quadrado: '))
#         resultado = area_quadrado(lado)
#         print(f'A area do quadrado é {resultado}')

#     except ValueError:
#         print('Erro: digite apenas numeros')


# if __name__ == '__main__':
#     main()


# 11. [NOME: metros_para_centimetros]
# Enunciado: Crie uma função que receba um valor em metros e mostre o valor convertido para centímetros (m * 100).


# def metros_para_centimetros(metros: float) -> float:
#     return metros * 100


# def main():
#     try:
#       metros = float(input('Digite quantos metros você quer converter: '))
#       resultado = metros_para_centimetros(metros)
#       print(f'{metros} convertidos para centimetros são {resultado}')
#     except ValueError:
#       print('Erro: digite apenas numeros')


# if __name__ == '__main__':
#     main()




# 12. [NOME: verificar_maioridade]
# Enunciado: Escreva uma função que receba uma idade e imprima se a pessoa é "Maior de idade" (18 ou mais) ou "Menor de idade".

# def verificar_maioridade(idade: int) -> str:
#     if idade >= 18:
#         return 'Maior de idade'
#     else:
#         return 'Menor de idade'


# def main():
#     try:
#         idade = int(input('Digite a sua idade: '))
#         resultado = verificar_maioridade(idade)
#         print(resultado)

#     except ValueError:
#         print('Erro: Digite apenas números')


# if __name__ == '__main__':
#     main()



# 13. [NOME: mostrar_media_tres_notas]
# Enunciado: Crie uma função que receba três notas de um aluno e exiba a média aritmética simples dessas notas.

# def media_notas(n1: float, n2: float, n3: float) -> float:
#     return (n1+n2+n3) / 3


# def main():
#     try:
#         n1 = float(input('Digite a primeira nota: '))
#         n2 = float(input('Digite a segunda nota: '))
#         n3 = float(input('Digite a terceira nota: '))
#         resultado = media_notas(n1, n2, n3)
#         print(f'A média das notas {n1}, {n2} e {n3} é {resultado:.2f}')

#     except ValueError:
#         print('Erro: digite apenas numeros')


# if __name__ == "__main__":
#     main()


# 14. [NOME: saudar_por_periodo]
# Enunciado: Escreva uma função que receba um nome e uma hora (0 a 23).
# Se a hora for menor que 12, diga "Bom dia, [nome]". Se for entre 12 e 17, "Boa tarde, [nome]". Caso contrário, "Boa noite, [nome]".

# def saudar_por_periodo(nome: str, hora: int) -> str:

#     if hora < 12:
#         periodo = 'Bom dia'
#     elif hora <= 17:
#         periodo = 'Boa tarde'
#     else:
#         periodo = 'Boa noite'

#     return f'{periodo}, {nome}'

# def main():
#     try:
#         nome = input('Digite seu nome: ')
#         hora = int(input('Digite uma hora entre 0-23: '))

#         if 0<= hora <= 23:
#             resultado = saudar_por_periodo(nome, hora)
#             print(resultado)
#         else:
#             print('Erro: inserir um horario entre 0 e 23!')

#     except ValueError:
#         print('Erro: inserir apenas numeros inteiros!')

# if __name__ == '__main__':
#     main()


# 15. [NOME: verificar_par_ou_impar]
# Enunciado: Crie uma função que receba um número inteiro e imprima no console se ele é "Par" ou "Ímpar".

# def verificar_par_impar(numero: int) -> str:

#     if numero % 2 == 0:
#         calculo = "Par"
#     else:
#         calculo = 'Impar'
#     return f'{calculo}'


# def main():
#     try:
#         numero = int(input('Digite um número: '))
#         resultado = verificar_par_impar(numero)
#         print(resultado)

#     except ValueError:
#         print('Erro: Digite apenas numeros!!!')


# if __name__ == '__main__':
#     main()



# 16. [NOME: obter_soma]
# Enunciado: Escreva uma função que receba dois números e retorne (use o comando return) a soma deles.
# Fora da função, armazene o resultado em uma variável e a imprima.

# def obter_soma(n1: float, n2: float) -> float:
#     return n1 + n2


# def main():
#     try:
#         n1 = float(input('Digite o primeiro numero: '))
#         n2 = float(input('Digite o segundo numero: '))
#         resultado = obter_soma(n1, n2)
#         print(f'A soma dos numeros {n1} e {n2} é {resultado}')

#     except ValueError:
#         print('Erro: Digite apenas números!')


# if __name__ == '__main__':
#     main()






# 17. [NOME: calcular_imc]
# Enunciado: Crie uma função que receba o peso e a altura de uma pessoa e retorne o valor do IMC (Peso / Altura²).
# O resultado define faixas de peso: abaixo de 18,5 (abaixo do peso), 18,5-24,9 (normal), 25-29,9 (sobrepeso), e \(\ge 30\) (obesidade).

# def calcular_imc(peso: float, altura: float) -> str:
#     valor_imc = peso / (altura ** 2)

#     if valor_imc < 18.5:
#         msg_imc = 'Abaixo do pedo'
#     elif valor_imc <= 24.9:
#         msg_imc = 'Normal'
#     elif valor_imc <= 29.9:
#         msg_imc = 'Sobrepeso'
#     else:
#         msg_imc = 'Obresidade'

#     return f'Seu imc é {valor_imc:.2f} e sua classificação é {msg_imc}'


# def main():
#     try:
#         peso = float(input('Digite seu peso: '))
#         altura = float(input('Digite a sua altura: '))

#         resultado = calcular_imc(peso, altura)
#         print(resultado)

#     except ValueError:
#         print('Erro: digite apenas números!')


# if __name__ == '__main__':
#     main()



# 18. [NOME: quem_e_o_maior]
# Enunciado: Escreva uma função que receba dois números e retorne qual deles é o maior. Se forem iguais, retorne qualquer um.

def quem_e_o_maior(n1: int, n2: int) -> int:
    
    if n1 > n2:
        maior = n1
    else:
        maior = n2

    return maior


def main():
    
    try: 
        n1 = int(input('Digite o primeiro número:'))
        n2 = int(input('Digite o segundo número: '))
        
        resultado = quem_e_o_maior(n1, n2)
        if n1 == n2:
            print(f'Os números são iguais: {resultado}')
        else:
            print(f'O número maior é: {resultado}')
        
    except ValueError:
        print('Erro: Digite apenas numeros inteiros!')
        

if __name__ == '__main__':
    main()


# 19. [NOME: tamanho_do_nome]
# Enunciado: Crie uma função que receba uma string (texto) e retorne a quantidade de caracteres que ela possui.

# 20. [NOME: gerar_preco_com_desconto]
# Enunciado: Escreva uma função que receba o valor de um produto e a porcentagem de desconto (ex: 10 para 10%).
# Retorne o valor final do produto com o desconto aplicado.

# 21. [NOME: celsius_para_fahrenheit]
# Enunciado: Crie uma função que receba uma temperatura em graus Celsius e retorne a conversão para Fahrenheit. (Fórmula: F = C * 1.8 + 32)

# 22. [NOME: criar_lista_pares]
# Enunciado: Escreva uma função que receba um número limite e imprima todos os números pares de 0 até o limite informado.

# 23. [NOME: validar_acesso]
# Enunciado: Crie uma função que receba uma string de senha. Se for igual a "python123", retorne "Acesso Liberado". Caso contrário, retorne "Acesso Negado".

# 24. [NOME: inverter_texto]
# Enunciado: Escreva uma função que receba uma palavra e a imprima de trás para frente (invertida).

# 25. [NOME: operacao_matematica]
# Enunciado: Crie uma função que receba dois números e uma string representando a operação ("+", "-", "*", "/").
# A função deve realizar o cálculo e exibir o resultado final.