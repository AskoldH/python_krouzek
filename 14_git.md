# Git - GitHub
* Git je verzovací software, což znamená, že postupně "commitujeme" (od slova commit -> potvrdit, poslat) nové změny do Gitu, kde se ukládají verze o jednotlivých verzích, co se změnilo, autor atd. Git umožňuje sledovat postup při programování projektu, "verzovat ho", pokud bychom se chtěli vrátit na dřívější verzi kódu, tak to není problém. Složka, do které se ukládají všechny soubory s kódem i soubory s dodatečnými informacemi se nazývá repozitář (repository). 
* GitHub slouží pro ukládání repositářů na cloudový server, tyto repositáře jsem pak členům, kteří k nim mají přístup, dostupné odkudkoli. To ulehčuje kolaboraci několika programátorů (všichni dělají nějaké změny, pracují na nových funkcích, ...), jelikož výsledný kód je na jednom místě.
* Git a GitHub umí několikanásobně víc, než jsem popsal, tohle je jen úplný základ.
___

## Jak zprovoznit GitHub repositář (Windows)
* Budeme používat VSCode, také se předpokládá, že máte založený GitHub účet.
* Nainstalujte si Git ze stránek: https://git-scm.com/downloads
* Projděte klasickou klikací instalačkou, správné nainstalování můžeme ověřit pomocí příkazu "git --version" zavolanému v příkazovém řádku, který nám zobrazí verzi nainstalovaného Gitu.
* Musíme si nastavit ještě jméno a heslo, budou sloužit jako identifikace pro to, kdo jaký commit (změnu) udělal. Použijeme příkazy git config --global user.name "Naše vybrané jméno" a git config --global user.email "náš@email.com". Ideální je si nastavit jméno a email stejný, jako máme na GitHub účtu.
```
git config --global user.name "Naše vybrané jméno"
git config --global user.email "náš@email.com".
```
* Ve VSCodu by jsme měli mít připravené funkce source control (správce zdrojového kódu) v levém panelu. Užitečná jsou i doplňující rozšíření jako Git Graph nebo GitHub rozšíření. Pomocí klávesové zktratky "ctrl+shift+p" se dostaneme do "ovládacího řádku" ve VSCodu, vyhledáme "git clone".
* Vybereme, že chceme naklonovat git repozitář z externího (remote) zdroje. VSCode by nás pak měl vyzvat k přihlášení se do našeho GitHub účtu v prohlížeči, tímto propojíme VSCode s naším GitHub učtem. Pokud se přihlášení nezdaří, následujte doporučení VSCode (nejspíš totiž vyjede okénko s nabízeným řešením).
* Po propojení VSCodu s GitHub můžeme provedené změny commitnout a pushnout (jednoduše nahrát) do našeho repozitáře na GutHubu.