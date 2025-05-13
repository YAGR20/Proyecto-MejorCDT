# 📈 Calculadora de Rentabilidad CDT – MejorCDT (Reto Técnico)

Este proyecto fue desarrollado como parte de un reto técnico de la empresa LUABLE . Permite analizar y calcular la rentabilidad de inversiones en CDT (Certificados de Depósito a Término) ofrecidos por 23 bancos en Colombia, con base en un archivo CSV suministrado.

##  Funcionalidades Principales

- ✅ Leer tasas desde un archivo CSV.
- ✅ Calcular la tasa vencida a partir de una tasa efectiva anual.
- ✅ Calcular el ROI (retorno de inversión) para un monto y plazo específico.
- ✅ Buscar tasas aplicables según monto y plazo.
- ✅ Ejecutar pruebas unitarias con `pytest`.
- ✅ Automatizar pruebas con CI (GitHub Actions).
- ✅ Proyecto organizado con buenas prácticas DevOps.

##  Estructura del Proyecto

```
mejorcdt/
├── data/
│   └── tasas.csv               # Archivo con las tasas (renombrado)
├── mejorcdt/
│   └── main.py                 # Funciones principales
├── tests/
│   └── test_main.py            # Pruebas unitarias
├── .github/workflows/
│   └── test.yml                # Workflow de GitHub Actions
├── requirements.txt            # Dependencias
├── Makefile                    # Atajos útiles para test y ejecución
└── README.md                   # Este archivo
```

## 🛠️ Instalación y Uso

1. Clona el repositorio:

```bash
git clone https://github.com/TU_USUARIO/mejorcdt.git
cd mejorcdt
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecuta las pruebas unitarias:

```bash
make test
```

## Ejemplos de Uso

### Calcular tasa vencida

```python
from mejorcdt.main import calcular_tasa_vencida

tasa = calcular_tasa_vencida(12.0, 180)
print(f"Tasa vencida para 180 días: {tasa:.4f}")
```

### Buscar tasas aplicables

```python
from mejorcdt.main import buscar_tasas

tasas = buscar_tasas(1000000, 60, "data/tasas.csv")
print(tasas)
```

### Calcular ROI

```python
from mejorcdt.main import calcular_roi

roi = calcular_roi(1000000, 60, "data/tasas.csv")
print(roi)
```

##  Integración Continua (CI)

Este proyecto utiliza **GitHub Actions** para ejecutar automáticamente las pruebas al hacer push a cualquier rama. El archivo de configuración se encuentra en:

```
.github/workflows/test.yml
```

## 🧠 Autor

**Yasmin Alejandra Giraldo Rendón**  
Estudiante de Ingeniería de Software – Reto Técnico MejorCDT  
Especial interés en DevOps y desarrollo backend

## 📝 Licencia

Este proyecto se ha desarrollado con fines evaluativos y educativos.
