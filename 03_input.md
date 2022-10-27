# Funkce input() a převod na jiný datový typ
Funkce input je důležitá pro komunikaci s uživatelem našeho programu, dovoluje přímo
dostat data od uživatele do programu, uživatel je tam prostě napíše (do konzole). Data pak vkládáme do
proměnné a dál s nimi pracujeme. **Defaultně bude proměnná datový typ string**, pro použití ve výpočtu ji
tudíž musíme konvertovat na datový typ čislo (int).
Funkce na změnu datového typu: **int()** -> měni na celé číslo, **float()** -> mění na desetinné číslo, 
**str()** mění na string, pokud nejdou data převést na daný typ tak kód končí chybou, (např. při převodu 
písmena na číslo -> nelze)


## Ukázka č. 1
Do závorky a uvozovek píšeme co se má zobrazi uživateli, je to nějaká výzva k napsání informací do konzole, 
např. "Zadejte číslo: " 
```python
input("Zadejte číslo: ")
```
 

## Ukázka č. 2
Pro použití načtené hodnoty ji musíme vložit do proměnné, defaultně je datový typ string, takže s 
informací můžeme dělat jen operace, které jsou povolené pro stringy.
```python
nactene_cislo = input("Zadejte číslo: ") # načtenou hodnotu ukládáme do proměnné nactene_cislo
print(nactene_cislo)
```

## Ukázka č. 3
Měnění datového typu. Pokud načtená data nejdou převést, tak nám kód vyhodí chybu. Kód bude nefunkční.
```python
nactene_cislo = int(input("Zadejte číslo: ")) # Změnili jsme z defaulního stringu na číslo (int)

nactene_desetinne_cislo = float(input("Zadejte desetinné číslo: ")) # Změnili jsme na desetinné číslo

nacteny_text = input("Zadejte text: ") # Načetli jsme text

cislo = 45
text = str(45) # Změnili jsme natový typ z číslo (int) na text (str)
```


## Ukázka č. 4
Operace s načtenými daty. Pracujeme s nimi jako s běžnými proměnnými. Platí pro ně vše jako pro běžně
vytvořené proměnné.
```python
nactene_cislo_a = int(input("Zadejte číslo a: "))
nactene_cislo_b = int(input("Zadejte číslo b: "))

nacteny_text = input("Zadejte zprávu uživateli: ")
print(nacteny_text)

soucet = nactene_cislo_a + nactene_cislo_b                  
print(nactene_cislo_a, "+", nactene_cislo_b, "je", soucet)
```