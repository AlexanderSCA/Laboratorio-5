# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 10:52:07 2021

@author: Publico
"""

from instrumental import AFG3021B, TDS1002B
import numpy as np
import time
import matplotlib.pyplot as plt

#%%

rm = visa.ResourceManager()

instrumentos = rm.list_resources()

#%%

gen = AFG3021B('USB0::0x0699::0x0346::C034166::INSTR')
osc = TDS1002B('USB0::0x0699::0x0363::C065089::INSTR')


gen.setFrequency(10)

frec = gen.getFrequency()
print(frec)

#%%

# del osc, el channel 1 es el gen func y el 2 es la salida
channel=1
scale = 100e-3

osc.set_channel(channel,scale)


gen.setAmplitude(0.5)

ampli = gen.getAmplitude()
print(ampli)
#%% osciloscopio channel 1

channel=1

osc.get_time()
osc.set_time(scale = 1e-3)
#osc.set_channel(1,scale = 2)
tiempo, data = osc.read_data(channel)
plt.figure()
plt.plot(tiempo,data)
plt.xlabel('Tiempo [s]')
plt.ylabel('Voltaje [V]')

#%% barrido 

frec1 = 0.5
frec2 = 30
N = 50
frecuencias = np.linspace(frec1,frec2,N)

channel = 2

data = []
data_ch1 = []
for i in range(len(frecuencias)):
    if (frecuencias[i] <= 2):
         osc.get_time()
         gen.setFrequency(frecuencias[i])
         osc.set_time(scale = 0.1)
         time.sleep(2)
         data.append(osc.read_data(channel))
         data_ch1.append(osc.read_data(1))
         print(frecuencias[i])
    else:
         osc.get_time()
         gen.setFrequency(frecuencias[i])
         osc.set_time(scale = 0.1)
         time.sleep(0.2)
         data.append(osc.read_data(channel))
         data_ch1.append(osc.read_data(1))
         print(frecuencias[i])

#%%

#Vpp = np.array([np.max(dato)-np.min(dato) for dato in data[:][1]]
Vpp = [np.max(dato[1]) - np.min(dato[1]) for dato in data]
Vpp_ch1 = [np.max(dato[1]) - np.min(dato[1]) for dato in data_ch1]

plt.plot(frecuencias,Vpp,'o')
#plt.plot(data[1][0],data[1][1])
plt.xlabel('Frecuencias [Hz]')
plt.ylabel('Voltaje [V]')

#%%
channel=2

osc.get_time()
osc.set_time(scale = 200e-3)
osc.set_channel(channel,scale)
tiempo, data = osc.read_data(channel)
plt.plot(tiempo,data)
plt.xlabel('Tiempo [s]')
plt.ylabel('Voltaje [V]')

#%% cuadrada
osc.write("SOURce1:FUNCtion:SHAPe SQUare")
