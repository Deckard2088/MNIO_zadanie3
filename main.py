# Dawid Wachecki 254890
# Kacper Skoczylas 254864
# Zadanie 3: wariant 1 - Interpolacja Lagrange'a dla węzłów równoodległych

import algorithms as alg
import Wykresy as wyk

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
        9: alg.funkcja_wielomian_9_stopnia,
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
        9: "y = x^9 - 2x^8 + 3x^7 - 4x^6 + 5x^5 - 6x^4 + 7x^3 - 8x^2 + 9x",
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
    n = int(input("PODAJ LICZBĘ WĘZŁÓW: "))
    if n < 2:
        print("Błąd: liczba węzłów musi być co najmniej 2.")
        return None, None
    x_nodes = alg.siatka_argumentow(a, b, n)
    return x_nodes, n


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
        f"lagrange_{nazwa.replace(' ', '_').replace('/', '_').replace('|', '').replace('^', '').replace('(', '').replace(')', '').replace('=', '').replace('-', '_').replace('.', '_')}_n{n}.png",
    )


def main():
    print("================================================")
    print("ZADANIE 3.")
    print("================================================\n")
    print("WYBIERZ FUNKCJĘ")
    # wypisujemy tylko zdefiniowane opcje w menu
    for i in sorted({1, 2, 3, 4, 5, 6, 7, 9}):
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