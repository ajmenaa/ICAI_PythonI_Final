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
        plt.figure(figsize=(20,10))
        plt.plot(entidades,tipo_cambio_valores, marker='o',linestyle='-',color='g')
        
        #Personalizar el grafico = plot
        plt.xlabel('Entidades Financieras')
        plt.ylabel(f'Tipo Cambio {tipo_cambio}')
        plt.title(f'Tipo cambio {tipo_cambio} en colones por Dolar')
        
        plt.xticks(rotation=90)
        plt.grid(True)
        plt.tight_layout()
        return plt
    
    def graficar_click(event):
        tipo_cambio_seleccionado = cbx_tipo_cambio.value 
        if sw_ordenar.value == True:
            df_data.sort_values(by='Compra',inplace=True);
        else:
            df_data.sort_values(by='Entidad',inplace=True);
        if cbx_tipo_entidad.value == 'TODOS':            
            grafico.current = MatplotlibChart(dibujar_grafico(df_data,tipo_cambio_seleccionado))
        else:
            data_filtrado = df_data[df_data['Tipo'] == cbx_tipo_entidad.value]
            print(data_filtrado)
            grafico.current = MatplotlibChart(dibujar_grafico(data_filtrado,tipo_cambio_seleccionado))
        grafico.update()
    #Definir Controles
    cbx_tipo_cambio = Dropdown(
        options=[
            dropdown.Option('Venta'),
            dropdown.Option('Compra')
        ],
        width=300,
        on_change=graficar_click
    )
    
    cbx_tipo_entidad = Dropdown( # Creo filtro por tio entidad
                                options=[dropdown.Option('TODOS')],
        width=400,
        on_change=graficar_click
    )
    
    for entidad in df_data['Tipo'].sort_values().unique():  # Cargo Filtro por tipo entidad
        cbx_tipo_entidad.options.append(dropdown.Option(entidad))
    
    btn_graficar = ElevatedButton(text=('Graficar'), on_click=graficar_click)
    
    grafico = MatplotlibChart(
        dibujar_grafico(df_data.sort_values(by='Entidad'),'Venta'),
        expand=True)
    
    
    cbx_tipo_cambio.value = 'Venta'
    cbx_tipo_entidad.value = 'TODOS'
    
    sw_ordenar = Switch(label="Ordenar datos", value=False, on_change=graficar_click)
    #Dibujar UI 
    page.add(
        Row(
            [
             cbx_tipo_cambio,
             cbx_tipo_entidad,
             sw_ordenar
            ],
            alignment='center'
        ),
        Row(
            [
             grafico
            ],
            alignment='center'
        )
    ) 


flet.app(target=main)