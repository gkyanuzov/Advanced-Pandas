import pandas as pd

df = pd.DataFrame({"Region":['North','West','East','South','North','West','East','South'],
          "Team":['One','One','One','One','Two','Two','Two','Two'],
          "Squad":['A','B','C','D','E','F','G','H'],
          "Revenue":[7500,5500,2750,6400,2300,3750,1900,575],
            "Cost":[5200,5100,4400,5300,1250,1300,2100,50]})

#create new column 'profit' using lambda
df['Profit'] = df.apply(lambda x: 'Profit' if x['Revenue']>x['Cost'] else 'Loss', axis=1)
print(df)

#create new column using map
team_map = {'One':'Red', 'Two':'Blue'}
df['team color'] = df['Team'].map(team_map)
print(df)

#use applymap to apply function to each element in the df
print(df.applymap(lambda x: len(str(x))))

#for loop
new_col = []


for i in range(0, len(df)):
    rev = df['Revenue'][i]/df[df['Region'] == df.loc[i, 'Region']]['Revenue'].sum()
    new_col.append(rev)

df['Revenue share of region'] = new_col
df.sort_values(by='Region')
print(df)