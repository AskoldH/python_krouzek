# Funkce print()
**POZNAMKA KE KOMENTÁŘŮM (nefunkčnímu kódu)** -> pro označení komentáře nebo jenom znefunkčnění
daného řádku dáme před něj hashtag "#", pro víceřádkový komentář používáme tři uvozovky na
začátku komentáře a totéž na konci.

Funkce print je základní funkce pro komunikaci s python programem,
díky ní jsme schopni printovat("tisknout", zobrazovat) data a
proměnné z python programu

## Ukázka č. 1
Základní použití funkce print().
```python
print("Ukázka 1")
```


## Ukázka č. 2
Znak \n v řetězci (textu) znamená skočení na nový řádek. (\n jako new line).
```python
print("Ukázka\nčíslo2")
```


## Ukázka č. 3
Argumentem funkce end="něco" určujeme co máme vytisknout na konec řetězce,
defaultně je end="\n", tudíž nám každý print začíná na novém řádku.
```python
print("Ukázka 3", end="*")
```


## Ukázka č. 4
Printovat můžeme ať už text, čísla, proměnné (o proměnných se 
budeme bavit v dalším souboru)i další datové typy, vše oddělujeme čárkami.
```python
cislo = 4
print(78, cislo, "Ukázka 4")
```
