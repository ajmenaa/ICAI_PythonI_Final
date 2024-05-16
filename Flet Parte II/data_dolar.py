import pandas as pd

def obtener_datos():
    # Realizamos un scrapping de una tabla de la tabla BCCR
    data = pd.read_html('https://gee.bccr.fi.cr/IndicadoresEconomicos/Cuadros/frmConsultaTCVentanilla.aspx', encoding='utf-8', decimal=',', thousands='.')
    
    data = data[2].copy()

    # Extraer la primera fila del DataFrame 'data' y asignarla a 'primera_fila'
    primera_fila = data.iloc[0]
    data.columns = primera_fila
    # Renombrar las columnas de 'data' usando los valores de 'primera_fila' como nuevos nombres
    data.rename(primera_fila, axis=1, inplace=True)
    # Eliminar la primera fila de 'data'
    data.drop(0, inplace=True)
    # Renombramos la primera columna para que sea más fácil consultarla
    data.rename(columns = {'Tipo de Entidad':'Tipo'}, inplace=True)
    data.rename(columns = {'Diferencial Cambiario':'Diferencial'}, inplace=True) 
    data.rename(columns = {'Entidad Autorizada':'Entidad'}, inplace=True)
    # Remplazar valores NaN con el último valor no nulo en la misma columna
    data['Tipo'].ffill(inplace=True)
    #Eliminar la ultima fila vacia
    data.drop(len(data) , inplace=True)
    # Seleccionar columnas numéricas
    columnas_numericas = ['Compra', 'Venta', 'Diferencial']
    # Convertir columnas numéricas con manejo de errores
    data[columnas_numericas] = data[columnas_numericas].apply(pd.to_numeric, errors='coerce')
    
    return data