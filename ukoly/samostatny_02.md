# Všeaplikace - 50 minut
Vytvotvořte aplikaci, do které se uživatel musí přihlásit heslem (pokud heslo zadá špatně, tak program vypíše že je špatně a ať ho zadá znova), pokud uživatel zadá příkaz "exit" do políčka heslo, tak se program ukončí. Po přihlášení pomocí hesla se dostane uživatel do hlavního menu výběru funkce, kde si vybere co chce dělat dál. 
* První funkcí je animace (vymyslete si konzolovou "animaci" pomocí jednoduchých printů a pomocí funkce sleep -> ukázka kódu níže), čím lepší animace, tím lepší, po ukinčení animace se program vrátí zpět do menu výběru. 
* Jako druhá funkce je hádání čísla, je zadané číslo, které uživatel musí uhodnout, když uživatel zadá při hádání větší číslo, programu mu vypíše, že číslo je moc vysoké, pokud zadá měnší číslo, program vypíše, že číslo je moc malé. Po uhodnutí se aplikace dostává zpět do menu vběru funkcí. 
* Při vybrání třetí funkce si uživatel vybere 5 čísel, program mu vyhodnotí jestli zadané čísla jsou sudá nebo lichá a to vypíše (př. První číslo 4 je sudé, druhé číslo 7 je liché, ...), po dokončení se vrací program do hlavního menu. 
* Čtvrtá funkce je určení aritmetického průměru z 10 čísel, které zadá uživatel, po vyprintění výsledku se dostává program zpět do hlavního menu.
* Pátá funkce je změření délky textu, uživatel může napsat text (i ho vložit) a program mu vypíše kolik znaků obsahuje.

**Při programování nezapomínejte na přehlednost a efektivitu programu, používejte listy, for a while loopy, f-stringy, proměnné pojmenovávejte co nejlépe. Snažte se zamysled nad tím, jestli by něco nešlo napsat lépe. Taky platí, že když něco nevíte jak napsat, tak první možností je se na to podívat z jiného úhlu a zamyslet se, další možností jsou výukové soubory, pak internet neba samozřejmě já.**


```python
# importy dáváme na začátek souboru, kódu
import time  
# počkej na 1s
time.sleep(1)
```