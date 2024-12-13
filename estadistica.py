def promedio(lista):
  """
  Calcula el promedio de una lista de numeros
  Parametros
  ----------
  lista : list
      Lista de numeros
  Retorna
  -------
  float
        Promedio de los numeros en la lista
  """
  listaSinNan = []
  for i in lista:
      if i == i:  # Verifica que i no sea NaN
          listaSinNan.append(i)

    # Verificar si la lista está vacía después de eliminar los NaNs
  if not listaSinNan:
      return 0  # Devolver 0 en caso de lista vacía

  suma = sum(listaSinNan)
  promedio = suma / len(listaSinNan)
  return promedio

def mediana(lista):
  """
  Calcula la mediana de una lista de numeros
  Parametros
  ----------
  lista : list
    Lista de numeros
  Retorna
  -------
     Mediana:float
    Mediana de los numeros en la lista
  """
  #eliminar los NANs
  listaSinNan=[]

  for i in lista:
    if i==i:
      listaSinNan.append(i)

  #ordenar lista
  listaSinNan.sort()
  k=len(listaSinNan)
  #determinar si es par o impar
  if len(listaSinNan) % 2 == 0:
    mediana = (listaSinNan[(k // 2) - 1] + listaSinNan[k // 2]) / 2
  else:
    mediana = listaSinNan[k // 2]

  return mediana

def moda(lista):
  """
  Calcula la moda de una lista de numeros
  Parametros
  ----------
  lista : list
    Lista de numeros
  Retorna
  -------
     Moda:float
     val_max:float
    Moda de los numeros en la lista
    valor maximo de frecuencia
  """
  #eliminar los NANs
  listaSinNan=[]
  for i in lista:
    if i==i:
      listaSinNan.append(i)

  categorias=[]
  for v in listaSinNan:
    if v not in categorias:
      categorias.append(v)

  #cuenta frecuencia de categorías
  cuentas=[]
  for c in categorias:
    n=0
    for v in listaSinNan:
      if v==c:
        n+=1
    cuentas.append(n)

  #Encontrar el valor maximo de frecuencia
  i_max=0
  val_max=cuentas[0]
  for i in range(1,len(cuentas)):
    if cuentas[i]>val_max:
      i_max=i
      val_max=cuentas[i]

  modas=[]#se guardan todas las categorias que tengan el mismo numero, numero maximo
  for i in range(len(cuentas)):
    if cuentas[i]==val_max:
      modas.append(categorias[i])
    #retorno la moda
   #moda=categorias[i_max]  , ya no se resporta sola una
  return modas, val_max


def rango(lista):
  """
  Calcula el rango de una lista de numeros
  Parametros
  ----------
  lista : list
    Lista de numeros
  Retorna
  -------
     Rango:float
    Rango de los numeros en la lista
  """
  listaSinNan=[]
  for i in lista:
    if i==i:
      listaSinNan.append(i)

  rango=max(listaSinNan)-min(listaSinNan)
  return rango


def varianza(lista):
  """
  Calcula la varianza de una lista de numeros
  Parametros
  ----------
  lista : list
    Lista de numeros
  Retorna
  -------
     Varianza:float
    Varianza de los numeros en la lista
  """
  listaSinNan=[]
  for i in lista:
    if i==i:
      listaSinNan.append(i)

  prom = promedio(listaSinNan)  # Calculamos el promedio una vez
  suma = sum((i - prom) ** 2 for i in listaSinNan)
  return suma / (len(listaSinNan)-1)

def desviacion_estandar(lista):
  """
  Calcula la desviacion estandar de una lista de numeros
  Parametros
  ----------
  lista : list
    Lista de numeros
  Retorna
  -------
     Desviacion estandar:float
    Desviacion estandar de los numeros en la lista
  """
  listaSinNan=[]
  for i in lista:
    if i==i:
      listaSinNan.append(i)

  desviacion=varianza(listaSinNan)**(1/2)
  return desviacion


def percentiles(lista):
  """
  Calcula los percentiles de una lista de numeros
  Parametros
  ----------
  lista : list
    Lista de numeros
  Retorna
  -------
     Percentil:float
    Percentil de los numeros en la lista
  """
  listaSinNan=[]
  for i in lista:
    if i==i:
      listaSinNan.append(i)

  percentil = []
  n = len(listaSinNan)
  listaSinNan.sort()


  for i, val in enumerate(listaSinNan):
    percentile = (i + 1) / n * 100  # Calcular el percentil para cada valor
    percentil.append(percentile)

  return percentil

  

def iqr(lista):
  """
  Calcula el rango intercuartil de una lista de numeros
  Parametros
  ----------
  lista : list
    Lista de numeros
  Retorna
  -------
     IQR:float
    Rango intercuartil de los numeros en la lista
  """
  listaSinNan=[]
  for i in lista:
    if i==i:
      listaSinNan.append(i)

  listaSinNan.sort()
  percentil=percentiles(listaSinNan)
  n = len(percentil)

  q1_index = int(0.25 * n)  # Índice del percentil 25
  q3_index = int(0.75 * n)  # Índice del percentil 75

  q1 = percentil[q1_index] if q1_index < n else percentil[-1] # Manejar el caso donde el índice está fuera de rango
  q3 = percentil[q3_index] if q3_index < n else percentil[-1]  # Manejar el caso donde el índice está fuera de rango

  # Calcular el IQR
  iqr_val = q3 - q1

  return iqr_val

def mad(lista):
  """
  Calcula la desviacion media absoluta de una lista de numeros
  Parametros
  ----------
  lista : list
    Lista de numeros
  Retorna
  -------
     MAD:float
    Desviacion media absoluta de los numeros en la lista
  """
  listaSinNan=[]
  for i in lista:
    if i==i:
      listaSinNan.append(i)

  prom = promedio(listaSinNan)
  mad = sum(abs(i - prom) for i in listaSinNan) / len(listaSinNan)
  return mad

def covarianza(lista1,lista2):
  """
  calcula la covarianza de dos listas de numeros
  Parametros
  ----------
  lista1 : list
    Lista de numeros
  lista2 : list
    Lista de numeros
  Retorna
  -------
     Covarianza:float
    Covarianza de los numeros en la lista
  """
  lista1SinNan=[]
  lista2SinNan=[]
  for i in lista1:
    if i==i:
      lista1SinNan.append(i)

  for i in lista2:
    if i==i:
      lista2SinNan.append(i)

  if len(lista1SinNan)!=len(lista2SinNan):
    return None

  prom1=promedio(lista1SinNan)
  prom2=promedio(lista2SinNan)


  cova = [(lista1SinNan[i] - prom1) * (lista2SinNan[i] - prom2) for i in range(len(lista1SinNan))]
  covarianza = sum(cova) / (len(cova) - 1)  # Usamos n-1 para estimación insesgada
  return covarianza



def correlacion(lista1,lista2):
  """
  Calcula la correlacion de dos listas de numeros
  Parametros
  ----------
  lista1 : list
    Lista de numeros
  lista2 : list
    Lista de numeros
  Retorna
  -------
     Correlacion:float
    Correlacion de los numeros en la lista
  """
  lista1SinNan=[]
  lista2SinNan=[]
  for i in lista1:
    if i==i:
      lista1SinNan.append(i)
  for i in lista2:
    if i==i:
      lista2SinNan.append(i)

  if len(lista1SinNan) != len(lista2SinNan):
      return None


  covar = covarianza(lista1SinNan, lista2SinNan)
  var1 = varianza(lista1SinNan)
  var2 = varianza(lista2SinNan)

  if var1 == 0 or var2 == 0:  
    return 0

  return covar / (var1 ** 0.5 * var2 ** 0.5)