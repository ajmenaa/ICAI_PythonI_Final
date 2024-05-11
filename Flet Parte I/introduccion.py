import flet
from flet import Page, TextField

def main(page: Page):
    #Instrucciones para crear controles y actulizar la pagina
    page.title = 'Mi primer app en Flet'
    
    txt_numero = TextField()
    
    pass

#Modo Desktop:
flet.app(target=main)

#Modo Web:
#flet.app(target=main, view=flet.WEB_BROWSER)

#Modo Cel:
#flet.app(target=main, view=flet.AppView)