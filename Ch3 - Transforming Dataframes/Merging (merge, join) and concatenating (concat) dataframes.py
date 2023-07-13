import pandas as pd
df1 = pd.DataFrame({'letter': ['A', 'B', 'C', 'D'],
                    'number': [1, 2, 3, 4]})
df2 = pd.DataFrame({'letter': ['C', 'D', 'E', 'F'],
                    'number': [3, 4, 5, 6]})

print(df1)
print(df2)
# Left join
print(df1.merge(df2, how ='left', on= 'number'))

# Inner join
print(df1.merge(df2, how ='inner', left_on= 'number', right_on='number'))

# Right join
print(df1.merge(df2, how ='right', on= 'number', suffixes=('', '_right')))

# Union
df3 = pd.concat([df1, df2]).reset_index(drop=True)
print(df3)
df4 = pd.concat([df1, df2]).drop_duplicates().reset_index(drop=True)
print(df4)

# Concatenate dataframes horizontally

df5 = pd.concat([df1,df2],axis=1)
print(df5)

# Append new row to dataframe
new_row = pd.Series(['Z', 26], index= df3.columns)
# df3.append(new_row, ignore_index = True)
print(df3)

# Join along index
join_df = pd.DataFrame({'letter': ['F','G', 'H', 'I'],
                        'number': [6, 7, 8, 9]})

df6=df2.join(join_df, rsuffix='_right')
print(df6)