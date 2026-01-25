"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim) <- Contagem de complexidade (ruim)
"""

# 1. Verificar se o carro está no alcance do radar
# 2. Verificar se o carro excedeu a velocidade máxima
# 3. Determinar se o carro foi multado
# 4. Exibir o resultado

velocidade = 65  # velocidade atual do carro
localizacao_carro = 100  # local em que o carro está na estrada

VM_RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_RADAR_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

# 1. Verificar se o carro está no alcance do radar
alcance_min = LOCAL_RADAR_1 - RADAR_RANGE
alcance_max = LOCAL_RADAR_1 + RADAR_RANGE
alcance_radar = (localizacao_carro >= alcance_min) and (localizacao_carro <= alcance_max)

# 2. Verificar se o carro excedeu a velocidade máxima
velocidade_excedida = velocidade > VM_RADAR_1

# 3. Determinar se o carro foi multado
carro_multado = velocidade_excedida and alcance_radar

# 4. Exibir o resultado
if carro_multado:
    print('multado')
else:
    print('não multado')
