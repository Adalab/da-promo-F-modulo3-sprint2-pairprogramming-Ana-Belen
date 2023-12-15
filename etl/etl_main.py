#%%
import pandas as pd
import os
import sys
import numpy as np
# %%
from src import etl_soporte
#%%
clientes = pd.read_csv('clientes.csv')
# %%
productos = pd.read_csv('productos.csv', sep=',', quotechar='"', error_bad_lines=False)
# %%
ventas = pd.read_csv('ventas.csv')
# %%
productos.head()
# %%
exploracion_dataframe(clientes)
# %%
exploracion_dataframe(productos)
# %%
exploracion_dataframe(ventas)
# %%
