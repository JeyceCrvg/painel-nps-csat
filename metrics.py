def calcular_nps(notas):
    total = len(notas)
    if total == 0:
        return 0.0

    promotores = sum(1 for nota in notas if nota >= 9)
    detratores = sum(1 for nota in notas if nota <= 6)

    return round((promotores - detratores) / total * 100, 1)


def calcular_csat(notas, nota_corte=4):
    total = len(notas)
    if total == 0:
        return 0.0

    satisfeitos = sum(1 for nota in notas if nota >= nota_corte)
    return round(satisfeitos / total * 100, 1)


def classificar_nps(notas):
    promotores = sum(1 for nota in notas if nota >= 9)
    neutros = sum(1 for nota in notas if 7 <= nota <= 8)
    detratores = sum(1 for nota in notas if nota <= 6)

    return {
        "promotores": promotores,
        "neutros": neutros,
        "detratores": detratores,
    }
