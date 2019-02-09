## Le script importe les donnees du csv dans un dataset
## Reste à faire les fonctions pour analyser les résultats pis des beaux petits graphiques en en couleur
import pandas as pd #used to read the dataset
import numpy as np
import matplotlib.pyplot as plt
import os
os.system('cls' if os.name == 'nt' else 'clear')

def printCountries(country):
    print("----------------------------------------number of records by country-----------------------------------------", end="\n\n")
    for i in range(len(country)):
        ndataByCountry = len(dataset[dataset["stateabb"] == country[i]])
        # print(country[i] + ": " +  str(ndataByCountry), end=" | ")
        print ("{:3}: {:3}".format(country[i], ndataByCountry), end=" | ")
        if  not ((i + 1) % 10) :
            print()
            for j in range(109):
                print('-', end='')
            print()

#Contains the data
dataset = pd.read_csv("Datasets/NMC_5_0.csv", na_values="-9")

#Displays the number of records by country
printCountries(dataset["stateabb"].unique())
print()
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

datasetYears = pd.DataFrame(dataset[dataset['year'] > 1900], columns=['stateabb','year','milex'])
datasetYearsPivot = datasetYears.pivot(index='year', columns='stateabb')
datasetYearsPivot.fillna(0, inplace=True)
print(datasetYearsPivot)
datasetYearsPivot.loc['Total'] = datasetYearsPivot.sum()
print(datasetYearsPivot.sort_values(['Total'], axis=1, ascending=False))
datasetYearsPivot.plot(kind='area')
plt.show()


