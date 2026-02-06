import flet as ft
from funtions import *


def main(page: ft.Page):

  page.theme_mode = ft.ThemeMode.DARK
  page.title = "Pandibay - Gestión de Costos"
  page.bgcolor = ft.Colors.PINK_700
  page.window.theme_mode = ft.ThemeMode.DARK
  page.window.width = 375
  page.window.height = 812
  page.window.resizable=False
  page.padding = ft.Padding(left=15, right=15, top=20, bottom=20)
  page.horizontal_alignment = "center"

# ----------------------- Limpiza ----------------------- #

  def limpiar():
    nm.value = ""
    pt.value = ""
    ct.value = ""
    cant.value = ""
    entrada_producto.value = ""
    entrada_medida.value = ""
    entrada_cantidad.value = ""
    entrada_cantidad_arreglo.value = ""
    texto_resultado.value = "0.00 m"
    page.update()

  def limpiar_campos():
    Tabla_datos.rows.clear()
    limpiar()
    page.update()

# ----------------------- Eventos ------------------------------------------------- #

  def actualizar_calculo(e):
    try:
      metros = float(entrada_medida.value) if entrada_medida.value else 0
      cantidad = int(entrada_cantidad.value) if entrada_cantidad.value else 0
      cantidad_arreglo = int(entrada_cantidad_arreglo.value) if entrada_cantidad_arreglo.value else 0
      
      resultado_metros = ((metros * cantidad) / 100) * cantidad_arreglo
      
      texto_resultado.value = f"{resultado_metros:.2f} m"
      nm.value = entrada_producto.value
      cant.value = resultado_metros

      
      if entrada_producto.value:
          texto_resultado.size = 14 
      
    except (ValueError, TypeError, ZeroDivisionError, BaseException):
      # Evita que la app falle por errores de conversion o division por cero
      pass
    page.update()

  def actualizar_tabla(e):
    content.auto_scroll=False
    try:
      nombre = nm.value if nm.value else ""
      precioTotal = float(pt.value) if pt.value else 0.0
      cantidadTotal = int(ct.value) if ct.value else 0.0
      cantidadUso = int(cant.value) if type(cant.value) == str else cant.value
      total = 0
      if cantidadTotal > 0 and precioTotal > 0:
        precioUnidad = precioTotal / cantidadTotal
        total = float(precioUnidad * cantidadUso)
      else:
        precioUnidad = 0.0
      
      if nombre and total > 0:
        nueva_fila = ft.DataRow(
          cells=[
            ft.DataCell(ft.Text(nombre, size=10)),
            ft.DataCell(ft.Text(f"{precioTotal:.2f}", size=10)),
            ft.DataCell(ft.Text(f"{cantidadTotal}", size=10)),
            ft.DataCell(ft.Text(f"{precioUnidad:.2f}", size=10)),
            ft.DataCell(ft.Text(f"{cantidadUso}", size=10)),
            ft.DataCell(ft.Text(f"{total:.2f}", size=10)),
          ]
        )
        Tabla_datos.rows.append(nueva_fila)
        content.auto_scroll=True
        limpiar()        
        page.update() 
    except (ValueError, TypeError, ZeroDivisionError, BaseException):
      # Evita que la app falle por errores de conversion o division por cero
      pass
    page.update()

  def presupuesto(e):
    content.auto_scroll=False
    try:
        costo_materiales = sum(float(row.cells[5].content.value) for row in Tabla_datos.rows)
        horas_trabajadas = float(entrada_tiempo.value) if entrada_tiempo.value else 0.0
        costo_mano_obra = horas_trabajadas * 1.5  # Tu tarifa por hora
        
        inversion_total = costo_materiales + costo_mano_obra

        precio_mercado = float(entrada_mercado.value) if entrada_mercado.value else 0.0
        margen_deseado = 0.30  # 30% de ganancia sobre el costo
        
        precio_sugerido = inversion_total * (1 + margen_deseado)

        if precio_mercado > 0 and precio_sugerido > precio_mercado:
            venta_final = precio_mercado 
        else:
            venta_final = precio_sugerido

        ganancia_neta = venta_final - inversion_total

        texto_inversion.value = f"${inversion_total:.2f}"
        texto_ganancia.value = f"${ganancia_neta:.2f}"
        texto_presupuesto.value = f"${venta_final:.2f}"

        texto_ganancia.color = ft.Colors.GREEN_ACCENT if ganancia_neta > 0 else ft.Colors.RED

        content.auto_scroll=True
        page.update()

    except (ValueError, TypeError, IndexError):
        texto_presupuesto.value = "Error en datos"
        page.update()

    except (ValueError, TypeError, IndexError):
        texto_presupuesto.value = "Error en datos"
        texto_presupuesto.color = ft.Colors.RED
        page.update()

