## Le script importe les donnees du csv dans un dataset
## Reste à faire les fonctions pour analyser les résultats pis des beaux petits graphiques en en couleur
import pandas as pd #used to read the dataset
import numpy as np
import matplotlib.pyplot as plt
import os
os.system('cls' if os.name == 'nt' else 'clear')

#Contains the data
dataset = pd.read_csv("Datasets/NMC_5_0.csv", na_values="-9")

#Displays the number of records by country
country =  dataset["stateabb"].unique()
print("-----number of records by country-----")
for c in country:
    ndataByCountry = len(dataset[dataset["stateabb"] == c])
    print(c + ": " +  str(ndataByCountry))
    

print()
print("Total Dataset length:",dataset.size)

print("Number of countries:",dataset.nunique()['ccode'])
nullValues = dataset.isnull().any(axis=1)
nullValueCount = 0;
nullValuesIndexes = []
print("-------------------------")
print("Dropping null-values' row ")
print("-------------------------")
for i in range(len(nullValues)):
    if nullValues[i]:
        nullValueCount += 1
        nullValuesIndexes.append(i)
dataset = dataset.drop(nullValuesIndexes)
print("Null values:",nullValueCount)
print("New dataset length:",dataset.size)
