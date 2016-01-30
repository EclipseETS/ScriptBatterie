"""Ce script <<parse>> le fichier text contenant les résultats du cyclage des cellules 
   pour les insérer dans un DataFrame et ensuite déterminer 38 groupes de 11 cellules"""
   
import pandas as pd
import numpy as np
import collections

#Création du dataframe
result=pd.DataFrame(np.nan, index=[], columns=['Salve','Cellule','InternalRes','Capacity'])

file=open('result.txt','r')

#Chaque ligne du fichier est transformé en liste contenant seulement les 
#info nécessaire, puis la liste est ajoutée au dataframe
for num, line in enumerate(file):
    list=line.split(":")
    list[0]=str(list[0])[-1]
    list[1]=str(list[1])[8:]
    list[2]=str(list[2])[7:]
    list[3]=str(list[3])[9:-1]
    result.loc[num]=list
file.close()

#La variable final représente la performance MOYENNE de chaque cellule pour X salve de test
#ex: résistance interne moyenne de la cellule 1 pour 9 salve
final=result.groupby('Cellule')['InternalRes','Capacity'].mean()

#Le dataframe est ordonné avec résistance interne déscendante,
#puis les 418 cellules avec la meilleure capacité sont retenues
final=final.sort_values('Capacity', ascending=False)
final['index'] = range(1, len(final) + 1)
final = final[final['index'] < 418]

#Divise les cellules en 38 groupes
final = final.sort_values('InternalRes')
groups = [final.iloc[i:i+11] for i in range(0, 418, 11)]

groups
