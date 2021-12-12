# Analyse des Beispieldatensatzes 

In diesem Abschnitt soll der Datensatz auf schlechte Daten analysiert werden. Hierbei werden die einzelenen Spalten Schritt für Schritt durchgegangen.
Zunächst soll jedoch darauf hingewiesen werden, dass Datenqualität nur dann bewertet werden kann, wenn man sog. Dataunderstanding hat. D.h. man sollte vorher wissen, um was für Daten es sich handelt und wie diese aufgebaut sind. 


Analysieren wir nun die Daten:

Die erste Spalte ist die ID. 
Die ID ist in der Regel ein Primärschlüssel und sollte daher eindeutig sein. Überprüfe, ob dies zutrifft:

```
print(df['ID'].value_counts())
```{{execute}}

Es zeigt sich die ID 2 ist zweimal vergeben. Dies ist ein Beispiel für schlechte Datenqualität. 

Mit diesem Befehl kann überprüft werden, ob ein Element keine ID hat.
```
print(df[(df["ID"] == None)])
```{{execute}}

Die zweite Spalte ist die Adresse.
Du kannst nun dein Wissen nutzen, um den vorherigen Code anzupassen, sodass du hier testen kannst, ob leere Felder existieren.

Des Weiteren sollten wir schauen, ob jede Adresse aus einer Straße und einer darauffolgenden Hausnummer besteht.
Hierzu verwenden wir follgenden Code:

```
print(df[df.str.match(r'(^[a-zA-Z]* [a-zA-Z]* \d)')==False])
```{{execute}}

Dies ist ein gutes Beispiel, warum Data Understanding wichtig ist, bzw. Datenqualität subjektiv erscheinen kann. In diesem Beispiel sind "gute" Adressen definiert aus 
Straße und Hausnummer, jedoch wäre es vorstellbar, dass man Straße und Hausnummer auch vertauschen kann.

Im letzten Schritt schauen wir uns die Grundstückfläche an. 
Hierfür schauen wir uns das Minimum und Maximum an.

```
print(df['Grundstueckflaeche'].max())
print(df['Grundstueckflaeche'].min())
```{{execute}}

Hierbei ist zu sehen, dass ein negativer Wert existiert. Dies ist ein fehlerhafter Eintrag. 
Jedoch können wir das nur bewerten, da Flächen in der Regel keine negativen Werte einnehmen können.

Alle negativen Flächen lassen sich mit folgendem Befehl anzeigen:

```
print(df[df['Grundstueckflaeche']<0])
```{{execute}}

