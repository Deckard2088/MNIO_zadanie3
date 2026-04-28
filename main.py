# Dawid Wachecki 254890
# Kacper Skoczylas 254864
# Zadanie 3: wariant 1 - Interpolacja Lagrange'a dla węzłów równoodległych

import algorithms as alg
import Wykresy as wyk
import re

BLAD_ZERO_TOL = 1e-10

# Wybór funkcji jako słownik, gdzie kluczem jest numer funkcji, a wartością jest sama funkcja.
def wybranaFunkcja(wybor):
    funkcje = {
        1: alg.funkcja_liniowa,
        2: alg.funkcja_abs,
        3: alg.funkcja_wielomian,
        4: alg.funkcja_trygonometryczna,
        5: alg.funkcja_zlozenie_1,
        6: alg.funkcja_zlozenie_2,
        7: alg.funkcja_zlozenie_3,
        8: alg.funkcja_wielomian_9_stopnia,
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
        8: "y = x^9 - 2x^8 + 3x^7 - 4x^6 + 5x^5 - 6x^4 + 7x^3 - 8x^2 + 9x",
    }
    return nazwa.get(wybor)


def pobierz_wezly(a, b):
    n = int(input("PODAJ LICZBĘ WĘZŁÓW: "))
    if n < 2:
        print("Błąd: liczba węzłów musi być co najmniej 2.")
        return None, None
    x_nodes = alg.siatka_argumentow(a, b, n)
    return x_nodes, n


def oblicz_i_narysuj(funkcja, a, b, x_nodes, n, nazwa):
    y_nodes = alg.wartosci_funkcji(funkcja, x_nodes)

    x_geste = alg.siatka_argumentow(a, b, 1000)
    y_funkcja = alg.wartosci_funkcji(funkcja, x_geste)
    y_interp = alg.wartosci_lagrangea(x_geste, x_nodes, y_nodes)

    blad = alg.maksymalny_blad(y_funkcja, y_interp)
    if abs(blad) < BLAD_ZERO_TOL:
        blad = 0.0
    print(f"Maksymalny blad interpolacji dla n = {n}: {blad}")

    wyk.rysuj_wykres(
        x_geste,
        y_funkcja,
        y_interp,
        x_nodes,
        y_nodes,
        f"Interpolacja Lagrange'a - {nazwa} | n = {n}",
        # sanitize file name: replace any character not alnum, dot, underscore or hyphen with underscore
        f"lagrange_{re.sub(r'[^A-Za-z0-9_.-]+', '_', nazwa)}_n{n}.png",
    )


def main():
    print("================================================")
    print("ZADANIE 3.")
    print("================================================\n")
    print("WYBIERZ FUNKCJĘ")
    # wypisujemy tylko zdefiniowane opcje w menu
    for i in sorted({1, 2, 3, 4, 5, 6, 7, 8}):
        print(f"{i}. {nazwaFunkcji(i)}")
    #pobieramy wybór od użytkownika
    wyborFunkcji = int(input("\nWYBRANA FUNKCJA: "))
    if wybranaFunkcja(wyborFunkcji) is None:
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

    szukaj_dalej = True
    while szukaj_dalej:
        x_nodes, n = pobierz_wezly(a, b)
        while x_nodes is None:
            x_nodes, n = pobierz_wezly(a, b)

        print(f"WYBRANA LICZBA WĘZŁÓW: {n}")
        oblicz_i_narysuj(funkcja, a, b, x_nodes, n, nazwaFunkcji(wyborFunkcji))

        odp = input("Czy chcesz sprawdzic blad dla innej liczby wezlow? (t/n): ")
        szukaj_dalej = odp.lower() == "t"


if __name__ == "__main__":
    main()