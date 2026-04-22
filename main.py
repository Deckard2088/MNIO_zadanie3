# Dawid Wachecki 254890
# Kacper Skoczylas 254864
#Zadanie 3: wariant 1 - Interpolacja Lagrange'a dla węzłów równoodległych

import algorithms as alg

#wybór funkcji jako słownik, gdzie kluczem jest numer funkcji, a wartością jest sama funkcja.
def wybranaFunkcja(wybor):
    funkcje = {
        1: alg.funkcja_liniowa,
        2: alg.funkcja_abs,
        3: alg.funkcja_wielomian,
        4: alg.funkcja_trygonometryczna,
    }
    return funkcje.get(wybor)

def nazwaFunkcji(wybor):
    nazwa = {
        1: "y = 2x - 5",
        2: "y = |0.5x + 3|",
        3: "y = 2x^3 - 5x^2 + 2x",
        4: "y = cos(x)",
    }
    return nazwa.get(wybor)
def main():
    print("================================================")
    print("ZADANIE 3.")
    print("================================================\n")
    print("WYBIERZ FUNKCJĘ")
    #wypisujemy opcje w menu
    for i in range(1, 5, 1):
        print(f"{i}. {nazwaFunkcji(i)}")
    #pobieramy wybór od użytkownika
    wyborFunkcji = int(input("\nWYBRANA FUNKCJA: "))
    if (wyborFunkcji < 1 or wyborFunkcji > 7):
        print("Błąd: wpisano niepoprawny numer.")
        return

    print("================================================\n")
    print("PODAJ PRZEDZIAŁ [a,b]")
    a = float(input("PODAJ WARTOŚĆ 'a': "))
    b = float(input("PODAJ WARTOŚĆ 'b': "))
    print(f"WYBRANY PRZEDZIAŁ: [{a}, {b}]")
    print("================================================\n")

    n = int(input("PODAJ LICZBĘ WĘZŁÓW:"))
    print(f"WYBRANA LICZBA WĘZŁÓW: {n}")


if __name__ == "__main__":
    main()