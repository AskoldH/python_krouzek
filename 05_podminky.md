# **Podmínky** - If, elif, else

If by se dalo přeložit jako pokud, elif (else if) jako jinak jestli a else jako jinak. Jsou to podmínky, to znamená že pokud platí nějaká rovnost, jestli je něco
pravda, tak se část kódu v podmínce provede (zápis viz ukázky). Podmínky jsou pro nás velice důležité, jelikož můžeme na základě různyých vstupů do programu dělat
různé věci, vykonávat různý kód. Na problematiku podmínek navazuje problematika logických spojek a operátorů, hlavní jsou and, or, not, těm se budeme věnovat
v dalším souboru.

## Ukázka č. 1
V této ukázce se provede jen kód v if větvi, protože podmínka je pravdivá, proměnná cislo je rovna čtyřem, to se i vytiskne. Kdyby proměnná cislo měla
hodnotu např. 6 tak se provede až větev else, jelikož tohle číslo se nerovná ani čtyřce nebo pětce. Rovnost kontrolujeme pomocí dvou označení rovnosti (==).
Hodnota mezi slovem if a dvojtečkou musí být jednoznačně rozhodnutelná, true/false, podle toho se Python rozhoduje. Platí že nejdřív se provede kontola podmínky
větve if, pokud je nepravda tak se kontoluje podmínka větve elif (těch můžeme zapsat i několik za pod sebe), pokud ani elif podmínka neplatí tak se provede 
automaticky kód ve větvi else, tak se nemusí kontolovat
```python
cislo = 4

if cislo == 4:
  print("Číslo je rovno čtyřem.")
elif cislo == 5:
  print("Číslo je rovno pěti.")
else: 
  print("Číslo není rovno pěti ani čtyřem")
```

## Ukázka č. 2
Zapsat můžeme i samotné if, samostatně ale nemůžeme napsat elif nebo else, jejich hodnota pravdivosti se kontroluje až pokud neplatí první podmínka neboli
větev if. V této ukázce platí, že slovo se rovná "hello", takže podmínka je pravdivá tudíž se provede kód v podmínce, vytiskne se slovo "hello". U podmínek
je povinná jen větev if, elif ani else už mít nepotřebujeme.
```python
slovo = "hello"

if slovo = "hello":
  print(slovo)
```

## Ukázka č. 3
Ukázka s více elif větvemi. U čísel můžeme používat nejen jestli jsou čísla rovna, ale i větší nebo menší popřípadě větší a rovna nebo menší a rovna. Zapisujeme
podobně jako v matematice: <, >, <=, >=
```python
cislo = 5

if cislo >= 10:
  print("Číslo je větší nebo rovno číslu 10.")
elif cislo > 7:
  print("Číslo je větší než 10.")
elif cislo < 3:
  print("Číslo je menší než 3.")
else:
  print(cislo)
```

## Ukázka č. 4
Příklad porovnání dvoou čísel za pomocí jedné větve if a jedné větve else.
```python
cislo_1 = 2
cislo_2 = 3

if cislo_1 > cislo_2:
  print("Číslo 1 je větší než číslo 2.")
else: 
  print("Číslo 2 je větší než číslo 1.")
```

 ## Ukázka č. 5
 Příklad porovnání načtených čísel, je to jen lehce upravená verze předchozí ukázky.
 ```python
 cislo_1 = int(input("Zadejte první číslo: "))
 cislo_2 = int(input("Zadejte druhé číslo: "))
 
 if cislo_1 > cislo_2:
  print("První zadané číslo je větší než druhé zadané číslo.")
 else: 
  print("Druhé zadané číslo je větší než první zadané číslo.")
 ```















