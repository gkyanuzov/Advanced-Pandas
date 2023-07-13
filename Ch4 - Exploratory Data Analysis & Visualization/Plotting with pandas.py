import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

daterange = pd.period_range('1/1/1950', freq='1d', periods=50)
date_df = pd.DataFrame(data=daterange, columns=['day'])
date_df['value1'] = np.random.randint(45, 65, size=(len(date_df)))
date_df['value2'] = np.random.randint(23, 35, size=(len(date_df)))
print(date_df)

# basic plot
ax = date_df.plot()

date_df.plot.area(stacked=False)
date_df.plot.area(stacked=True)

# histograms
iris = pd.read_csv('D:\\Docs\\Uni\\Online Courses\\Advanced Pandas - LinkedInLearning\\Ex_Files_Adv_Pandas\\Exercise '
                   'Files\\iris.csv')
iris.hist()
iris[['sepal_width', 'sepal_length']].plot.hist(alpha=1)

# scatter plot
colors = {'versicolor': 'red', 'setosa': 'green', 'virginica': 'blue'}
iris['colors'] = iris['species'].map(colors)
iris.plot.scatter(x='sepal_width', y='sepal_length', color=iris['colors'])

# scatter matrix
from pandas.plotting import scatter_matrix

scatter_matrix(iris, figsize=(15, 9))

plt.show()
