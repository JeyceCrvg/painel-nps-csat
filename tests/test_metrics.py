from metrics import calcular_csat, calcular_nps


def test_nps_todos_promotores():
    assert calcular_nps([9, 9, 10, 10]) == 100.0


def test_nps_todos_detratores():
    assert calcular_nps([0, 3, 5, 6]) == -100.0


def test_nps_lista_vazia():
    assert calcular_nps([]) == 0.0


def test_csat_totalmente_satisfeito():
    assert calcular_csat([5, 5, 4, 4]) == 100.0


def test_csat_lista_vazia():
    assert calcular_csat([]) == 0.0
