import flet as ft  # Importar la librería Flet

def main(page: ft.Page):  # Función principal de la aplicación
  # Crear campos
  primer_nombre = ft.TextField(label="Nombre", autofocus=True)
  apellido = ft.TextField(label="Apellido")
  saludos = ft.Column()
  
  def clic_del_boton(e):  # Función que se ejecuta al hacer clic en el botón
    saludos.controls.append(ft.Text(f"¡Hola, {primer_nombre.value} {apellido.value}!"))
    primer_nombre.value = ""
    apellido.value = ""
    page.update()
    primer_nombre.focus()

  # Agrega los elementos a la página
  page.add(
      primer_nombre,
      apellido,
      ft.ElevatedButton("¡Saludar!", on_click=clic_del_boton),  # Botón elevado con texto
      saludos,
  )

ft.app(target=main) # Inicia la aplicación de Flet
