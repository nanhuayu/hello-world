import pandas as pd
wine = pd.read_csv('wine.data',
                   names = ["Cultivator", "Alchol", "Malic_Acid",
                            "Ash", "Alcalinity_of_Ash", "Magnesium",
                            "Total_phenols", "Falvanoids", "Nonflavanoid_phenols",
                            "Proanthocyanins", "Color_intensity", "Hue",
                            "OD280", "Proline"])

print(wine.head())
