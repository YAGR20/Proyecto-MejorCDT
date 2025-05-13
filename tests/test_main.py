from mejorcdt.main import calcular_tasa_vencida, buscar_tasas, calcular_roi

def test_calcular_tasa_vencida():
    resultado = calcular_tasa_vencida(12.0, 180)
    assert round(resultado, 4) == round((1 + 0.12) ** (180 / 360) - 1, 4)

def test_buscar_tasas():
    resultados = buscar_tasas(1_000_000, 30, "data/tasas.csv")
    assert isinstance(resultados, list)

def test_calcular_roi():
    resultados = calcular_roi(1_000_000, 30, "data/tasas.csv")
    assert isinstance(resultados, list)
