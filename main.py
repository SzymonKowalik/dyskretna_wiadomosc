import math


def sprawdz_pozycje(pozycja, przyklad):
    """Sprawdza czy pozycja w wyniku jest zerem czy jedynką."""
    dl_czesci = 2 ** pozycja
    polowa_czesci = dl_czesci // 2
    ilosc_czesci = len(przyklad) // dl_czesci

    zmiana = 0
    bez_zmiany = 0

    for i in range(ilosc_czesci):
        czesc = przyklad[i*dl_czesci:(i+1)*dl_czesci]
        for j in range(polowa_czesci):
            if czesc[j] == czesc[j+polowa_czesci]:
                bez_zmiany += 1
            else:
                zmiana += 1
    return '1' if zmiana > bez_zmiany else '0'


def wyzeruj(binarna, miejsca):
    """Zwraca binarną liczbę z nałożoną maską zer."""
    nowa_binarna = ''
    for b, m in zip(binarna, miejsca):
        if m == '0': nowa_binarna += '0'
        else: nowa_binarna += b
    return nowa_binarna


def sprawdz_negacje(wynik, przyklad):
    """Szyfruje wiadomosc bez negacji sprawdzając czy liczba zmian
    jest większa niż dopuszczalna. Wtedy następuje negacje."""
    max_zmiany = 2**(len(wynik) - 2) - 1
    zmiany = 0

    for i in range(2**len(wynik)//2):
        obecne = f"{bin(i)[2:]:0>{len(wynik)}}"
        maska_obecne = wyzeruj(obecne, wynik)
        miejsce_szyfru = str(maska_obecne.count('1') % 2)
        if str(przyklad[i]) != miejsce_szyfru:
            zmiany += 1
            if zmiany > max_zmiany:
                return '1'
    return '0'


def rozwiazanie(przyklad):
    """Zwraca rozwiązanie dla danego przykładu."""
    ilosc_zmiennych = int(math.log2(len(przyklad)))  # + 1 na negacje potem
    wynik = ''
    # Odszyfrowuje wiadomosc
    for zmienna in range(1, ilosc_zmiennych+1):
        wynik = sprawdz_pozycje(zmienna, przyklad) + wynik

    # Dodanie bitu negacji do wyniku
    wynik = sprawdz_negacje(wynik, przyklad) + wynik

    return wynik


def czytaj_plik(sciezka):
    """Odczytuje przykłady z pliku i zwraca je jako listę."""
    with open(sciezka, 'r') as plik:
        zawartosc = [linia.strip() for linia in plik.readlines()[3:]]
    return zawartosc


def rozwiaz_wszystkie(sciezka_in, sciezka_out):
    """Zapisuje wyniki do pliku."""
    przyklady = czytaj_plik(sciezka_in)

    with open(sciezka_out, 'w') as plik:
        for przyklad in przyklady:
            wynik = rozwiazanie(przyklad)
            plik.write(wynik + '\n')


if __name__ == '__main__':
    rozwiaz_wszystkie('wiadomosci/messages7.in.txt', 'wyniki/messages7.out.txt')
    rozwiaz_wszystkie('wiadomosci/messages13.in.txt', 'wyniki/messages13.out.txt')
    rozwiaz_wszystkie('wiadomosci/messages16.in.txt', 'wyniki/messages16.out.txt')
