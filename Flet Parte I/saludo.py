import flet
from flet import Page,TextField,Text,Row,ElevatedButton

def main(page: Page):
    #Atributos Pagina
    page.title='Aplicación Saludo'
    page.vertical_alignment='center'
    
    #Funciones
    def saludar(e):
        lbl_saludo.value = f'¡Hola {txt_nombre.value} esto es Flet!'
        lbl_saludo.update()
    
    #Definir Controles
    txt_nombre = TextField(label='Digite su nombre')
    lbl_saludo = Text()
    
    #Dibujar UI
    row_1 = Row(controls=[
        txt_nombre,
        ElevatedButton(text='Saludar', on_click=saludar)
    ],alignment='center')
    
    row_2 = Row(controls=[
        lbl_saludo
    ],alignment='center')

    page.add(row_1, row_2)

flet.app(target=main)
