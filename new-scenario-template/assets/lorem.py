import pandas as pd

ID = ["1", "2", "3", "4", "2", None, "6"] 
Adresse = ["Nan", "Max Str", "Max Str", "Min Str", "Min Str", "Min Str", "54693"] 
Besitzer = ["Uhu", "Esel", "Elefant", "Pinguin", "Amsel", "Igel", "Goldfisch"]
Grundstueckflaeche = [40, 30 , 19, 0 , 10000, -40, 20] 	
dict = {'ID': ID, 'Adresse': Adresse, 'Besitzer': Besitzer, 'Grundstueckflaeche': Grundstueckflaeche} 
df = pd.DataFrame(dict) 
df.to_csv('test.csv')