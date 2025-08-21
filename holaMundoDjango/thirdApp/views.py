from django.shortcuts import render
from django.http import HttpResponse


def Diccionario(request):
    Estructura = {}
    mono = True
    nro = 1
    for i in range(1,11):
        lista = []
        for j in range(i):
            lista.append(mono)
            mono = not mono 
        Estructura['Elemento'+str(nro)] = lista
        nro /= 10
        return HttpResponse(str(Estructura))