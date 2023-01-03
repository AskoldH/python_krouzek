# For loop
For loop je v Pythonu velmi užitečným nástrojem na procházení datových struktur ale i vykonávání určité akce po několik opakování.

Používáme operátor "in", který se dá lehce přeložit jako "v", přiblíženo je to v ukázkách.

**Je důležité pochopit, jak for loop funguje, vše si důkladně vyzkoušejte sami minimálně zkopírovat. zkusit si spustit ale předtím se zkuste ještě zamyslet nad tím, jaký bude výsledek, postupně si to projděte.**

Poznámka: Ve for loopu funguje **continue** a **break** úplně stejně jako u while loopu, nebudu to tady proto opakovat, mějte to ale na paměti, jsou to užitečná klíčová slova v Pythonu.

## Ukázka č. 1
V ukázce je základní for loop s "in" a funkcí range(), funkčnost by se dala popsat jako pro proměnnou i (nepsané pravidlo je, že pojmenováváme proměnnou ve for loopu "i" nejspíš jakožto zkráceninu "index") v rozsahu 5 (počítá se ale od nuly, tudíš rozsah je 0, 1, 2, 3, 4) prověď print proměnné i s pozdravem "ahojda". For loop postupuje postupně, postupuje do té doby, dokud má čím procházet. 

```python
for i in range(5):
    print(f"{i}. ahojda!")    
```

## Ukázka č. 2
Pokud do funkce range doplníme i druhé číslo, tak nám to první udává začátek počítání, druhé pak konec, výsledné procházení je včetně začátečního čísla ale bez toho ukončujícího. For loop bude procházet čísly 10, 11, 12, 13 a 14. 

```python
for i in range(10, 15):
    print(i)    
```

## Ukázka č. 3
Přidáním třetí čísla do funkce range říkáme, že první je stejně jako v předchozí ukázce začátek, druhé je konec ale třetí je step neboli skok, krok,... jedoduše o kolik se posuneme další iterací, opakováním. Stejně jako u předchozí ukázky, procházíme včetně začátečního čísla ale be toho ukončujícího, procházíme tudíž čísli 20, 30, 40, 50, 60, 70.

```python
for i in range(20, 80, 10):
    print(i)    
```

## Ukázka č. 4
V téhle ukázce jsem chtěl demonstrovat, že s promměnou i můžeme pracovat úplně stejně jako s jaoukoli jinou proměnnou se stejným datovým typem. Zkuste si postupně projít, co se bude dít, pak si to ověřte spuštěním snipetu.

```python
for i in range(10):
    print(f"Tohle je {i+1}. iterace a i*5 je {i*5}.")    
```

## Ukázka č. 5
Nemusíme procházet je v rozsahu čísel, nicméně i např. stringy tedy textem (i dalšími strukturami, na to se podíváme v dalším souboru), v proměnné pismeno bude přímo příslušné písmeno ze stringu slovo. Budeme procházet postupně písmeny S, r, a, n, d, i, s, t, a. Jelikož to je charater, text, tak s ním můžu dělat co můžu dělat s textem, tudíš ho můžu třeba násobit.

```python
slovo = "Srandista"
for pismeno in slovo:
    print(pismeno*3)    
```