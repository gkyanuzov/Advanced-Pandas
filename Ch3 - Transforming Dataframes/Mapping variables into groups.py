import pandas as pd
import numpy as np

df = pd.DataFrame({"Species": ['Chinook', 'Chum', 'Coho', 'Steelhead', 'Bull Trout'],
                   "Population": ['Skokomish', 'Lower Skokomish', 'Skokomish', 'Skokomish', 'SF Skokomish'],
                   "Count": [1208, 2396, 3220, 6245, 8216]})
print(df)
print('\n')

# pd.cut
bins = [0, 2000, 4000, 6000, 8000, np.inf]
labels = ['Low Return', 'Below Avg Return', 'Avg Return', 'Above Avg Return', 'High Return']

df['Count Category'] = pd.cut(df['Count'], bins, labels=labels)
print(df)
print('\n')

# map species to endangered status
fed_status = {"Chinook": "Threatened",
              "Chum": "Not Warranted",
              "Coho": "Not Warranted",
              "Steelhead": "Threatened"}


df['Federal Status'] = df['Species'].map(fed_status)
print(df)
print('\n')

# categorical data type
df['Count Category'] = pd.Categorical(df['Count Category'],
                                      ordered=True,
                                      categories=labels)
print(df['Count Category'])
print('\n')

# sort by count category
print(df.sort_values(by=['Count Category'], ascending=False))
print('\n')


# get_dummies() - converts categorical variable into a dummy variable
print(pd.get_dummies(df['Count Category']))
