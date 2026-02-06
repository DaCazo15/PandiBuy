import flet as ft

def create_campo(texto, campo=None, margin=ft.Margin(0,0,0,0)):
  if campo is None:
    return ft.Row([texto], alignment=ft.MainAxisAlignment.CENTER, spacing=10, margin=margin)
  return ft.Row([texto, campo], alignment=ft.MainAxisAlignment.CENTER, spacing=10, margin=margin)

def create_column(values, espacio=10):
  return ft.Column(
    controls=values,
    horizontal_alignment=ft.CrossAxisAlignment.START,
    spacing=espacio,
  )

def create_fila(values):
  return ft.Row(
    controls=values,
    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    spacing=None,
    margin=ft.Margin(5,0,5,0)
  )

def create_contenedor(values, color = ft.Colors.WHITE, alto=None, margin=ft.Margin(0,0,0,0)):
  return ft.Container(
    content=create_column(values),
    bgcolor=color,
    padding=ft.Padding(left=10, right=10, top=10, bottom=10),
    border_radius=ft.BorderRadius.all(10),
    width=350,
    height= alto,
    margin=margin
  )

def create_boton_icon(icono, funcion):
  return ft.IconButton(
    icon=icono,
    icon_color=ft.Colors.WHITE,
    bgcolor=ft.Colors.GREY_800,
    hover_color=ft.Colors.GREY_600,
    animate_rotation=True,
    width=80,   
    height=35, 
    on_click=funcion,
    style=ft.ButtonStyle(
      shape=ft.RoundedRectangleBorder(radius=10), 
    )
  )

def create_h2(texto):
  return ft.Text(texto, color=ft.Colors.WHITE, size=15, weight=ft.FontWeight.BOLD)

def create_h3(texto, color=ft.Colors.PINK_700):
  return ft.Text(texto, color=color, size=12, weight=ft.FontWeight.BOLD)

def text_field(placeholder=None, ancho=None, evento=None, tipo_teclado=None):
  return ft.TextField(
    hint_text=placeholder, 
    content_padding=ft.Padding(0,0,0,0), 
    text_align=ft.TextAlign.CENTER,
    bgcolor=ft.Colors.WHITE,
    text_size=12, 
    width=ancho, height=35, 
    cursor_color=ft.Colors.BLUE_GREY_900, 
    border_color=ft.Colors.BLUE_GREY_600, 
    focused_border_color=ft.Colors.BLUE_GREY_900, 
    color=ft.Colors.BLUE_GREY_900, 
    text_vertical_align=ft.VerticalAlignment.CENTER, 
    keyboard_type=tipo_teclado,
    on_change=evento
  )
