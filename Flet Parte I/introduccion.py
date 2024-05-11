import flet
from flet import Page, TextField, Row, IconButton, icons

def main(page: Page):
    #Instrucciones para crear controles y actulizar la pagina
    page.title = 'Mi primer app en Flet'
    page.vertical_alignment = 'center'
    
    txt_numero = TextField(value='0',width=100,text_align='right')
    
    def sumar_click(event):
        txt_numero.value = int(txt_numero.value) + 1
        page.update()
        
    def restar_click(event):
        txt_numero.value = int(txt_numero.value) - 1
        txt_numero.update()
    

    #Dibujar UI 
    page.add(
        Row(
            [
                IconButton(icon='REMOVE',icon_color="pink600",tooltip="Restar Número", on_click=restar_click),
                txt_numero,
                IconButton(
                            icons.ADD, 
                            icon_color="green",
                            tooltip="Sumar Número", 
                            on_click=sumar_click
                           )
            ],
            alignment='center'
        )
    ) 
#Modo Desktop:
flet.app(target=main)

#Modo Web:
#flet.app(target=main, view=flet.WEB_BROWSER)

#Modo Cel:
#flet.app(target=main, view=flet.AppView)