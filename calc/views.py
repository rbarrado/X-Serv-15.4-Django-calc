from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sumador(request, parametro):
    try:
        sumandos = parametro.split('+')
        operando1 = sumandos[0]
        operando2 = sumandos[1]
        suma = int(operando1) + int(operando2)
        return HttpResponse('<h1>Esto es una suma de ' + parametro + ', el resultado es ' + str(suma) + '</h1>')
    except IndexError:
        return HttpResponse('<h1>Error, usa una url: IP:puerto/suma/sumando1+sumando2</h1>')

def restador(request, parametro):
    try:
        rest = parametro.split('-')
        operando1 = rest[0]
        operando2 = rest[1]
        resta = int(operando1) - int(operando2)
        return HttpResponse('<h1>Esto es una resta de ' + parametro + ', el resultado es ' + str(resta) + '</h1>')
    except IndexError:
        return HttpResponse('<h1>Error, usa una url: IP:puerto/resta/numero1-numero2</h1>')

def multiplicador(request, parametro):
    try:
        mult = parametro.split('*')
        operando1 = mult[0]
        operando2 = mult[1]
        multiplicacion = int(operando1) * int(operando2)
        return HttpResponse('<h1>Esto es una multiplicacion de ' + parametro + ', el resultado es ' + str(multiplicacion) + '</h1>')
    except IndexError:
        return HttpResponse('<h1>Error, usa una url: IP:puerto/multi/operando1*operando2</h1>')

def divisor(request, parametro):
    try:
        div = parametro.split('/')
        operando1 = div[0]
        operando2 = div[1]
        division = float(operando1) / float(operando2)
        return HttpResponse('<h1>Esto es una division de ' + parametro + ', el resultado es ' + str(division) + '</h1>')
    except IndexError:
        return HttpResponse('<h1>Error, usa una url: IP:puerto/divison/divisor1/divisor2</h1>')
