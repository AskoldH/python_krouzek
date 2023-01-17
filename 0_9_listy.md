# Listy
List je datová struktura, která se objevuje v nespočtu programovacích jazyků, jednoduše se dá říct, že list je objekt, nějaká obálka, do které vkládáme jiné objekty, můžou to být čísla, stringy, nebo i jiný list, vše to ale taky můžeme v jednom listu nakombinovat. 

## Ukázka č. 1
V ukázce vytváříme list s označením jmena, ve kterém jsou tři jména, všimněte si hranatých závorek, díky tomu poznáme, že se jedná o list. Když chceme z listu získat data, v tomto případě jedno z jmen, tudíž string, napíšeme název listu a za něj hranaté závorky, do nich pak index položky z listu, kterou cheme získat. Indexy začínáme počítat od nuly, takže "Pepa" má index 0, "Karel" má index 1 a "Radek" index 2. Print nám tak musí vytisknout "Já jsem Radek!". (Pozn. Můžeme printit samozdřejmě i celé listy, to ale děláme jen pokud chceme vidět celý obsah listu).

```python
jmena = ["Pepa", "Karel", "Radek"]

print(f"Já jsem {jmena[2]}!")
```

## Ukázka č. 2
S listy můžeme dělat nespočet operací, ty nejvíce důležité jsou v ukázce. Vyzkoušejte si co dělá co, je to důležité pro správnou, efektivní práci s listy. Pro shrnutí to jsou fukce **append(hodnota), count(hodnota), insert(index, hodnota), pop(index), remove(hodnota), sort(), len(jmeno_listu**).

```python
jmena = ["Pepa", "Karel", "Radek", "Zuzanka"]
print(f"List vypadá takto: {jmena}")

jmena.append("Pepa")   # přidá hodnotu na konec seznamu
print(f"List vypadá takto: {jmena}")

pocet_pepu = jmena.count("Pepa")) # zjistí počet výskytů zadané hodnoty, vrátí číslo  
print(f"Počet Pepů v listu je: {pocet_pepu}")

jmena.insert(2, "Franta") # vloží hodnotu na pozici v seznamu, první informace v závorce je index (na který se má něco vložit), druhá informace je co se na daný index má vložit

jmena.pop(0)       # odebere prvek z dané pozice (indexu v závorce)
print(f"List vypadá takto: {jmena}")

jmena.remove("Karel")   # odebere první výskyt zadané hodnoty
print(f"List vypadá takto: {jmena}")

jmena.sort()      # seřadí list, záleží čeho to je list    
print(f"List vypadá takto: {jmena}")

delka_listu = len(jmena) # takto zjistíme délku listu
print(f"Délka listu je {delka_listu}!")
```

## Ukázka č. 3
V této ukázce procházíme listem pomocí for loopu. Všimněte si velice dobrého označení proměnných, přesně víme co v nich máme.

```python
jmena = ["Pepa", "Karel", "Radek", "Zuzanka"]

for jmeno in jmena:
    print(f"Jsi {jmena}?")
```