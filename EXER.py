# TÓPICO 01 – FUNÇÕES (def)
# 📌 O que é uma função?
# Uma função é um bloco de código que executa uma tarefa específica.
# Pense nela como uma “ máquina”:
# •	Você dá uma entrada
# •	Ela processa
# •	Ela devolve um resultado
# ________________________________________
# 🧠 Por que usar funções?
# •	Evita repetição de código
# •	Organiza o programa
# •	Facilita manutenção
# •	Deixa o código mais profissional
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
# 1.	Crie uma função que mostre seu nome.

# def mostrar_nome() -> str:
#     return 'Olá Wander'


# def main():
#     mensagem = mostrar_nome()
#     print(mensagem)


# if __name__ == '__main__':
#     main()


def saudar_usuario(nome_recebido: str) -> str:
    return f'Ola {nome_recebido}! Seja bem vindo.'


def main():
    nome_usuario = input('Digite seu nome: ')
    mensagem_final = saudar_usuario(nome_usuario)
    print(mensagem_final)


if __name__ == '__main__':
    main()






    
# 2.	Crie uma função que receba dois números e mostre a multiplicação.

# def multiplicar(n1,n2):
#     resultado = n1*n2
#     print(f'O resultado da multiplicação é {resultado}')
# multiplicar(3,10)

# def multiplicar()->int:
#     return 



# 3.	Crie uma função que calcule a média de três notas.

# def media(n1,n2,n3):
#     media= (n1+n2+n3)/3
#     print(f"A media das notas é {media}")
# media(9,7,8)

# 4.	Faça uma função que diga se um número é par.

# def numero(n1):
#     return 'par' if n1 % 2 == 0 else 'impar'
# resultado = numero(9)
# print(f'O numero é {resultado}')

# 5.	Crie uma função que converta Celsius para Fahrenheit.

# def temp(c):
#     far = (c * 1.8) + 32
#     print(f'Aconversão é {far}')
# temp(40)


# 01. [NOME: saudar_aluno]
# Enunciado: Escreva uma função que, ao ser chamada, imprima a frase: "Olá! Bem-vindo ao curso de Python."

# def saudar_aluno(msg):
#     print(msg)
# saudar_aluno('Olá! Bem-vindo ao curso de Python')



# 02. [NOME: saudar_usuario]
# Enunciado: Crie uma função que receba um nome como parâmetro (argumento) e exiba: "Olá, [nome]! Prazer em te ver."

# def saudar_usuario(nome):
#     print(f'Ola {nome}! Prazer em te ver')
# saudar_usuario('wander')



# 03. [NOME: calcular_dobro]
# Enunciado: Escreva uma função que receba um número e imprima o resultado do seu dobro.

# def calcular_dobro(n1):
#     dobro = n1 * 2
#     print(f'O dobro de {n1} é {dobro}')
# calcular_dobro(8)


# 04. [NOME: somar_dois_numeros]
# Enunciado: Crie uma função que receba dois números como parâmetros e mostre a soma entre eles.

# def soma_numeros(n1,n2):
#     soma = n1+n2
#     print(f'A soma de {n1} e {n2} é {soma}')
# soma_numeros(4,5)


# 05. [NOME: calcular_area_quadrado]
# Enunciado: Escreva uma função que receba o valor do lado de um quadrado e exiba a área (Lado * Lado).

# def area_quad(lado):
#     area = lado * lado
#     print(f"A area do quadrado é {area}")
# area_quad(4)

# 06. [NOME: metros_para_centimetros]
# Enunciado: Crie uma função que receba um valor em metros e mostre o valor convertido para centímetros.

# def conversao(metros):
#     cent = metros * 100
#     print(f"{metros} metro(s) são {cent} centimetros")
# conversao(2)

# 07. [NOME: verificar_maioridade]
# Enunciado: Escreva uma função que receba uma idade e imprima se a pessoa é "Maior de idade" (18 ou mais) ou "Menor de idade".

# def verf_idade(idade):
#     return 'Maior de idade' if idade >= 18 else 'Menor de idade'
# resultado = verf_idade(65)
# print(resultado)

