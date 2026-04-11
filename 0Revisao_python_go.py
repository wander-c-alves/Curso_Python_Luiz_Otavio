# O mesmo exercicio em PYTHON E GO (TREINAR EM CASA)


# Crie um programa que declare duas variáveis: uma saudação
#  (ex: "Olá") e um nome (ex: "Wanderley"). O programa deve
#  ter uma função separada para imprimir a mensagem completa
#   (Saudação + Nome).

#EM PYTHON - TREINAR

SAUDACAO_PADRAO = 'Olá, '
NOME_USUARIO = 'Pedro'

def exibir_saudacao(saudacao: str, nome: str) -> str:
    print(f'{saudacao} {nome}')

def main():
    exibir_saudacao(SAUDACAO_PADRAO, NOME_USUARIO)

if __name__ == '__main__':
    main()



# //Crie um programa que calcule a área de um retângulo.(a = b * a)

# /*Declare duas constantes: base (valor 10) e altura (valor 5).
# Crie uma função chamada calcularArea que receba esses dois valores como parâmetros
# (em Go use o tipo int).
# A função deve imprimir: "A área do retângulo é: [resultado]". */

#EM PYTHON - TREINAR

BASE = 10
ALTURA = 5


def calcular_area(base: int, altura: int):
    area = base*altura
    print(f'A area do retangulo é: {area}')


def main():
    calcular_area(BASE, ALTURA)


if __name__ == '__main__':
    main()


# O Desafio:
# Crie um programa que:
# Tenha uma função chamada exibirDados (ou exibir_dados em Python).
# Essa função deve receber: um nome (string), uma idade (int) e uma cidade (string).
# O programa deve imprimir: "O [nome] tem [idade] anos e mora em [cidade]".

# Regras Específicas:
# Em Go: Dentro da main, declare essas 3 variáveis usando o operador curto := e depois passe-as para a função.
# Em Python: Declare as 3 variáveis dentro da main e passe-as para a função. Use Type Hints na definição da função.
# Mantenha as estruturas profissionais que você já aprendeu (package main / if __name__ == "__main__":).

#EM PYTHON - TREINAR

def exibir_dados(nome: str, idade: int, cidade: str) -> None:
    print(f"O {nome} tem {idade} anos e mora em {cidade}")


def main():

    nome_usuario = "wander"
    idade_usuario = 16
    cidade_usuario = "Campinas"

    exibir_dados(nome_usuario, idade_usuario, cidade_usuario)


if __name__ == "__main__":
    main()



# Exercício de Fixação #04 (Go + Python)
# Vamos criar um pequeno validador de acesso.

# O Desafio:
# Crie uma função chamada verificarAcesso (Go) / verificar_acesso (Python).
# Essa função deve receber um parâmetro idade (int).
# Regra: * Se a idade for 18 ou mais, imprima: "Acesso liberado".
# Se for menor que 18, imprima: "Acesso negado".
# Na main, declare uma variável idadeUsuario := 45 (em Go) e idade_usuario = 45 (em Python) e chame a função.


def verificar_acesso(idade: int) -> None:
    if idade >= 18:
        mensagem = "Acesso liberado"
    else:
        mensagem = "Acesso negado"
    print(mensagem)


def main():
    idade_usuario = 17
    verificar_acesso(idade_usuario)


if __name__ == "__main__":
    main()



