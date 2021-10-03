# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 16:05:32 2021

@author: Alexander
"""
# =============================================================================
# Importante: renombrar los datos para facilitar la iteración al momento de cargar los datos.
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def picos (data, umbral):
    b = find_peaks(data, umbral)
    return(b[1]["peak_heights"])

#%% Analisis de picos
elemento = "Bi207"

dato = np.array([])
for ii in range(14):
    print(ii)
    try: #Esto por si algún dato no se guardó o no se cargó bien, como para que pase a leer el siguiente
        y = np.loadtxt('{}'.format(elemento)+'_091KV_toma{}_tsen8.txt'.format(ii))
        dato = np.append(dato, picos(np.abs(y-np.mean(y)), 0.005))
    except:
        pass
    
# dato_2 = np.array([d for d in dato if d>0.005]) #Le pongo el umbral que me interesa

#%%
plt.figure(1, figsize=(7,7))
plt.clf()
plt.plot(np.abs(y-np.mean(y)),'o-', label = 'Señal detectada')
# plt.xlabel('Tiempo [s]')
plt.ylabel('Voltaje [V]')
plt.show()

#%% Grafico el histograma

plt.figure(2, figsize=(6,6))
plt.clf()
n, bins, patches = plt.hist(dato, bins = int(1+3.322*np.log(len(dato)))*16)

ancho = np.diff(bins)[0]
Volts = np.linspace(bins[0]+ancho/2, bins[-1]-ancho/2, num=len(n))

plt.plot(Volts, n, '+')
plt.ylabel('Cantidad')
plt.xlabel('Voltaje [V]')
plt.yscale('log')
plt.suptitle('Detección de radiación gamma fuera del fuerte de plomo para el '+ elemento)
# plt.title('107KV')
plt.show()
