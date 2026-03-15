import psutil

def analisar_conforto_estudo():
    """
    Analisa se o setup atual (24GB) está proporcionando 
    folga para o fluxo de estudo (VS Code + Chrome + Udemy).
    """
    # 1-Configurações e Constantes
    MEMORIA = psutil.virtual_memory()
    TOTAL_GB = MEMORIA.total / (1024**3)
    DISPONIVEL_GB = MEMORIA.available / (1024**3)
    USO_PERCENTUAL = MEMORIA.percent

    print(f"--- Status do Ambiente de Estudo ---")
    print(f"Memória Total: {TOTAL_GB:.2f} GB")
    print(f"Memória Livre para abas/extensões: {DISPONIVEL_GB:.2f} GB")
    
    # Lógica de diagnóstico
    if TOTAL_GB > 20:
        print("\nDiagnóstico:")
        print("Você tem 'colchão' de sobra. Pode abrir a documentação de Go")
        print("e a aula da Udemy em 4K sem que o VS Code fique lento.")
    else:
        print("\nDiagnóstico:")
        print("Sistema operando próximo ao limite de troca (swap).")

def main():
    """Executa a verificação de saúde do setup de estudos."""
    try:
        analisar_conforto_estudo()
    except ImportError:
        print("Instale psutil para rodar: pip install psutil")

if __name__ == '__main__':
    main()