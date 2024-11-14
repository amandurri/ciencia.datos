def promedio(vals_in):
  """
  calcula el promedio de una lista de números
  Parámetros
  ----------
  vals_in : list
    lista de números
  Retorna
  -------
    promedio : float
    promedio aritmetico de los números
  """
  vals=[]
  for v in vals_in:
    if math.isfinite(v):
        vals.append(v)
    
    
  promedio=sum(vals_in)/len(vals_in)
  return promedio

def mediana(vals_in):
"""

clacula la mediana de uanlista de numeros.
Detecta y elimina valores NaN
parametros
--------
vals: lista
	LISTA con los nuemros
reotorna
median: float
	(la mediana de los numeros excluyendo NaNs)

"""
    




#Eliminamos los valores que sean Nan

	vals=[]
	for v in vals_in:
		if math.isfinite(v):
			vals.append(v)

#ordenar lista
	vals.sort()
     #determinar si es par o impar 
	if len(vals)%2!=0:
		k=len(vals)//2 #valor de al medio 
		mediana=vals[k]

	else:
		k=len(vals) //2  # si ni es impas se va a tomar el del medio mas uno
		mediana= (vals[k-1] +vals[k])/2.0
		

    return mediana
    
    
    
    
def moda(vals):
"""
CAlcular la moda de una lista conteniendo una variable categòrica nominal

Paràmetros
-------
vals:list
    lista con las cateforìas 
    
    retorna
    ------
   moda:str
   la moda de la muestra 

"""
#encontrar conjunto de elemtos unicos 

    categorias=
        for v in vals:
            if v not in categorias:
                categorias.append(v)
        
        
    #obtener el numero de cuentas en la muestra 
    #para cada una de la s categorias
    
    cuentas=[]
    for c in categorias:
        n=0
        for val in vals:
            if val==c:
                n=n+1
        cuentas.append(n)


#encontrar la posiciòn del valor de la lista con el maximo de cuenta
#guess and check
    i_max=0
    val_max=cuentas[0]
    for i in range(1,len(cuentas)):
        if cuentas[i]>val_max:
            i_max=i
            val_max=cuentas[i]
            
            
            
    #Determinar todas lass categorias que tenga el numero maximo de cuetas, mas de una moda 
    #val_max dice qcual es el valor maximo en la tabla de frecuencia
    modas=[]     #se guardan todas las categorias que tengan el mismo numero, numero maximo
            
    for i in range(len(cuentas)):
        if cuentas[i]==val_max:
            modas.appen(categorias[i])
            
        
        
        
        
    #retorno la moda
    #moda=categorias[i_max] # ya no se reporta sola una 
    return modas
    


def rango(vals_in):
"""
Calcula el rago de la lista 
Detecta y elemina los none

paprametrso
-------
vlas:lista 
LISTA CON LOS NUMEROS

RETORNA
---------
rango:float 
    rango e los numeros (excluyendo NANs)
 
"""
#eliminar los NANs
 vals=[]
	for v in vals_in:
		if math.isfinite(v):
			vals.append(v)
			
	#determinar maximo y minimo desde 0		
    #forma 2  gues an check, adivino luego resctifico
    minimo=vals[0]
    maximo=[0]
    for v in vals:
        if v<minimo:
            minimo=v
        if v>maximo:
            maximo=v
            
			
    return maximo-minimo 
    #return max(vals)-min(vals) #forma 1 con funciones 
    

def varianza(vals_in):
"""
determina la variaza 
elimina y detenca los nans 
 parametro 
 vals=lista 
 lista con los numeros 
 
 retorna 
 varianza:float
 varianza de los numeros (excluyendo los nansn)

"""
#eliminamos los valores que sean NANs 
    vals=[]
    for v in (vals_in):
        if math.isfinite(v):
                vals.append(v)
                
                
    #estimar promedio            
    promedio=promedio(vals)
    
    #estimamos las desviaciones cuadraticas medias
    dcm=[]
    for v in vals:
        dcm.append((v-promedio)**2)
    
    #calculo varianza 
    varianza= sum(dcm/len(vals))
    return varianza

def std(vals_in):

"""
calcula la desaviacion estandar y elimina los nan
vals=lista que contiene los valores 
"""
 
    #eliminamos los valores que sean NANs 
    vals=[]
    for v in (vals_in):
        if math.isfinite(v):
                vals.append(v)
                
    #estimamos las desviaciones cuadraticas medias
    dcm=[]
    for v in vals:
        dcm.append((v-promedio)**2)
    
    #calculo varianza 
    varianza= sum(dcm/len(vals))
        
    
    return varianza **1/2
        
    
#funcion de percentiles y rango intercuartìlico

def percentiles(vals_in):
    percentil=[]
    percentiles=len(vals_in)/100
    for i in vals_in:
    
    
    return percentil
        

def iqr(vals_in): 
"""
calcule el rango intercualrtilico. Ignora nan
parametros
---------
vals: list
    lista con los valores
    
retorna
-------
IQR: float
 el rango interculatiico 
"""
 #eliminar los nan
    vals =[]
    for v in (vals_in):
        if math.isfinite(v):
                vals.append(v)
 
	

    iqr=percentil(vals,75)-percentil()
	
    return iqr 

def mad(vals_in):
	"""
Calcula el mad de una serie de 

parametros
---------
vals: list
lista con los 
"""	
#leer la fila y graficar 





























    
