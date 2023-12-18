#%%
import pandas as pd
import os
import sys
import numpy as np
import mysql.connector
# %%
from src import bbdo_soporte

#%%
bbdo_soporte.creacion_bbdd_tablas("AlumnaAdalab", 'clientes')
# %%
