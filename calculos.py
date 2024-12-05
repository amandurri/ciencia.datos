
from calculoUnivariado.py import promedio,mediana,moda
from calculoUnivariado.py import rango,varianza
from calculoUnivariado.py import std
from calculoUnivariado.py import percentil,iqr
from calculoUnivariado.py import mad
import math 
import numpy as np

entrada =open("bsc_sel.dat","r")
entrada.readline()

vmag=[]

stype=[]
for lin in entrada:
#hay que agrar un if , oorque hay comillas
    if lin.split()[2]=='""':
        vmag.append(np.nan)
    vmag.append(float(lin.split()[2]))
    stype.append(lin.split[4])
    
entrada.close()

        
print("Moda de tipo espectral: ",moda(stype))
print("Promedio de Vmag:",promedio(vmag))
print("Meidana de Vmag:",mediana(vmag))



print("percentil 1%: ", percnetil(vmag,1))

print(np.nanpercentile(vamg,1))

print("varianza", varianza (vmag))
print("desviacion estandar")
print("ranfo interculatil:",iqr(vmag))
print("mad:", mad(vmag) )














