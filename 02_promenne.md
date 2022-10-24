# Proměnné a datové typy
Hodnotu nahradíme označením. Je to vyhrazená část paměti počítače
pro naši manipulaci. Do proměnných můžeme přiřadit různé datové typy,
např. text neboli string, charakter neboli jeden znak, číslo, desetinné číslo,
tuple neboli hodnotu true / false nebo listy, slovníky ... o tom později.
Jako jména proměnných nesmíme používat klíčová slova python jako jsou if, del,
while, for ...

# Ukázka č. 1
Proměnná se jmenuje cislo a je jí přiřazena hodnota číslo 12, když použijeme název
proměnné někde v našem kódu, tak to je to stejné, jako kdybychom použili přímo číslo 12,
takže např. funkce print vytiskne právě číslo 12.
```python
cislo = 12  
print(cislo)
```

# Ukázka č. 2
**Pojmenování proměnných** má svá pravidla, používá se tzv. snake case, to znamená že všechna 
písmena musí být malá, bez diakritiky (háčků a čárek), slova se oddělují pomocí podtžítka -> "_", 
jména proměnných by měli být krátké ale výstižné, aby se nám nepletly, když jich tam budeme mít desitky.
```python
pozdrav_uzivatele = "Ahoj karle"
```

# Ukázka č. 3 #
**Datové typy**
```python
charakter = 'a'         # jeden charakter
text = "Pepa"           # charaktery tvoříci string (řetězec, text, slovo)
cislo = 15              # celé číslo
desetinne_cislo = 3.14  # desetinné číslo
provdo_lez = True       # tuple -> pravda (true) nebo nepravda (false), mužeme jen změnit na opačnou hodnotu
```

# Ukázka č. 4 #
**Operace se stringy**, stringy můžeme sčítat a násobit, odčítat nebo dělit už ale ne (nedává to smysl).
```python
text_1 = "Hello"
text_2 = "world"

sectene = text_1 + text_2
print(sectene)

vynasobene = sectene * 2 
print(vynasobene)
```

# Ukázka č. 5 #
**Operace s čísly**, v Pythonu můžeme dělat s čísly víceméně to stejné co v matematice, ať už s desetinnými nebo 
celými. Takže sčítat, odečítat, násobit, dělit, mocniny, zbytek po dělení (lépe řečeno modulo). Pro složitější
operace používáme knihovnu math.
```python
cislo_1 = 4
cislo_2 = 2
soucet = cislo_1 + cislo_2  
rozdil = cislo_1 - cislo_2  
soucin = cislo_1 * cislo_2  
podil = cislo_1 / cislo_2   
mocnina = cislo_1**2         # tahle je na druhou, číslo za '**' znamená na kolikátou
zbytek_po_deleni = 4 % 2    
```
# Ukázka č. 6 #
Určení délky stringů pomocí funkce len(), délku můžeme určovat i například u listů, ty budeme probírat později.
```python
pozdrav_karla = "Ahoj Karle!"
delka_textu = len(pozdrav_karla)
print(delka_textu)
```
