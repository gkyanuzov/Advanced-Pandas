import pandas as pd

iris = pd.read_csv('D:\\Docs\\Uni\\Online Courses\\Advanced Pandas - LinkedInLearning\\Ex_Files_Adv_Pandas\\Exercise '
                   'Files\\iris.csv')

print(iris.head(5))

# Group by
print(iris.groupby(['species']).max())
print('---------------------------------------')

# multiple aggregation methods to diff variables
df = iris.groupby(['species']).agg({'sepal_length':['mean', 'min','max'],
                                    'sepal_width': 'count'})
print(df)

# flattening hierarchical index
df.columns = ['_'.join(col).strip() for col in df.columns.values]
df.reset_index()
print(df)
print('--------------------------------------')

# specifying grouping prior to any aggregation
groupings = iris.groupby(['species'])
print(groupings.get_group('setosa').head())
print(groupings.max())

print(groupings.apply(lambda x: x.max()))

# use filter, similar to having in sql
print(groupings.filter(lambda x: x['petal_length'].max() < 5))