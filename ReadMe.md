Potrzebujemy:

1. Klasa postaci na podstawie której będziemy tworzyć obiekty. Za jej pomocą będziemy tworzyć zarówno postaci gracza, jak i przeciwników. 
2. Klas dziedziczonych po klasie głównej. Osobno dla każdego stworzenia i osobno dla każdej rasy. 
3. Klasy na przedmioty. Główna klasa dla wszystkich przedmiotów + dziedziczone klasy dla ubrań i broni. 
4. Klasa walki. Będzie brała dwa lub więcej obiektów, ustawiała ich w kolejce i umożliwiała interakcje z nimi. 


1. Klasa postaci (ogólna):
* name
* playable (1 jeśli postać jest gracza, 0 jeśli to postać NPC)
* attitude (jeśli grywalna = 1 to 0, w innym przypadku: jeśli wroga = -1, neutralna =1 pozytywna = 2-100)
* is_alive (jeśli -1 to znaczy, że nie żyje; jeśli 1 to znaczy, że żyje; jeśli 0 to jest w stanie agonii)
* base_attack = 1

2. Klasa postac_aktywna, dziedziczy z klasy postaci:
poza tym co odziedziczy z klasy postaci:

* Szansa na unik
* Szansa na sparowanie
* Odporność na magię światła
* Odporność na magię cienia
* Odporność na magię arcane
* Odporność na magię wody
* Odporność na magię oginia
* Odporność na magię natury
* Szansa na uderzenie krytyczne
* HP
* Inicjatywa
* Szansa na trafienie I atak
* Unik
* Skupienie
* Precyzja
* Siła

Dwie metody:
atakuj(typ_ataku (któraś ze szkół magii lub fizyczne),obrażenia )
unikaj()

3. Klasa postaci dziedziczy z klasy przeciwnik
* Klasa
* Specjalizacja
* Przydomek
* Poziom
* Jezyki
* Umiejętności

- lista_ekwipunku[obiekty_klasy_przedmiot]

Metody (umiejętności)