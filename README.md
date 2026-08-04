# Painel NPS e CSAT

Script em Python que processa respostas de pesquisas de satisfacao ficticias e calcula NPS e CSAT, geral e por canal de atendimento.

## Funcionalidades

- Geracao de dados ficticios de pesquisas
- Calculo de NPS (promotores, neutros, detratores)
- Calculo de CSAT
- Relatorio por canal (chat, email, Reclame Aqui)
- Grafico comparativo entre canais

## Tecnologias

Python, Pandas, Matplotlib

## Como executar

```
git clone https://github.com/JeyceCrvg/painel-nps-csat.git
cd painel-nps-csat
pip install -r requirements.txt
python generate_data.py
python main.py
```

Exemplo de saida:

```
NPS geral: -53.0
CSAT geral: 36.0%
Promotores: 22 | Neutros: 41 | Detratores: 137

chat: NPS=-57.4 | CSAT=39.7%
email: NPS=-59.1 | CSAT=31.8%
reclame_aqui: NPS=-42.4 | CSAT=36.4%

Canal que mais precisa de atencao: email
```
