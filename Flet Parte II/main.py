import flet
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


from flet.matplotlib_chart import MatplotlibChart
from flet import *
from data_dolar import obtener_datos

matplotlib.use("svg")

def main(page: flet.Page):
    df_data = obtener_datos()
    print(df_data)

    def dibujar_grafico(data, tipo_cambio):
        # Extraer datos
        entidades = data['Entidad']
        tipo_cambio_valores = data[tipo_cambio]

        # Crear line plot
        plt.
        
    #Definir Controles
    cbx_tipo_cambio = Dropdown(
        options=[
            dropdown.Option('Venta'),
            dropdown.Option('Compra')
        ],
        width=300
    )
    
    cbx_tipo_entidad = Dropdown( # Creo filtro por tio entidad
        width=400
    )
    
    for entidad in df_data['Tipo'].sort_values().unique():  # Cargo Filtro por tipo entidad
        cbx_tipo_entidad.options.append(dropdown.Option(entidad))
    
    btn_graficar = ElevatedButton(text=('Graficar'))
    
    grafico = MatplotlibChart(plt, expand=True)
    
    #Dibujar UI 
    page.add(
        Row(
            [
             cbx_tipo_cambio,
             cbx_tipo_entidad,
             btn_graficar
            ],
            alignment='center'
        ),
        Row(
            [
             
            ],
            alignment='center'
        )
    ) 


flet.app(target=main)