#!/bin/python3
import sys
import math
from datetime import datetime
import json



def VectorTexto(vector):
    largo = len(vector)
    retorno = ""
    if largo > 0:
        for x in range(0, largo):
            retorno += "%s" %(vector[x])
    return retorno

def SumaVector(vector, arreglosuma):
    arreglotmp = []
    largo = len(arreglosuma)
    resto = 0
    if largo <= 0:
        arreglosuma = vector
    else:
        largovector = len(vector)
        largoacomulado = len(VectorTexto(arreglosuma))
        largo = 0
        diferencia = 0
        if largoacomulado > largovector:
            largo = largoacomulado
            diferencia = largoacomulado - largovector  
        else:
            largo = largovector

        for x in range(largo - 1, 0-1, -1):
            if x - diferencia >= 0:
                suma = int(vector[x - diferencia]) + int(arreglosuma[x]) + resto
            else:
                suma = int(arreglosuma[x]) + resto
            if suma >= 10:
                resto = 1
                suma = suma - 10
            else:
                resto = 0
            arreglotmp.append(suma)
        if resto > 0:
            arreglotmp.append(resto)
        arreglosuma = [arreglotmp[i-1] for i in range(len(arreglotmp),0,-1)]
        
    return str(VectorTexto(arreglosuma))

def findMedian(arr):
    retorno = []
    lista = sorted(list(set(arr)))
    largo = len(lista)
    total = 0
    sumafinal = ""
    arreglosuma = []
    for x in range(largo):
        sumafinal = SumaVector(str(lista[x]), arreglosuma)
        print(sumafinal)
    
    return 0

if __name__ == "__main__":
    
    arreglotmp = []
    n = 10
    arr = [1,2,3]
    result = findMedian(arr)
    print(result)