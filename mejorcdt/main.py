import pandas as pd

def calcular_tasa_vencida(tasa_efectiva_anual, periodo_objetivo):
    try:
        return (1 + tasa_efectiva_anual / 100) ** (periodo_objetivo / 360) - 1
    except (TypeError, ZeroDivisionError):
        return None

def calcular_roi(monto, plazo_en_dias, archivo_csv):
    try:
        df = pd.read_csv(archivo_csv, delimiter=';')
        roi_resultados = []

        for _, row in df.iterrows():
            try:
                if row["minplazo"] <= plazo_en_dias <= row["maxplazo"]:
                    monto_min = float(str(row["minmonto"]).replace('.', '').replace(',', ''))
                    monto_max = float(str(row["maxmonto"]).replace('.', '').replace(',', ''))
                    if monto_min <= monto <= monto_max:
                        tasa = float(row["tasa"])
                        tasa_vencida = calcular_tasa_vencida(tasa, plazo_en_dias)
                        if tasa_vencida is not None:
                            ganancia = monto * tasa_vencida
                            roi_resultados.append({
                                "banco": row["banco"],
                                "tasa": tasa,
                                "ganancia": round(ganancia, 2)
                            })
            except:
                continue 

        return roi_resultados
    except:
        return []

def buscar_tasas(monto, plazo_en_dias, archivo_csv):
    try:
        df = pd.read_csv(archivo_csv, delimiter=';')
        resultados = df[
            (df["minplazo"] <= plazo_en_dias) &
            (df["maxplazo"] >= plazo_en_dias)
        ]

        resultados_filtrados = []
        for _, row in resultados.iterrows():
            try:
                min_monto = float(str(row["minmonto"]).replace('.', '').replace(',', ''))
                max_monto = float(str(row["maxmonto"]).replace('.', '').replace(',', ''))
                if min_monto <= monto <= max_monto:
                    resultados_filtrados.append({
                        "banco": row["banco"],
                        "tasa": row["tasa"]
                    })
            except:
                continue

        return resultados_filtrados
    except:
        return []

# Interfaz por consola
if __name__ == "__main__":
    try:
        monto = float(input("Ingrese el monto a invertir: "))
        plazo = int(input("Ingrese el plazo en días: "))
        archivo = "data/tasas.csv"

        print("\n Tasas aplicables:")
        tasas = buscar_tasas(monto, plazo, archivo)
        if tasas:
            for t in tasas:
                print(f"Banco {t['banco']} - Tasa: {t['tasa']}%")
        else:
            print("No se encontraron tasas aplicables.")

        print("\n ROI estimado:")
        rois = calcular_roi(monto, plazo, archivo)
        if rois:
            for r in rois:
                print(f"Banco {r['banco']} - Tasa: {r['tasa']}% - Ganancia: ${r['ganancia']}")
        else:
            print("No se pudo calcular el ROI.")

    except ValueError:
        print("Por favor ingrese valores numéricos válidos.")
