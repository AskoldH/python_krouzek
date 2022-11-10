# **Logické spojky**

Logické spojky nám dovolují spojovat podmínky a modifikovat podmínky, pravdivé/nepravdivé výrazy, jsou to and (a, a zárověň), or (nebo), not (ne -> negace).

|a|b|a and b|
|:-:|:-:|:-:|
|0|0|0|
|0|1|0|
|1|0|0|
|1|1|0|

|a|b|a or b|
|:-:|:-:|:-:|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|1|

|a|not a|
|:-:|:-:|
|0|1|
|1|0|

## Ukázka č. 1
```python
cislo = 5

if cislo > 3 and 
```
