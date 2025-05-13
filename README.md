 # Calculadora de Rentabilidad CDT – MejorCDT (Reto Técnico)

Este proyecto fue desarrollado como parte de un reto técnico de la empresa **LUABLE MEJOR CDT**. Permite analizar y calcular la rentabilidad de inversiones en CDT (Certificados de Depósito a Término) ofrecidos por 23 bancos en Colombia, con base en un archivo CSV suministrado.

## Funcionalidades Principales

- Leer tasas desde un archivo CSV.
- Calcular la tasa vencida a partir de una tasa efectiva anual.
- Calcular el ROI (retorno de inversión) para un monto y plazo específico.
- Buscar tasas aplicables según monto y plazo.
- Ejecutar pruebas unitarias con `pytest`.
- Automatizar pruebas con CI (GitHub Actions).
- Proyecto organizado con buenas prácticas DevOps.

## Estructura del Proyecto

```
MEJORCDT/
├── .github/
│ └── workflows/
│ └── test.yml
├── .pytest_cache/
├── data/
│ └── tasas.csv
├── mejorcdt/
│ ├── pycache/
│ └── main.py
├── tests/
│ ├── pycache/
│ └── test_main.py
├── venv/
├── .gitignore
├── Makefile
├── README.md
└── requirements.txt
```

## Instalación y Uso

1. Clona el repositorio:

```bash
git clone https://github.com/TU_USUARIO/mejorcdt.git
cd mejorcdt
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecuta las pruebas unitarias:

```bash
pytest
```

## Ejemplos de Uso con Resultados Esperados

### Calcular tasa vencida

```python
from mejorcdt.main import calcular_tasa_vencida

resultado = calcular_tasa_vencida(12.0, 180)
print(resultado)  # Esperado: ~0.0583
```

### Buscar tasas aplicables

```python
from mejorcdt.main import buscar_tasas

tasas = buscar_tasas(1_000_000, 60, "data/tasas.csv")
print(tasas)  # Lista con bancos y tasas
```

### Calcular ROI

```python
from mejorcdt.main import calcular_roi

roi = calcular_roi(1_000_000, 60, "data/tasas.csv")
print(roi)  # Lista con banco, tasa y ganancia esperada
```

## 🖥️ Interfaz por consola

Ejecuta el archivo principal para ingresar datos manualmente:

```bash
python mejorcdt/main.py
```

## Integración Continua (CI)

Este proyecto usa **GitHub Actions** para ejecutar pruebas automáticamente con cada `push`.

Archivo CI:
```
.github/workflows/test.yml
```

## Autor

**Yasmin Alejandra Giraldo Rendón**  
Estudiante de Ingeniería de Software – Reto Técnico MejorCDT  
Especial interés en DevOps y desarrollo backend

## Licencia

Este proyecto se ha desarrollado con fines evaluativos y educativos.
