# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 01:04:56 2021

@author: Nicole
"""
import numpy as np
import os 

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
    globals()[archivo_texto[i][:-4]] = np.loadtxt(ruta_carpetas + "/" + archivo_texto[i],skiprows=4, unpack=True,)
    