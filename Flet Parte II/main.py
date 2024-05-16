import flet
import pandas as pd

from flet import *
from data_dolar import obtener_datos

def main(page: flet.Page):
    df_data = obtener_datos()


flet.app(target=main)