# While loop (while smyčka)
While, je smyčka, která se provádí dokud platí její podmínka. Jako 
podmínku vkládáme stejně jako u if else statementů určitý výraz, který
může obsahovat i logické operátory. Důležité jsou také klíčová slova continue a break.

## Ukázka č. 1
V tomto případě je podmínka rovna hodnotě True, tím pádem se while
bude vykonávat do nekončna, takové podmínky nedávají smysl, návejte si
pozor na to, jestli vaše podmínka dělá co má! Pozor táké na odsazení,
to co chceme, aby bylo ve while loopu musí být správně odsazené, to co
je na stejné úrovni jako while, už v něm není!
```python
while True:
    print("Ahoj Karle!")
```

## Ukázka č. 2
V této ukázce již provádíme while loop několikrát za sebou a pak už přestane
platit podmínka, tím pádem se dostaneme z while loopu. While proběhne 5x. Zkuste
si projít postupně co se bude dít, je to skutečně 5x?
```python
cislo = 0
while cislo < 5:
    cislo += 1
    
print("Již jsme venku z while!")
print(f"Hodnota proměnné cislo je: {cislo}!")
```

## Ukázka č. 3
Iterace = opakování. Kolikrát se provede funkce print (Když nepočítáme
ten print, který je mimo while), co se bude v ukázce dít?
```python
cislo = 1
while cislo < 10:
    print(f"{cislo}. iterace!")
    cislo += 1
    
print("Již jsme venku z while!")
```

## Ukázka č. 4
V této ukázce smyčka while končí až v případě, že uživatel zadá slovní spojení "Ahoj Karle!".
```python
zadano_uzivatelem = input("Zadejte 'Ahoj Karle!': ") 
while zadano_uzivatelem != "Ahoj Karle!":
    print("Nezadal jsi 'Ahoj Karle!', styď se!")
    zadano_uzivatelem = input("Zadejte 'Ahoj Karle!': ") 
    
print("Správně!")
```

## Ukázka č. 5
Slovo **break** nám ukončí cyklus. Všimněte si nekonečné smyčky, provede se ale jen jednou kvůli break.
```python 
while True:
    print("První iterace!")
    break

print("Breaknuto ven!")
```

## Ukázka č. 5
Slovo continue nám skočí rovnou na konec cyklu a poté se cyklus provede znova, jestli platí podmínka.
```python
cislo = 1
while cislo < 10:
    print(f"{cislo}. Iterace a ", end="")
    
    if cislo % 2:
        print(f"číslo je liché!\n")
        cislo += 1
        continue
    
    print("číslo je sudé!\n")
    cislo += 1

print("Jsme venku ze smyčky.")
```