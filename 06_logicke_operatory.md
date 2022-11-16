# **Logické spojky**

Logické spojky nám dovolují spojovat podmínky a modifikovat podmínky, pravdivé/nepravdivé výrazy, jsou to and (a, a zárověň), or (nebo), not (ne -> negace).

Pravdivostní tabulku pro and, or a not:
|a|b|a and b|
|:-:|:-:|:-:|
|0|0|0|
|0|1|0|
|1|0|0|
|1|1|1|

|a|b|a or b|
|:-:|:-:|:-:|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|1|

|a|not a|
|:-:|:-:|
|0|1|
|1|0|

## Ukázka č. 1
Podmínka if se provede jen když je proměnná cislo větší než číslo 3 **A ZÁROVEŇ** je menší než číslo 10.
```python
cislo = 5

if cislo > 3 and cislo < 10:
  print("Je menší než 10 a větší než 3!")
```

## Ukázka č. 2
Podmínka if se provede jen když je proměnná cislo větší než 3 **NEBO** menší než 0.
```python
cislo = 5

if cislo > 3 or cislo < 0:
  print("Je menší než 0 a větší než 3!")
```

## Ukázka č. 3
Not nám otáčí pravdivostní hodnotu. Podmínka if se provede jen pokud je číslo menší nebo rovno třem.
```python
cislo = 5

if not(cislo > 3):
  print("Číslo je menší nebo rovno třem!")
```

## Ukázka č. 4
Použití logického operátoru or, pokud je zadané slovo Karel nebo Honza tak vyprintíme Ahoj a příslušné jméno, pokud to je Pribiňáček nebo Bueno vyprintíme Dal bych si příslušné slovo.
```python
slovo = int(input("Zadejte jedno slovo: "))

if slovo == "Karel" or slovo == "Honza":
  print(f"Ahoj {slovo}!")
elif slovo == "Pribiňáček" or slovo == "Bueno":
  print(f"Dal bych si {slovo}!")
else:
  print(f"Slovo {slovo} neznám.")
```
