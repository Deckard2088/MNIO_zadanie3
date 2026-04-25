# Dawid Wachecki 254890
# Kacper Skoczylas 254864
#Zadanie 3: wariant 1 - Interpolacja Lagrange'a dla węzłów równoodległych

import algorithms as alg
import Wykresy as wyk

#wybór funkcji jako słownik, gdzie kluczem jest numer funkcji, a wartością jest sama funkcja.
def wybranaFunkcja(wybor):
    funkcje = {
        1: alg.funkcja_liniowa,
        2: alg.funkcja_abs,
        3: alg.funkcja_wielomian,
        4: alg.funkcja_trygonometryczna,
        5: alg.funkcja_zlozenie_1,
        6: alg.funkcja_zlozenie_2,
        7: alg.funkcja_zlozenie_3,
    }
    return funkcje.get(wybor)

def nazwaFunkcji(wybor):
    nazwa = {
        1: "y = 2x - 5",
        2: "y = |0.5x + 3|",
        3: "y = 2x^3 - 5x^2 + 2x",
        4: "y = cos(x)",
        5: "y = (2x - 5) + cos(x)",
        6: "y = |0.5x + 3| * cos(x)",
        7: "y = (2x^3 - 5x^2 + 2x) + |0.5x + 3|",
    }
    return nazwa.get(wybor)


def policz_wartosci(funkcja, lista_x):
    lista_y = []
    for x in lista_x:
        lista_y.append(funkcja(x))
    return lista_y


def policz_lagrange(x_lista, x_nodes, y_nodes):
    y_lista = []
    for x in x_lista:
        y_lista.append(alg.wartosc_langrange(x, x_nodes, y_nodes))
    return y_lista


def sprawdz_blad(y1, y2):
    blad = 0
    for i in range(len(y1)):
        roznica = abs(y1[i] - y2[i])
        if roznica > blad:
            blad = roznica
    return blad


def pobierz_wezly(a, b):
    print("\nJAK PODAĆ WEZLY?")
    print("1. Ręcznie - podaj liczbę węzłów, a program zrobi równoodległe")
    print("2. Z pliku - wczytaj położenia węzłów z pliku tekstowego")
    wybor = int(input("WYBÓR: "))

    if wybor == 1:
        n = int(input("PODAJ LICZBĘ WĘZŁÓW: "))
        if n < 2:
            print("Błąd: liczba węzłów musi być co najmniej 2.")
            return None, None
        x_nodes = alg.siatka_argumentow(a, b, n)
        return x_nodes, n

    if wybor == 2:
        sciezka = input("PODAJ ŚCIEŻKĘ DO PLIKU Z WĘZŁAMI: ")
        x_nodes = alg.wczytaj_z_pliku(sciezka)
        if len(x_nodes) < 2:
            print("Błąd: w pliku musi być co najmniej 2 węzły.")
            return None, None
        x_nodes.sort()
        return x_nodes, len(x_nodes)

    print("Błąd: niepoprawny wybór.")
    return None, None


def oblicz_i_narysuj(funkcja, a, b, x_nodes, n, nazwa):
    y_nodes = policz_wartosci(funkcja, x_nodes)

    x_geste = alg.siatka_argumentow(a, b, 1000)
    y_funkcja = policz_wartosci(funkcja, x_geste)
    y_interp = policz_lagrange(x_geste, x_nodes, y_nodes)

    blad = sprawdz_blad(y_funkcja, y_interp)
    print(f"Maksymalny blad interpolacji dla n = {n}: {blad}")

    wyk.rysuj_wykres(
        x_geste,
        y_funkcja,
        y_interp,
        x_nodes,
        y_nodes,
        f"Interpolacja Lagrange'a - {nazwa} | n = {n}",
    )


def main():
    print("================================================")
    print("ZADANIE 3.")
    print("================================================\n")
    print("WYBIERZ FUNKCJĘ")
    #wypisujemy opcje w menu
    for i in range(1, 8, 1):
        print(f"{i}. {nazwaFunkcji(i)}")
    #pobieramy wybór od użytkownika
    wyborFunkcji = int(input("\nWYBRANA FUNKCJA: "))
    if (wyborFunkcji < 1 or wyborFunkcji > 7):
        print("Błąd: wpisano niepoprawny numer.")
        return

    funkcja = wybranaFunkcja(wyborFunkcji)
    if funkcja is None:
        print("Błąd: nie wybrano funkcji.")
        return

    print("================================================\n")
    print("PODAJ PRZEDZIAŁ [a,b]")
    a = float(input("PODAJ WARTOŚĆ 'a': "))
    b = float(input("PODAJ WARTOŚĆ 'b': "))
    if a > b:
        a, b = b, a
    if a == b:
        print("Błąd: przedział nie może mieć zerowej długości.")
        return

    print(f"WYBRANY PRZEDZIAŁ: [{a}, {b}]")
    print("================================================\n")

    while True:
        x_nodes, n = pobierz_wezly(a, b)
        if x_nodes is None:
            continue

        print(f"WYBRANA LICZBA WĘZŁÓW: {n}")
        oblicz_i_narysuj(funkcja, a, b, x_nodes, n, nazwaFunkcji(wyborFunkcji))

        odp = input("Czy chcesz sprawdzic blad dla innej liczby wezlow? (t/n): ")
        if odp.lower() != "t":
            break


if __name__ == "__main__":
    main()