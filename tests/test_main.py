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

def test_sin_resultados_en_roi():
    resultado = calcular_roi(999, 9999, "data/tasas.csv") 
    assert resultado == []

def test_sin_resultados_en_busqueda():
    resultado = buscar_tasas(0.01, 1, "data/tasas.csv") 
    assert resultado == []

def test_tasa_vencida_invalida():
    assert calcular_tasa_vencida('no_numero', 180) is None
    assert calcular_tasa_vencida(12.0, 'abc') is None

def test_roi_monto_fuera_de_rango():
    resultado = calcular_roi(100, 9999, "data/tasas.csv")
    assert resultado == []

def test_buscar_tasas_plazo_fuera():
    resultado = buscar_tasas(1_000_000, 999999, "data/tasas.csv")  # plazo exagerado
    assert resultado == []


def test_archivo_csv_invalido():
    resultado = calcular_roi(1_000_000, 60, "data/no_existe.csv")
    assert resultado == []
