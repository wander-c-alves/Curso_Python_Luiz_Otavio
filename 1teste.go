package main

import "fmt"

// No Go, a func main() é o nosso ponto de entrada.
// É aqui que a execução começa, assim como no 'if __name__ == "__main__"'.
func main() {
	nome := "Wanderr"
	mensagem := gerarSaudacao(nome)
	fmt.Println(mensagem)
}

// Criamos funções separadas para manter o código limpo e organizado.
func gerarSaudacao(nome string) string {
	return "Olá, " + nome + "! Seu ambiente Go 1.26.0 está voando! 🚀"
}