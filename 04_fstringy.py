"""
F-STRING
F-string je jen jinak, zapsaný string, používáme ho pro složitější operace se stringy (texty).
Velice užitěcné jsou pro printování více informací najednou.
"""

# ukázka 1 #
cislo_a = 5
cislo_b = 7
priklad = str(cislo_a) + " + " + str(cislo_b) + " = " + str(cislo_a+cislo_b) # pomocí klasických operací se stringy
print(priklad)

# vs

cislo_a = 5
cislo_b = 7
priklad = f"{cislo_a} + {cislo_b} = {cislo_a+cislo_b}"      # pomocí f stringů to je jednodušší a přehlednější
print(priklad)                                              # do složených závorek můžeme vložit proměnnou
                                                            # ale můžeme tam i používat početní operace nebo i jinak proměnné upravovat

# ukázka 2 #
jmeno = "Pepa"
vek = 12
pozdrav = f"Ahoj, já jsem {jmeno} a je mi {vek}!"            # zapisujeme pomocí f"{nějaká_proměnná}"
print(pozdrav)

# vs

jmeno = "Franta"
vek = 15
pozdrav = "Ahoj, já jsem {} a je mi {}!".format(jmeno, vek) # nebo pomocí "{}".format(nějaká_proměnná), dle mého je lepší první možnost
print(pozdrav)                                              # oba zápisy nám zajistí ale stejné výsledky