# ---------------------------------------------Entradas ------------------------------------------ #

  entrada_producto = text_field("Ingrese el nombre del producto", 245, actualizar_calculo)
  entrada_medida = text_field("Ingrese la medida en cm", 225, actualizar_calculo, tipo_teclado=ft.KeyboardType.NUMBER)
  entrada_cantidad = text_field("Ingrese la cantidad", 247, actualizar_calculo, tipo_teclado=ft.KeyboardType.NUMBER)
  entrada_cantidad_arreglo = text_field("Ingrese la cantidad", 222, actualizar_calculo, tipo_teclado=ft.KeyboardType.NUMBER)

  entrada_tiempo = text_field("Ingrese el tiempo en minutos", 220, None, tipo_teclado=ft.KeyboardType.NUMBER)
  entrada_mercado = text_field("Ingrese el precio del mercado", 208, None, tipo_teclado=ft.KeyboardType.NUMBER)
 
  texto_resultado = ft.Text("0.00 m", color=ft.Colors.WHITE, size=15, weight=ft.FontWeight.BOLD)
  texto_presupuesto = ft.Text("$0.00", color=ft.Colors.WHITE, size=20, weight=ft.FontWeight.BOLD)
  texto_inversion = ft.Text("$0.00", color=ft.Colors.WHITE, size=12, weight=ft.FontWeight.BOLD)
  texto_ganancia = ft.Text("$0.00", color=ft.Colors.WHITE, size=12, weight=ft.FontWeight.BOLD)
  titulo = ft.Text("PandiBuy", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.PINK_400, margin=ft.Margin(top=25))
  
  nm = text_field("Material", 100, None)
  pt = text_field("PC", 40, None, tipo_teclado=ft.KeyboardType.NUMBER)
  ct = text_field("CC", 40, None, tipo_teclado=ft.KeyboardType.NUMBER)
  cant = text_field("CANT", 80, None, tipo_teclado=ft.KeyboardType.NUMBER)
  
#---------------------- UI/UX ----------------------#
   
  Tabla_datos = ft.DataTable(
    width=380,
    bgcolor=ft.Colors.GREY_800,
    border_radius=15, 
    column_spacing=15, 
    horizontal_margin = 10,
    horizontal_lines=ft.border.BorderSide(1, ft.Colors.GREY_800),
    columns=[
        ft.DataColumn(ft.Text("Nombre", size=9, weight="bold")),
        ft.DataColumn(ft.Text("Precio\nCompra", size=9, weight="bold")),
        ft.DataColumn(ft.Text("Cantidad\nCompra", size=9, weight="bold")),
        ft.DataColumn(ft.Text("Precio\nUnitario", size=9, weight="bold")),
        ft.DataColumn(ft.Text("Cant. Uso", size=9, weight="bold")), 
        ft.DataColumn(ft.Text("Total", size=9, weight="bold")),
    ],
    rows=[]  # Inicialmente vacío
  )

  content = ft.Column(
    controls=[
      create_h2("Calculadora de Metraje"),
      create_contenedor([
        create_campo(create_h3("Producto"), entrada_producto),
        create_campo(create_h3("Medida (cm)"), entrada_medida),
        create_campo(create_h3("Cantidad"), entrada_cantidad),
        create_campo(create_h3("Cant. Arreglo"), entrada_cantidad_arreglo)
      ]),
      create_contenedor([
        create_campo(
          create_h3("Metraje/Comprar:", color=ft.Colors.WHITE),
          texto_resultado
        ),
      ], color=ft.Colors.GREY_800),
      create_fila([
        create_h2("Materiales"), 
        create_boton_icon(ft.Icons.DELETE, limpiar_campos),
        create_boton_icon(ft.Icons.ADD, actualizar_tabla)
      ]),
      create_column([
        create_contenedor([
        create_fila([
          nm, pt, ct, cant
        ])], color=ft.Colors.GREY_800),
        Tabla_datos
    ], espacio=5),
      create_h2("Información Adicional"),
      create_contenedor([
         create_campo(create_h3("Tiempo (min)"), entrada_tiempo),
         create_campo(create_h3("Precio Mercado"), entrada_mercado)
      ]),
      create_contenedor([
        create_campo(create_h3("Inversión: ", color=ft.Colors.WHITE), texto_inversion),
        create_campo(create_h3("Ganancia: ", color=ft.Colors.WHITE), texto_ganancia),
        create_campo(create_h3("PV: ", color=ft.Colors.WHITE), texto_presupuesto)
      ], color=ft.Colors.GREY_800),
      create_campo(create_boton_icon(ft.Icons.PAYMENTS, presupuesto)),
    ],
    horizontal_alignment=ft.CrossAxisAlignment.START,
    spacing = 10,
    scroll=ft.ScrollMode.HIDDEN,
    expand=True,
  )
  page.add(
    titulo, 
    content
  )
ft.run(main, assets_dir="assets")
