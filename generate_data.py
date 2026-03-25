import csv
import random
from datetime import datetime, timedelta

CANAIS = ["chat", "email", "reclame_aqui"]


def gerar_respostas(quantidade=200, saida="data/pesquisas.csv"):
    inicio = datetime(2026, 1, 1)
    linhas = []
    for i in range(quantidade):
        data = inicio + timedelta(days=random.randint(0, 210))
        linhas.append(
            {
                "id": i + 1,
                "data": data.strftime("%Y-%m-%d"),
                "canal": random.choice(CANAIS),
                "nota_nps": random.randint(0, 10),
                "nota_csat": random.randint(1, 5),
            }
        )

    with open(saida, "w", newline="", encoding="utf-8") as arquivo:
        campos = ["id", "data", "canal", "nota_nps", "nota_csat"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(linhas)


if __name__ == "__main__":
    gerar_respostas()
