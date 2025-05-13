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
│   └── workflows/
│       └── test.yml
├── data/
│   └── tasas.csv
├── mejorcdt/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── .gitignore
├── Makefile
├── README.md
├── requirements.txt
└── venv/
```

## Instalación y Uso

1. Clona el repositorio:

```bash
git clone https://github.com/YAGR20/Proyecto-MejorCDT.git
cd Proyecto-MejorCDT
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

4. Ejecuta el programa:

```bash
python mejorcdt/main.py
```

## Ejecutar las Pruebas

Para verificar que todo el proyecto funcione correctamente, puedes ejecutar las pruebas unitarias utilizando `pytest`.

### En Windows (PowerShell):

```powershell
$env:PYTHONPATH="."; pytest
```

Esto asegura que Python reconozca correctamente el paquete `mejorcdt` desde la raíz del proyecto.

### En Linux / macOS (bash):

```bash
PYTHONPATH=. pytest
```

> Estas pruebas cubren los casos normales, casos límite y validaciones de errores, asegurando que todas las funciones principales estén funcionando correctamente.

## Ejemplos de Uso

```python
from mejorcdt.main import calcular_tasa_vencida, buscar_tasas, calcular_roi

print(calcular_tasa_vencida(12.0, 180))  # ~0.0583
print(buscar_tasas(1_000_000, 60, "data/tasas.csv"))
print(calcular_roi(1_000_000, 60, "data/tasas.csv"))
```

## Interfaz por Consola

Puedes ejecutar la aplicación como un script interactivo para ingresar los valores manualmente:

```bash
python mejorcdt/main.py
```

## Integración Continua (CI)

Este proyecto usa **GitHub Actions** para ejecutar pruebas automáticamente con cada `push` o `pull request`.

Archivo CI:
```
.github/workflows/test.yml
```

## Autor

**Yasmin Alejandra Giraldo Rendón**  
Estudiante de Ingeniería de Software – Reto Técnico MejorCDT  
Especial interés en DevOps y desarrollo backend

## 📝 Licencia

Este proyecto se ha desarrollado con fines evaluativos y educativos.
