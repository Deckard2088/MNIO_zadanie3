#ZGADZA SIE, PODJEBAŁEM KOD SAMEMU SOBIE Z ZADANIA 1.
from cmath import cos

def horner(x, tablica_wspolczynnikow, dlugosc_tablicy):
    #Czyli zamiast np. y = 4*x*x*x + 3*x + 5 podaje się funkcje wielomian z argumentami: x, [4,0,3,5], 4
    y = tablica_wspolczynnikow[0]
    for i in range(1,dlugosc_tablicy,1):
        y = tablica_wspolczynnikow[i] + x * y
    return y

def funkcja_liniowa(x):
    #y = 2x - 5
    y = 2*x-5
    return y

def funkcja_abs(x):
    #y = |0.5x + 3|
    y = abs(0.5*x + 3)
    return y

def funkcja_wielomian(x):
    # y = 2x^3 - 5x^2 + 2x
    y = horner(x, [2, -5, 2, 0], 4)
    return 0

def funkcja_trygonometryczna(x):
    # y = cos(x)
    y = cos(x)
    return y
