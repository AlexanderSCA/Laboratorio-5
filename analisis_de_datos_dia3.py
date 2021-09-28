# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 22:47:26 2021

@author: Nicole
"""

import numpy as np
import os 
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


#%% cargo todos los .txt
#####################
#### BISMUTO 207 ####
#####################

ruta_carpetas = "Bi207"

nombres_carpetas = os.listdir(ruta_carpetas) 
def buscar_archivos(ruta): 
    archivos_texto = [] 
    archivos       = os.listdir(ruta) 
    for archivo in archivos: 
        if archivo[-4:] == '.txt': 
            archivos_texto.append(archivo) 
    return archivos_texto 
archivo_texto = buscar_archivos(ruta_carpetas)

for i in range(len(archivo_texto)):
    globals()[archivo_texto[i][:-4]] = np.loadtxt(ruta_carpetas + "/" + archivo_texto[i], unpack=True,)

#%%

lista_datos_bismuto = [Bi207_091KV_2006907_intento6, Bi207_091KV_2391941_intento9, 
                       Bi207_091KV_300358, Bi207_091KV_303077_intento5, 
                       Bi207_091KV_3489466_intento3, Bi207_091KV_4678445_intento4, 
                       Bi207_091KV_4995725_intento2, Bi207_091KV_880410_intento8, 
                       Bi207_091KV_intento7, Bi207_091KV__intento7] #el ultimo tenia un corchete que le borre porque si no no me deja leerlo

#%% Junto todos los datos en un solo array 

datos_totales = []

for i in range(len(lista_datos_bismuto)):
    datos_totales = np.append(datos_totales, lista_datos_bismuto[i])

#%% Ploteo la señal

plt.figure(1, figsize=(10,7))
plt.plot(datos_totales)
plt.grid()
plt.show()


#%%
# =============================================================================
# ANÁLISIS DE PICOS
# =============================================================================
elemento = 'Bi207'
umbral = 0.05

Picos = []
N = 1

if N == 1:
    pos = find_peaks(datos_totales, umbral)
    Picos = pos[1]["peak_heights"]
    # Tiempos_picos = tiempos[Picos[0]]
else:
    for ii in range(N):
        pos = find_peaks(datos_totales[ii], umbral)
        for vv, w in zip(pos[0], pos[1]["peak_heights"]):
            Picos.append(w)    
            # Tiempos_picos.append(tiempos[ii][vv])


#%% Grafico el histograma para N capturas

bins= int(round((1+3.322*np.log(len(Picos)))*2*2))

plt.figure(2, figsize=(10,7))
plt.clf()
plt.hist(Picos, bins= bins)
plt.ylabel('Cantidad')
plt.xlabel('Voltaje [V]')
plt.yscale('log')
plt.xlim(0.05, 5.5)
plt.title('Detección de radiación gamma dentro del fuerte de plomo para el '+ elemento)
plt.show()





#%%
###################
#### CESIO 137 ####
###################
ruta_carpetas = "Cs137/DAQ"

nombres_carpetas = os.listdir(ruta_carpetas) 
def buscar_archivos(ruta): 
    archivos_texto = [] 
    archivos       = os.listdir(ruta) 
    for archivo in archivos: 
        if archivo[-4:] == '.txt': 
            archivos_texto.append(archivo) 
    return archivos_texto 
archivo_texto = buscar_archivos(ruta_carpetas)

for i in range(len(archivo_texto)):
    globals()[archivo_texto[i][:-4]] = np.loadtxt(ruta_carpetas + "/" + archivo_texto[i], unpack=True,)

#%% Junto todos los datos en un solo array 

lista_datos_cesio = [Cs137_091KV_206084_toma7, 
                     Cs137_091KV_2290543_toma2, Cs137_091KV_244846_toma8, 
                     Cs137_091KV_2786743_toma5, Cs137_091KV_395097_toma9, 
                     Cs137_091KV_4082951_toma4, Cs137_091KV_534633_toma1] #la toma 3 se guardo vacia asique la borré

datos_totales = []

for i in range(len(lista_datos_cesio)):
    datos_totales = np.append(datos_totales, lista_datos_cesio[i])

#%% Ploteo

plt.figure(1, figsize=(10,7))
plt.plot(datos_totales)
plt.ylabel('Voltaje [V]')
plt.grid()
plt.show()

#%%
# =============================================================================
# ANÁLISIS DE PICOS
# =============================================================================
elemento = 'Ce137'
umbral = 0.05

Picos = []
N = 1

if N == 1:
    pos = find_peaks(datos_totales, umbral)
    Picos = pos[1]["peak_heights"]
    # Tiempos_picos = tiempos[Picos[0]]
else:
    for ii in range(N):
        pos = find_peaks(datos_totales[ii], umbral)
        for vv, w in zip(pos[0], pos[1]["peak_heights"]):
            Picos.append(w)    
            # Tiempos_picos.append(tiempos[ii][vv])


#%% Grafico el histograma para N capturas

bins= int(round((1+3.322*np.log(len(Picos)))*2*2*2))

plt.figure(3, figsize=(10,7))
plt.clf()
plt.hist(Picos, bins= bins)
plt.ylabel('Cantidad')
plt.xlabel('Voltaje [V]')
plt.yscale('log')
plt.xlim(0.05, 5.5)
plt.title('Detección de radiación gamma dentro del fuerte de plomo para el '+ elemento)
plt.show()






#%%
##################
#### SODIO 22 ####
##################
import numpy as np
import os 
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


ruta_carpetas = "Na22"

nombres_carpetas = os.listdir(ruta_carpetas) 
def buscar_archivos(ruta): 
    archivos_texto = [] 
    archivos       = os.listdir(ruta) 
    for archivo in archivos: 
        if archivo[-4:] == '.txt': 
            archivos_texto.append(archivo) 
    return archivos_texto 
archivo_texto = buscar_archivos(ruta_carpetas)

for i in range(len(archivo_texto)):
    globals()[archivo_texto[i][:-4]] = np.loadtxt(ruta_carpetas + "/" + archivo_texto[i], unpack=True,)

#%% Junto todos los datos en un solo array 

lista_datos_sodio = [Na22_091KV_6847718_toma1, Na22_091KV_1615450_toma2, 
                     Na22_091KV_2216609_toma3, Na22_091KV_4036866_toma4, 
                     Na22_091KV_558124_toma5]

# lista_datos_sodio2 = [Na22_091KV_1259925_toma1_tsen8, Na22_091KV_4751878_toma2_tsen8, 
#                       Na22_091KV_1773320_toma3_tsen8, Na22_091KV_1480564_toma4_tsen8, 
#                       Na22_091KV_3949077_toma5_tsen8, Na22_091KV_6539082_toma8_tsen8, 
#                       Na22_091KV_2828249_toma9_tsen8, Na22_091KV_1045528_toma11_tsen8, 
#                       Na22_091KV_4239968_toma12_tsen8, Na22_091KV_426834_toma13_tsen8]

datos_totales = []

# datos_totales2 = []

for i in range(len(lista_datos_sodio)):
    datos_totales = np.append(datos_totales, lista_datos_sodio[i])
    # datos_totales2 = np.append(datos_totales2, lista_datos_sodio2[i])

#%% Ploteo

plt.figure(1, figsize=(10,7))
plt.plot(datos_totales)
plt.ylabel('Voltaje [V]')
plt.grid()
plt.show()

#%%
# =============================================================================
# ANÁLISIS DE PICOS
# =============================================================================
elemento = 'Na22'
umbral = 0.05

Picos = []
N = 1

if N == 1:
    pos = find_peaks(datos_totales, umbral)
    Picos = pos[1]["peak_heights"]
    # Tiempos_picos = tiempos[Picos[0]]
else:
    for ii in range(N):
        pos = find_peaks(datos_totales[ii], umbral)
        for vv, w in zip(pos[0], pos[1]["peak_heights"]):
            Picos.append(w)    
            # Tiempos_picos.append(tiempos[ii][vv])


#%% Grafico el histograma para N capturas

bins= int(round((1+3.322*np.log(len(Picos)))*2*2*2))

plt.figure(3, figsize=(10,7))
plt.clf()
plt.hist(Picos, bins= bins)
plt.ylabel('Cantidad')
plt.xlabel('Voltaje [V]')
plt.yscale('log')
plt.xlim(0.05, 5.5)
plt.title('Detección de radiación gamma dentro del fuerte de plomo para el '+ elemento)
plt.show()












#%%
###################
#### BALIO 133 ####
###################
import numpy as np
import os 
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


ruta_carpetas = "Ba133"

nombres_carpetas = os.listdir(ruta_carpetas) 
def buscar_archivos(ruta): 
    archivos_texto = [] 
    archivos       = os.listdir(ruta) 
    for archivo in archivos: 
        if archivo[-4:] == '.txt': 
            archivos_texto.append(archivo) 
    return archivos_texto 
archivo_texto = buscar_archivos(ruta_carpetas)

for i in range(len(archivo_texto)):
    globals()[archivo_texto[i][:-4]] = np.loadtxt(ruta_carpetas + "/" + archivo_texto[i], unpack=True,)

#%% Junto todos los datos en un solo array 

lista_datos_balio = [Ba133_091KV_toma0_tsen8, Ba133_091KV_toma1_tsen8, 
                     Ba133_091KV_toma2_tsen8, Ba133_091KV_toma3_tsen8, 
                     Ba133_091KV_toma4_tsen8, Ba133_091KV_toma5_tsen8, 
                     Ba133_091KV_toma6_tsen8]

datos_totales = []

for i in range(len(lista_datos_sodio)):
    datos_totales = np.append(datos_totales, lista_datos_sodio[i])

#%% Ploteo

plt.figure(1, figsize=(10,7))
plt.plot(datos_totales)
plt.ylabel('Voltaje [V]')
plt.grid()
plt.show()

#%%
# =============================================================================
# ANÁLISIS DE PICOS
# =============================================================================
elemento = 'Ba133'
umbral = 0.05

Picos = []
N = 1

if N == 1:
    pos = find_peaks(datos_totales, umbral)
    Picos = pos[1]["peak_heights"]
    # Tiempos_picos = tiempos[Picos[0]]
else:
    for ii in range(N):
        pos = find_peaks(datos_totales[ii], umbral)
        for vv, w in zip(pos[0], pos[1]["peak_heights"]):
            Picos.append(w)    
            # Tiempos_picos.append(tiempos[ii][vv])


#%% Grafico el histograma para N capturas

bins= int(round((1+3.322*np.log(len(Picos)))*3*3))

plt.figure(3, figsize=(10,7))
plt.clf()
plt.hist(Picos, bins= bins)
plt.ylabel('Cantidad')
plt.xlabel('Voltaje [V]')
plt.yscale('log')
plt.xlim(0.05, 5.5)
plt.title('Detección de radiación gamma dentro del fuerte de plomo para el '+ elemento)
plt.show()
