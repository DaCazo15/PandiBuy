<p align="center">
  <a href="" rel="noopener">
    <img width="200" height="200" src="assets/logo.png" alt="PandiBuy logo">
  </a>
</p>

# PandiBuy — Calculadora de Costos y Metraje

PandiBuy es una aplicación de movil ligera desarrollada en Python y Flet para ayudar a talleres y pequeños negocios a calcular metraje, costo por unidad y presupuestos de productos hechos a medida. La app permite registrar materiales, calcular consumo según medidas y generar un precio sugerido considerando mano de obra y margen.

**Estado:** Activa · **Lenguaje:** Python · **UI:** Flet

## ✅ Características principales
- Cálculo de metraje a partir de medidas en centímetros y cantidades.
- Registro de materiales con precio total y cantidad para obtener precio por unidad.
- Tabla interactiva de materiales con totales por material.
- Cálculo rápido de inversión, ganancia y precio de venta sugerido.
- Interfaz simple y pensada para móvil/ventanas pequeñas (375×600).

## 🚀 Comenzando (local)

Prerequisitos: Python 3.10+ y `pip`.

1. Clona el repositorio o descarga los archivos.
2. Crea e instala un entorno virtual (recomendado):

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

3. Ejecuta la app:

```bash
python main.py
```

La ventana se abrirá con la interfaz de PandiBuy. Si la imagen del logo no aparece, asegúrate de que `assets/logo.png` exista.

## 🧭 Uso rápido
- Ingresa el nombre del producto, medida en cm y cantidades para calcular el metraje necesario.
- Añade materiales con `PT` (precio total) y `CT` (cantidad total) y usa `ADD` para agregar a la tabla.
- En la sección de "Información Adicional" ingresa tiempo de trabajo y precio del mercado para obtener el presupuesto y la ganancia estimada.

## 🧩 Tecnologías
- Python
- Flet (para UI)

## Contribuir
1. Haz fork del repositorio.
2. Crea una rama con tu feature: `git checkout -b feature/nombre`.
3. Haz commits claros y abre un pull request.

## Licencia
Proyecto abierto — añade aquí tu licencia preferida (ej. MIT).

## Autor
- Daniel Cazo — PandiBuy

