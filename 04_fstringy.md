# F-stringy
F-string je jen jinak, zapsaný string, používáme ho pro složitější operace se stringy (texty).
Velice užitěcné jsou pro printování více informací najednou, tabulek atd.

# Ukázka č. 1 
**Rozdíl mezi klasickým stringem a f-stringem.** Pomocí f-stringu je zápis výrazně jednodušší a přehlednější.
Zapisujeme jako f"{nejaka_promenna} a nějaký text", ve složených závorkách můžeme vykonávat i početní 
operace nebo i jinak upravovat proměnné, které chceme tisknout.
```python
# klasický zápis stringu
cislo_a = 5
cislo_b = 7

priklad = str(cislo_a) + " + " + str(cislo_b) + " = " + str(cislo_a+cislo_b)
print(priklad)

# VS

# pomocí f-stringů
cislo_a = 5
cislo_b = 7

priklad = f"{cislo_a} + {cislo_b} = {cislo_a+cislo_b}"      
print(priklad)
```
# Ukázka č. 2
Dva způsoby zápisu f-stringů, prvni je dle mého výrazně lepší, přehlednější, používejte ho.
```python
jmeno = "Pepa"
vek = 12
pozdrav = f"Ahoj, já jsem {jmeno} a je mi {vek}!"            # zapisujeme pomocí f"{nějaká_proměnná}"
print(pozdrav)

# VS

jmeno = "Franta"
vek = 15
pozdrav = "Ahoj, já jsem {} a je mi {}!".format(jmeno, vek) # nebo pomocí "{}".format(nějaká_proměnná)
print(pozdrav)                                        
```
