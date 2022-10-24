"""
PROMĚNNÉ A DATOVÉ TYPY
Hodnotu nahradíme označením. Je to vyhrazená část paměti počítače
pro naši manipulaci. Do proměnných můžme přiřadit různé datové typy,
např. text neboli string, charakter neboli jeden znak, číslo, desetinné číslo,
tuple neboli hodnotu true / false nebo listy, slovníky ... o tom později.
Jako jména proměnných nesmíme používat klíčová slova python jako jsou if, del,
while, for ...
"""

# ukázka 1 #
promenna = 12   # proměnná se jmenuje promenna a je jí přiřazena hodnota číslo 12
print(promenna) # když název promenna použiji tak to je jako když bych použil přímo
                # hodnotu proměnné, tudíž funkce print vytiskne přímo číslo 12

# ukázka 2 #
sude_cislo = 8 # pojmenování proměnných má svá pravidla, používá se tzv. snake case,
               # to znamená že všechna písmena musí být malá, bez diakritiky (háčků a čárek),
               # slova se oddělují pomocí podtžítka -> "_", jména proměnných by měli být
               # krátké ale výstižné, aby se nám nepletly, když jich tam budeme mít desitky

# ukázka 3 #
charakter = 'a'         # jeden charakter
text = "Pepa"           # charaktery tvoříci string (řetězec, text, slovo)
cislo = 15              # celé číslo
desetinne_cislo = 3.14  # desetinné číslo
provdo_lez = True       # tuple -> pravda (true) nebo nepravda (false), mužeme jen změnit na druhou hodnotu

# ukázka 4 #
text_1 = "Hello"
text_2 = "world"
sectene = text_1 + text_2 # stringy můžeme sčítat
vynasobene = sectene * 2  # i násobit, oděčítat nebo dělit ale nikoli
print(sectene)

# ukázka 5 #
cislo_1 = 4
cislo_2 = 2
soucet = cislo_1 + cislo_2  # s čísli můžeme dělat to stejné co v matematice, takže scítat,
rozdil = cislo_1 - cislo_2  # odečítat,
soucin = cislo_1 * cislo_2  # násobit,
podil = cislo_1 / cislo_2   # dělit,
na_druhou = cislo_1**2      # mocniny (tahle je na druhou),
zbytek_po_deleni = 4 % 2    # ale důležité je i dělení se zbytkem, jehož výsledek je zbytek po dělení
                            # složitější operace umí python také, bude už ale potřeba knihovna math (matematiky)

# ukázka 6 #
pozdrav_karla = "Ahoj Karle!"
delka_textu = len(pozdrav_karla) # pomocí funkce len() můžeme změřit, jak je text dlouhý
print(delka_textu)