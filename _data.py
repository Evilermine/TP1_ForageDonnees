## Le script importe les donnees du csv dans un dataset
## Reste à faire les fonctions pour analyser les résultats pis des beaux petits graphiques en en couleur
import pandas as pd #used to read the dataset
import numpy as np
import matplotlib.pyplot as plt

#Contains the data
dataset = pd.read_csv("Datasets/NMC_5_0.csv", na_values="-9")

print("Loading dataset...")
print(dataset[0:10])
print("dataset loaded !")

# CAN=dataset[0:]

# plt.scatter(CAN[0:]["upop"], CAN[0:]["pec"])
# plt.show()

print()
print("Dataset length:",dataset.size)

# Finding the number of countries
print("Number of countries:",dataset.nunique()['ccode'])

# Finding null values and counting
nullValues = dataset.isnull().any(axis=1)
nullValueCount = 0;
for i in range(len(nullValues)):
    if nullValues[i]:
        nullValueCount += 1
print("Null values:",nullValueCount)
