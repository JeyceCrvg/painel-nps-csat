# Painel NPS e CSAT

Script em Python pra calcular NPS e CSAT em cima de respostas de pesquisa de satisfacao. Fiz depois de mexer com essas metricas no trabalho e ficar curiosa se dava pra automatizar o calculo por canal (chat, email, reclame aqui) em vez de fazer na mao em planilha.

Pra rodar:

```
git clone https://github.com/JeyceCrvg/painel-nps-csat.git
cd painel-nps-csat
pip install -r requirements.txt
python generate_data.py
python main.py
```

Isso gera um csv com respostas ficticias e imprime algo assim:

```
NPS geral: -53.0
CSAT geral: 36.0%
Promotores: 22 | Neutros: 41 | Detratores: 137

chat: NPS=-57.4 | CSAT=39.7%
email: NPS=-59.1 | CSAT=31.8%
reclame_aqui: NPS=-42.4 | CSAT=36.4%

Canal que mais precisa de atencao: email
```

Tambem salva um grafico comparando os canais em data/metricas_por_canal.png.
