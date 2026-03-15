import subprocess
import json

def verificar_ram_powershell():
    """
    Usa o PowerShell moderno para obter detalhes da RAM.
    Evita o uso do 'wmic' depreciado.
    """
    # 1-Configurações e Constantes: Comando PowerShell formatado para JSON
    ps_command = (
        "Get-CimInstance Win32_PhysicalMemory | "
        "Select-Object Capacity, Speed, PartNumber | "
        "ConvertTo-Json"
    )

    try:
        print("--- Analisando Hardware via PowerShell ---")
        # Executa o comando e captura a saída
        result = subprocess.run(
            ["powershell", "-Command", ps_command], 
            capture_output=True, 
            text=True, 
            check=True
        )
        
        # Converte o JSON para dicionário Python
        data = json.loads(result.stdout)
        
        # Se houver apenas um pente, o PowerShell retorna um dict. 
        # Se houver mais, retorna uma lista de dicts.
        pentes = data if isinstance(data, list) else [data]
        
        total_memoria_gb = 0
        for i, pente in enumerate(pentes, 1):
            capacidade_gb = int(pente['Capacity']) / (1024**3)
            total_memoria_gb += capacidade_gb
            print(f"Pente {i}: {capacidade_gb:.0f}GB | Velocidade: {pente['Speed']}MHz")

        print("-" * 40)
        print(f"Total Detectado: {total_memoria_gb:.2f} GB")
        
        if len(pentes) > 1:
            print("Status: Sucesso! Dual Channel detectado.")
        
    except Exception as e:
        print(f"Erro ao processar dados de hardware: {e}")
        print("Dica: Verifique o Gerenciador de Tarefas (Ctrl+Shift+Esc) na aba Desempenho.")

def main():
    """Executa a verificação profissional de memória."""
    verificar_ram_powershell()

if __name__ == '__main__':
    main()