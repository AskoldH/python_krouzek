"""
PRINT
Funkce print je základní funkce pro komunikaci s python programem,
díky ní jsme schopni printovat("tisknout", zobrazovat) data a
proměnné z python programu
POZNAMKA KE KOMENTÁŘŮM (nefunkčnímu kódu) -> pro označení komentáře nebo jenom znefunkčnění
daného řádku dáme před něj hashtag "#", pro víceřádkový komentář používáme tři uvozovky na
začátku komentáře a totéž na konci
"""

# ukázka 1 #
print("Ukázka 1") # základní použití

# ukázka 2 #
print("Ukázka\nčíslo2") # "\n" znamená skočení na další řádek

# ukázna 3 #
print("Ukázka 3", end="*") # argument funkce end="něco" nám určuje co se připojí na konec printovaných dat
                           # defaultní je "\n" -> skočí na další řádek

# ukázka 4 #
cislo = 4
print(78, cislo, "Ukázka 4") # printovat můžeme ať už text, čísla nebo proměnné (i listy, tuples, ..., o tom později)
                             # vše oddělujeme čárkami