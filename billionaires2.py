import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#the top 10 billionaires according to their NetWorth:

data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Billionaire.csv")
print(data.head())

df = data.sort_values(by = ["NetWorth"], ascending=False).head(10)
plt.figure(figsize=(20, 10))
sns.histplot(x="Name", hue="NetWorth", data=df)
plt.show()