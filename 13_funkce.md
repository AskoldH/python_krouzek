# Funkce - základ
* Funkce je blok kódu, který můžete opakovaně použít v programu. V Pythonu definujete funkci pomocí klíčového slova "def" a následuje název funkce. Poté můžete definovat vstupní argumenty v závorkách.
* Uvnitř funkce můžete provádět různé operace s těmito argumenty a můžete také definovat návratovou hodnotu, kterou funkce vrátí zpět, když je volána.
* Funkci vyvoláme napsáním jejího názvu a za něj vložíme závorky (případné argumenty se umisťují do závorek)
* Funkce slouží k přehlehlednějšímu kódu, schováváme klidně i dlouhé částy kódu do jednoho řádku.Taky díky funkcím můžeme určitý úkon velice jednoduše zopakovat.

## Ukázka č. 1 
V této ukázce máme jednu fuknci s názvem "rekni_ahoj", v ní je jen jeden print, po zavolání funkce (napsání názvu funkce), se provede obsah funkce (vyprintí se "Hello world").Důležíté je si všimnou zápisu. Pro označení použijeme klíčové slovo "def", za ním následuje název funkce a závorky, dvojtečka je za nimi, pod tímto řádkem následuje už blok kódu funckce.
```python
def rekni_ahoj():
    print("Hello world!")

rekni_ahoj()
```


## Ukázka č. 2
V této ukázce přidáváme do funkce "rekni_ahoj" parametr (název "jmeno" v závorce), tento parametr můžeme používát kdekoli ve funkci. Když si funkci vyvoláme, tak zadáme do závorek za název funkce, přesně tím, co tam zadáme, budeme pracovat v bloku kódu funkce.
```python
def rekni_ahoj(jmeno):
    print(f"Ahoj {jmeno}")

rekni_ahoj("Petr")
```

## Ukázka č. 3
V ukázce, ve funkci používám klíčové slovo return pro vrácení hodnoty (v tomto případě True pokud je číslo sudé, False pokud je liché, funkce bool() se používá na převod hodnoty na boolean -> True/False hodnotu). V kódu níže se funkce přímo rovná vrácené hodnotě, tím pádem se můžeme pomocí této hodnoty rozhodnout.
```python
def je_sude(cislo):
    print(f"Číslo je {cislo}.")
    return (not bool(cislo % 2))

if je_sude(7):
    print("Číslo je sudé!")
```
