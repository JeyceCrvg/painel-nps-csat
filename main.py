import pandas as pd

from charts import gerar_grafico_por_canal
from metrics import calcular_csat, calcular_nps


def carregar_dados(caminho="data/pesquisas.csv"):
    return pd.read_csv(caminho)


def gerar_relatorio(df):
    nps_geral = calcular_nps(df["nota_nps"].tolist())
    csat_geral = calcular_csat(df["nota_csat"].tolist())

    print(f"NPS geral: {nps_geral}")
    print(f"CSAT geral: {csat_geral}%")
    print()

    for canal, grupo in df.groupby("canal"):
        nps_canal = calcular_nps(grupo["nota_nps"].tolist())
        csat_canal = calcular_csat(grupo["nota_csat"].tolist())
        print(f"{canal}: NPS={nps_canal} | CSAT={csat_canal}%")


def main():
    df = carregar_dados()
    gerar_relatorio(df)
    gerar_grafico_por_canal(df)


if __name__ == "__main__":
    main()
