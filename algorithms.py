from math import cos

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
    return y

def funkcja_trygonometryczna(x):
    # y = cos(x)
    y = cos(x)
    return y


def funkcja_zlozenie_1(x):
    # y = (2x - 5) + cos(x)
    return funkcja_liniowa(x) + funkcja_trygonometryczna(x)


def funkcja_zlozenie_2(x):
    # y = |0.5x + 3| * cos(x)
    return funkcja_abs(x) * funkcja_trygonometryczna(x)


def funkcja_zlozenie_3(x):
    # y = (2x^3 - 5x^2 + 2x) + |0.5x + 3|
    return funkcja_wielomian(x) + funkcja_abs(x)


def funkcja_wielomian_9_stopnia(x):
    # y = x^9 - 2x^8 + 3x^7 - 4x^6 + 5x^5 - 6x^4 + 7x^3 - 8x^2 + 9x
    y = horner(x, [1, -2, 3, -4, 5, -6, 7, -8, 9, 0], 10)
    return y


def siatka_argumentow(a, b,liczba_wezlowa):
    #tworzymy siatkę argumentów, czyli tablicę z n równomiernie rozmieszczonymi punktami w przedziale [a,b]
    #np. dla a=0, b=10, n=5, siatka będzie wyglądać tak: [0, 2.5, 5, 7.5, 10]
    siatka = []
    for i in range(liczba_wezlowa):
        x = a + i * (b - a) / (liczba_wezlowa - 1)
        siatka.append(x)
    return siatka


def wartosc_langrange(x, x_nodes, y_nodes):
    n = len(x_nodes)
    if n != len(y_nodes):
        raise ValueError("x_nodes i y_nodes muszą mieć ten sam rozmiar.")

    suma = 0.0
    for i in range(n):
        licznik = 1.0
        mianownik = 1.0
        for j in range(n):
            if i != j:
                licznik *= (x - x_nodes[j])
                mianownik *= (x_nodes[i] - x_nodes[j])
        suma += y_nodes[i] * (licznik / mianownik)
    return suma

def wartosci_lagrangea(x_lista, x_nodes, y_nodes):
    return [wartosc_langrange(x, x_nodes, y_nodes) for x in x_lista]


def wartosci_funkcji(func, x_lista):
    return [func(x) for x in x_lista]


def maksymalny_blad(y_true, y_approx):
    if len(y_true) != len(y_approx):
        raise ValueError("Listy porównywane do błędu muszą mieć ten sam rozmiar.")
    return max(abs(y_true[i] - y_approx[i]) for i in range(len(y_true)))