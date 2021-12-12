# Einrichten des Setups

In diesem Abschnitt werden wir die notwenidgen Setups vollziehen.
Hierzu gehört das Importieren der notwendigen Bibliotheken und das Erzeugen eines Datensatzes.


Um anfangen zu können, müssen wir die Bibliotken "Pandas" importieren.
Verwende hierzu folgenden Befehl:


```
python
import pandas as pd
```{{execute}}

Im zweiten Schritt erstellen wir einen Beispieldatensatz. Verwende hierzu follgenden Code:

```
ID = ["1", "2", "3", "4", "2", None, "6"] 
Adresse = [None, "Max Str 2", "Max Str 3", "Min Str 4", "Min Str 5", "Min Str 6", "54693"] 
Besitzer = ["Uhu", "Esel", "Elefant", "Pinguin", "Amsel", "Igel", "Goldfisch"]
Grundstueckflaeche = [40, 30 , 19, 0 , 10000, -40, 20]
Zeitstempel = ["01.01.2020", "01.01.2020", "01.13.2020","24.01.2000","01.01.2020", "6566843", "01.01.2023"]
dict = {'ID': ID, 'Adresse': Adresse, 'Besitzer': Besitzer, 'Grundstueckflaeche': Grundstueckflaeche, 'Zeitstempel': Zeitstempel} 
df = pd.DataFrame(dict) 
df.to_csv('test.csv')
```{{execute}}

Damit hast du ein so genanntes Pandas Dataframe erzeugt. 

Mit 
```
print(df)
```{{execute}}
kannst du dir das Dataframe anschuen

Dieses verhält sich ähnlich wie eine Tabelle.
Mithilfe von Befehlen können die einzelnen Einträge der Tabelle selektiert, verändert oder gelöscht werden. 
Im nächsten Abschnitt wollen diese Operationen nutzen, um die verschiedenen Arten von schlechter Datenqualität zu ermitteln.

