## Dane
- N+1 - ilość bitów oryginalnej wiadomości
- x<sub>0</sub>, ..., x<sub>N</sub> - bity oryginalnej wiadomości
- 2<sup>N</sup> - ilość bitów zaszyfrowanej wiadomości
- a - dowolna liczba w zbiorze {1, ..., N}

## Szyfrowanie wiadomości
Formułę logiczną kodującą wiadomość można uprościć do parzystości 1 w wartościowaniu.
Gdy ilość jest parzysta, wtedy wynik wartościowania to 0, gdy nieparzysta - 1.
(Wynika to z działania operatora XOR. Parzysta ilość prawd -> 0, nieparzysta -> 1).
Następnie wynik poddawany jest negacji, jeżeli wartość bitu x<sub>0</sub> = 1, natomiast dla wartości 0 wynik
pozostaje bez zmian. Każdy bit x<sub>1</sub>, ..., x<sub>N</sub> pokazuje czy dana kolumna p<sub>1</sub>, ..., p<sub>N</sub> 
będzie miała bity 1 i 0, (p<sub>a</sub> = 1), czy wszystkie jedynki zostaną wyzerowane (p<sub>a</sub> = 0).
![Szyfrowanie](obrazki/przyklad1.jpg)

## Odszyfrowywanie wiadomości
Każdy bit wyniku x<sub>1</sub>, ..., x<sub>N</sub> da się odszyfrować poprzez porównywanie odpowiadających sobie 
wartościowań, które zmienia co najwyżej dana kolumna<sup>[1]</sup>. Gdy następuje więcej zmian bitów w odpowiadających sobie parach, to wartość x<sub>a</sub> 
jest równa 1, w przeciwnym wypadku 0. Negację natomiast da się określić poprzez odwrócenie bitów 1 na 0 dla każdego wartościowania 
i porównanie czy ilość bitów 0 jest większa niż 1, wtedy x<sub>0</sub> = 0. Gdy ilość 1 jest większa od 0, to x<sub>0</sub> = 1.
Negację można również określić poprzez zaszyfrowanie odkodowanej wiadomości bez negacji i porównanie czy liczba niezmienionych 
bitów jest większa od zmienionych (W ten sposób działa algorytm w pliku *main.py*).

#### <sup>[1]</sup> Porównywanie bitów
Pary do porównania bitów określa się według następującego schematu (w zapisie binarnym kolejnych liczb 
istnieją 2 liczby różniące się 1 bitem):\
Dla każdego x<sub>a</sub> dzielimy zaszyfrowaną wiadomość na bloki długości 2<sup>a</sup> = d, w których porównujemy bity 
b<sub>0</sub>, ..., b<sub>d</sub> następująco:\
b<sub>0</sub> - b<sub>d/2+1</sub>, b<sub>1</sub> - b<sub>d/2+2</sub>, ..., b<sub>d/2</sub> - b<sub>d</sub>
![Odszyfrowywanie](obrazki/przyklad2.jpg)

## Maksymalna ilość zniekształconych bitów
Maksymalnie wiadomość może mieć zmienione 2<sup>N-2</sup>-1 bitów. Wtedy mamy pewność, że nierówność przy ilości par 
bitów zmienionych i niezmienionych będzie taka sama jak w oryginalniej wiadomości (Już przy zmianie 2<sup>N-2</sup> bitów 
natrafiamy na przypadek gdzie ilość par zmienionych i nie są sobie równe. Wtedy nie możemy określić, która wersja była 
oryginalnie zakodowana.)