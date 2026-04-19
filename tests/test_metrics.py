from metrics import calcular_nps


def test_nps_todos_promotores():
    assert calcular_nps([9, 9, 10, 10]) == 100.0


def test_nps_todos_detratores():
    assert calcular_nps([0, 3, 5, 6]) == -100.0


def test_nps_lista_vazia():
    assert calcular_nps([]) == 0.0
