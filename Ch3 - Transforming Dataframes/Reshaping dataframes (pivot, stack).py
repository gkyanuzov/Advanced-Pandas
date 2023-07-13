import pandas as pd

df = pd.DataFrame({"Region":['North','West','East','South','North','West','East','South'],
          "Team":['One','One','One','One','Two','Two','Two','Two'],
          "Revenue":[7500,5500,2750,6400,2300,3750,1900,575],
            "Cost":[5200,5100,4400,5300,1250,1300,2100,50]})
print(df)

print(df.pivot(index='Region', columns='Team', values='Revenue'))

# Stack
df2 = df.set_index(['Region', 'Team'])
stacked = pd.DataFrame(df2.stack())
print(stacked)

# Unstack
print(stacked.unstack())
print(stacked.unstack('Region'))

# Melt
print(df.melt(id_vars= ['Region', 'Team'], var_name = 'value type'))

# Support aggregation with pivot_table
# by default uses mean()
print(df.pivot_table(index='Team', values='Revenue'))
print(df.pivot_table(index='Team', columns='Region',values='Revenue'))
