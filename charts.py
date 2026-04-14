import matplotlib.pyplot as plt

from metrics import calcular_csat, calcular_nps


def gerar_grafico_por_canal(df, saida="data/metricas_por_canal.png"):
    canais = []
    valores_nps = []
    valores_csat = []

    for canal, grupo in df.groupby("canal"):
        canais.append(canal)
        valores_nps.append(calcular_nps(grupo["nota_nps"].tolist()))
        valores_csat.append(calcular_csat(grupo["nota_csat"].tolist()))

    x = range(len(canais))
    largura = 0.35

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar([i - largura / 2 for i in x], valores_nps, largura, label="NPS")
    ax.bar([i + largura / 2 for i in x], valores_csat, largura, label="CSAT")

    ax.set_xticks(list(x))
    ax.set_xticklabels(canais)
    ax.set_ylabel("Pontuação")
    ax.set_title("NPS e CSAT por canal")
    ax.legend()

    fig.tight_layout()
    fig.savefig(saida)
