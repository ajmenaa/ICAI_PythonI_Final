import flet
from flet import *

def main(page: Page):
    page.title='Aplicación Saludo'
    page.vertical_alignment='center'
    
    txt_nombre = TextField(label='Digite su nombre')
    lbl_saludo = Text()
    
    
    row = Row(controls=[
        txt_nombre,
        ElevatedButton(text='Saludar'),
        lbl_saludo
    ],alignment='center')

    page.add(row)

flet.app(target=main)
