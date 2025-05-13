import pandas as pd

def calcular_tasa_vencida(tasa_efectiva_anual, periodo_objetivo):
    """
    Convierte la tasa efectiva anual a una tasa vencida para un periodo dado en días.
    """
    return (1 + tasa_efectiva_anual / 100) ** (periodo_objetivo / 360) - 1

def calcular_roi(monto, plazo_en_dias, archivo_csv):
    """
    Calcula el ROI (retorno de inversión) para un monto y plazo en días.
    """
    df = pd.read_csv(archivo_csv, delimiter=';')
    roi_resultados = []

    for _, row in df.iterrows():
        if row["minplazo"] <= plazo_en_dias <= row["maxplazo"]:
            monto_min = float(str(row["minmonto"]).replace('.', ''))
            monto_max = float(str(row["maxmonto"]).replace('.', ''))
            if monto_min <= monto <= monto_max:
                tasa = row["tasa"]
                tasa_vencida = calcular_tasa_vencida(tasa, plazo_en_dias)
                ganancia = monto * tasa_vencida
                roi_resultados.append({
                    "banco": row["banco"],
                    "tasa": tasa,
                    "ganancia": round(ganancia, 2)
                })

    return roi_resultados

def buscar_tasas(monto, plazo_en_dias, archivo_csv):
    """
    Busca las tasas aplicables según monto y plazo.
    """
    df = pd.read_csv(archivo_csv, delimiter=';')
    resultados = df[
        (df["minplazo"] <= plazo_en_dias) &
        (df["maxplazo"] >= plazo_en_dias)
    ]

    resultados_filtrados = []
    for _, row in resultados.iterrows():
        min_monto = float(str(row["minmonto"]).replace('.', ''))
        max_monto = float(str(row["maxmonto"]).replace('.', ''))
        if min_monto <= monto <= max_monto:
            resultados_filtrados.append({
                "banco": row["banco"],
                "tasa": row["tasa"]
            })

    return resultados_filtrados
