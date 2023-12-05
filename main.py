class MonitorDeSaude:
    def __init__(self):
        self.media_batimentos = 0
        self.media_temperatura = 0
        self.contador_atualizacoes = 0
 
    def receber_dados_sensor(self, batimentos, temperatura):
        # Atualizar a média móvel
        self.media_batimentos = ((self.media_batimentos * self.contador_atualizacoes) + batimentos) / (self.contador_atualizacoes + 1)
        self.media_temperatura = ((self.media_temperatura * self.contador_atualizacoes) + temperatura) / (self.contador_atualizacoes + 1)
 
        # Atualizar limites com base nas médias móveis
        limite_batimentos = (self.media_batimentos - 10, self.media_batimentos + 10)
        limite_temperatura = (self.media_temperatura - 0.5, self.media_temperatura + 0.5)
 
        # Analisar dados
        resultado = self.analisar_dados(batimentos, temperatura, limite_batimentos, limite_temperatura)
 
        # Incrementar o contador de atualizações
        self.contador_atualizacoes += 1
 
        return resultado
 
    def analisar_dados(self, batimentos, temperatura, limite_batimentos, limite_temperatura):
        # Simples lógica de verificação com base nos limites
        if limite_batimentos[0] <= batimentos <= limite_batimentos[1] and \
           limite_temperatura[0] <= temperatura <= limite_temperatura[1]:
            return 0  # Dados normais
        else:
            return 1  # Dados alterados
 
# Exemplo de uso
monitor = MonitorDeSaude()
 
# Simulação de leituras do sensor ao longo do tempo
leituras_sensor = [
    (75, 37.0),
    (80, 37.2),
    (110, 38.0),
    (78, 36.9),
    # Adicione mais leituras conforme necessário
]
 
for leitura in leituras_sensor:
    batimentos, temperatura = leitura
    resultado = monitor.receber_dados_sensor(batimentos, temperatura)
 
    if resultado == 0:
        print("Dados normais. Armazenando...")
    else:
        print("ALERTA! Dados alterados. Disparando alerta...")
