"""
INPUT
Funkce input je důležitá pro komunikaci s uživatelem našeho programu, dovoluje přímo
dostat data od uživatele do programu, uživatel je tam prostě napíše. Data pak vkládáme do
proměnné a dál s nimi pracujeme. Defaultně bude proměnná datový typ string, pro použití ve výpočtu ji
tudíž musíme konvertovat na datový typ čislo.
Funkce na změnu datového typu: int() -> měni na celé číslo, float() -> mění na desetinné číslo, str() mění na string,
pokud nejdou data převést na daný typ tak kód končí chybou, (př. při převodu písmena na číslo -> nelze to prostě lul)
"""

# ukázka 1 #
input("Zadejte číslo: ") # do závorky a uvozovek píšeme co se má zobrazit uživateli,
                         # jaká výzva, tady je např. zadejte číslo

# ukázka 2 #
nactene_cislo = input("Zadejte číslo: ") # načtenou hodnotu ukládáme do proměnné nactene_cislo
print(nactene_cislo)                     # to ale ještě není datový typ číslo, je to např. "5" a my chceme 5

# ukázka 3 #
nactene_cislo = int(input("Zadejte číslo: ")) # načtenou hodnotu měníme na datový typ int (celé číslo) pomocí funkce
                                              # int(), !! Pokud uživatel nezadal číslo, takže např. 4 ale zadal např. písmeno "a" tak
                                              # nám kód skončí chybou, jelikož písmeno na datový typ číslo převést nemůžeme

# ukázka 4 #
nactene_cislo_a = int(input("Zadejte číslo a: "))
nactene_cislo_b = int(input("Zadejte číslo b: "))
nacteny_text = input("Zadejte zprávu uživateli: ")

soucet = nactene_cislo_a + nactene_cislo_b                  # s načtenými hodnotami pracujeme jako s běžnými proměnnými,
print(nactene_cislo_a, "+", nactene_cislo_b, "je", soucet)  # platí pro ně vše co pro proměnné, můžeme je samozřejmě i printit
print(nacteny_text)