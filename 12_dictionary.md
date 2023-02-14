# Dictionary - Slovník
* Slovníky jsou další datová struktura pro ukládání a manipulaci s více daty než jen s jednou proměnnou.
* Slovníky v Pythonu poznáme podle složených závorek '{}', podobně jako u vytvoření listu, kdy jsme obsah listu vkládali do hranatých závorek '[]', tak v případě slovníků to bude do složených.
* Do slovníku vkldádáme páry vždy klíče a hodnoty (key - value pairs). Ze slovníku získáváme data pomocí správného klíče, pomocí páru klíč hodnota pak zapisujeme nové páry do slovníku. Ukážeme si to v ukázkách.
* Slovníky můžou na první pohled vypadat zbytečně složitě oproti listům, které už známe, nicméně obojí má své výhody i nevýhody. Výhody slovníků jsou rychlost (pro Python je nesrovnatelně rychlejší získat hodnotu ze slovníku oproti listu) a logičnost zápisu dat.

## Ukázka č. 1 
V této ukázce jsem vytvořil slovník s dvěmi informacemi uvnitř, všimněte si, že pro hodnotu "#ff0000" je klíč "cervena" a pro hodnotu "#00ff00" je klíč "zelena". Celý slovník má pak název barvy.
```python
barvy = {"cervena":"#ff0000", "zelena":"#00ff00"}
```

## Ukázka č. 2
Pomocí jména slovníku, hranatých závorek a správného klíče printíme hodnotu pro klíč "cervena", tedy "#ff0000".
```python
barvy = {"cervena":"#ff0000", "zelena":"#00ff00"}

print(f"Hodnota pro klíč \"cervena\" je: {barvy["cervena"]}.")
```

## Ukázka č. 3
Pomocí jména slovníku, hranatých závorek (do kterých vložíme unikátní klíč pro novou hodnotu) a nové hodnoty můžeme do slovníku vložit novou hodnotu. V tomto případě do slovníku vložíme hodnotu "#0000ff", dostaneme se k ní pomocí klíče "modra".
```python
barvy = {"cervena":"#ff0000", "zelena":"#00ff00"}
print(f"Slovník: {barvy}")

barvy["modra"] = "#0000ff"
print(f"Slovník: {barvy}")
```

## Ukázka č. 4
Pomocí funkcí keys() a values() můžeme zjistit všechny klíče a hodnoty ve slovníku.
```python
barvy = {"cervena":"#ff0000", "zelena":"#00ff00", "modra": "#0000ff"}
print(f"Klíče jsou: {barvy.keys()}.")
print(f"Hodnoty jsou: {barvy.values()}.")
```

## Ukázka č. 5
Klíče jsou jednoduchá datová struktura (String nebo Integer). Hodnota pro daný klíč může být taky String, Integer, Float, atd. ale mohou to být i složitější datové struktury jako například list (s listem ve slovníku pracujeme stejně jako s každým jiným listem). V této ukázce je klíč jméno člověka, hodnota je list obsahující přezdívku, bydliště a telefonní číslo.
```python
lide = {"Josef":["Pepus","Olomouc","789 456 123"], "Lucie":["Tuk","Aš","777 894 567"]}
print(f"Slovník: {lide}")
```

## Ukázka č. 6
Pomocí operátoru 'in' můžeme kontrolovat jestli je hodnota ve slovníku, výsledkem je buď True (hodnota ve slovníku je) nebo False (hodnota ve slovníku není).

```python
barvy = {"cervena":"#ff0000", "zelena":"#00ff00", "modra": "#0000ff"}

print("#00ff00" in barvy)
print("#ffffff" in barvy)
```