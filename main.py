#MapPlot.py
#Name:Jenna Kramer
#Date:4/9
#Assignment:Lab 10

import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

# df = pd.DataFrame({"Trial": []})
df = pd.read_csv('reaction_time_data.csv')
print(df.head())

plt.plot(df["Trial"], df["ReactionTime_ms"])
# plt.savefig("output.png")

Q1 = df['ReactionTime_ms'].quantile(0.25)
Q3 = df['ReactionTime_ms'].quantile(0.75)

IQR = Q3 - Q1 

lower_bound = Q1 - 1.5 * IQR 
upper_bound = Q3 + 1.5 * IQR 

outliers = df[(df['ReactionTime_ms'] < lower_bound) | (df['ReactionTime_ms'] > upper_bound)]
filtered_df = df[(df['ReactionTime_ms'] >= lower_bound) & (df['ReactionTime_ms'] <= upper_bound)]

print(f'IQR: {IQR}')
print(f'Outliers:\n{outliers}')

plt.scatter(df["Trial"], df["ReactionTime_ms"])
plt.title("Reaction Time Across Trials")
plt.xlabel("Trial")
plt.ylabel("Reaction Time (ms)")
plt.xticks(np.arange(2, 21, 2))
plt.savefig("output.png")
