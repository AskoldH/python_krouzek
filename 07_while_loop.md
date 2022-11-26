# While loop (while smyčka)
While, je smyčka, která se provádí dokud platí její podmínka. Jako 
podmínku vkládáme stejně jako u if else statementů určitý výraz, který
může obsahovat i logické operátory.

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