# 08. [NOME: mostrar_media_tres_notas]
# Enunciado: Crie uma função que receba três notas de um aluno e exiba a média aritmética simples dessas notas.

# def media_notas(n1,n2,n3):
#     media = (n1+n2+n3)/3
#     print(f"A médoa das notas {n1}, {n2} e {n3} é {media}")
# media_notas(9,7,8)


# def media_notas():
#     n1 = float(input('Digite a primeira nota: '))
#     n2 = float(input('Digite a segunda nota: '))
#     n3 = float(input('Digite a terceira nota: '))
    
#     media = (n1 + n2 + n3) / 3
#     print(f'A média das notas {n1}, {n2} e {n3} é {media:.2f}')
# media_notas()
    
    
# 09. [NOME: saudar_por_periodo]
# Enunciado: Escreva uma função que receba um nome e uma hora (0 a 23). 
# Se a hora for menor que 12, diga "Bom dia, [nome]". Se for entre 12 e 17, "Boa tarde, [nome]". Caso contrário, "Boa noite, [nome]".

# BLOCO 1: LÓGICA (A COZINHA)
# def gerar_saudacao(nome: str, hora: int) -> str:
#     if hora < 12:
#         periodo = "Bom dia"
#     elif 12 <= hora <= 17:
#         periodo = "Boa tarde"
#     else:
#         periodo = "Boa noite"

#     return f"{periodo}, {nome}!" # Retorna a frase pronta

# # BLOCO 2: INTERAÇÃO (O GARÇOM)
# def main():
#     try:
#         usuario = input("Qual seu nome? ")
#         h = int(input("Que horas são (0-23)? "))

#         if 0 <= h <= 23:
#             # Chamamos a lógica e guardamos o retorno numa variável
#             mensagem_final = gerar_saudacao(usuario, h)
#             print(mensagem_final)
#         else:
#             print("Erro: A hora deve ser entre 0 e 23.")

#     except ValueError:
#         print("Erro: Digite um número inteiro para a hora.")

# # CHAVE DE IGNIÇÃO
# if __name__ == "__main__":
#     main()



# 10. [NOME: verificar_par_ou_impar]
# Enunciado: Crie uma função que receba um número inteiro e imprima no console se ele é "Par" ou "Ímpar".

# 11. [NOME: obter_soma]
# Enunciado: Escreva uma função que receba dois números e retorne (use o comando return) a soma deles. Fora da função, armazene o resultado em uma variável e a imprima.

# 12. [NOME: calcular_imc]
# Enunciado: Crie uma função que receba o peso e a altura de uma pessoa e retorne o valor do IMC (Peso / Altura²).

# 13. [NOME: quem_e_o_maior]
# Enunciado: Escreva uma função que receba dois números e retorne qual deles é o maior. Se forem iguais, retorne qualquer um.

# 14. [NOME: tamanho_do_nome]
# Enunciado: Crie uma função que receba uma string (texto) e retorne a quantidade de caracteres que ela possui.

# 15. [NOME: gerar_preco_com_desconto]
# Enunciado: Escreva uma função que receba o valor de um produto e a porcentagem de desconto (ex: 10 para 10%). Retorne o valor final do produto com o desconto aplicado.

# 16. [NOME: celsius_para_fahrenheit]
# Enunciado: Crie uma função que receba uma temperatura em graus Celsius e retorne a conversão para Fahrenheit. (Fórmula: F = C * 1.8 + 32)

# 17. [NOME: criar_lista_pares]
# Enunciado: Escreva uma função que receba um número limite e imprima todos os números pares de 0 até o limite informado.

# 18. [NOME: validar_acesso]
# Enunciado: Crie uma função que receba uma string de senha. Se for igual a "python123", retorne "Acesso Liberado". Caso contrário, retorne "Acesso Negado".

# 19. [NOME: inverter_texto]
# Enunciado: Escreva uma função que receba uma palavra e a imprima de trás para frente (invertida).

# 20. [NOME: operacao_matematica]
# Enunciado: Crie uma função que receba dois números e uma string representando a operação ("+", "-", "*", "/"). A função deve realizar o cálculo e exibir o resultado final.
