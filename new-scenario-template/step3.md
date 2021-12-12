# Analyse eines Datensatzes

In diesem Schritt werden wir mit einem Beispieldatensatz arbeiten.
Hierzu werden wir die Python Bibliothek "Numpy-Pandas" verwenden.

Im ersten Schritt solltest du daher diese Biblithek importieren.
Verwende hierzu folgenden Befehl.



```
python
print("Hello World")
```{{execute}}

```
lorem.py
```{{execute}}

`import pandas as pd`{{execute}}

`df = pd.read_csv('dataset.csv')`{{execute}}


```
ID = ["1", "2", "3", "4", "2", None, "6"] 
Adresse = ["Nan", "Max Str", "Max Str", "Min Str", "Min Str", "Min Str", "54693"] 
Besitzer = ["Uhu", "Esel", "Elefant", "Pinguin", "Amsel", "Igel", "Goldfisch"]
Grundstueckflaeche = [40, 30 , 19, 0 , 10000, -40, 20] 	
dict = {'ID': ID, 'Adresse': Adresse, 'Besitzer': Besitzer, 'Grundstueckflaeche': Grundstueckflaeche} 
df = pd.DataFrame(dict) 
df.to_csv('test.csv')
```{{execute}}


