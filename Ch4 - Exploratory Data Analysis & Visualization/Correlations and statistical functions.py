import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('D:\\Docs\\Uni\\Online Courses\\Advanced Pandas - LinkedInLearning\\Ex_Files_Adv_Pandas\\Exercise '
                   'Files\\iris.csv')

# measures of central tendency
print(iris.mean)
print(iris.median)
print(iris.mode)

# variance measures
print(iris.std(numeric_only=True))
print(iris.boxplot())

# quick insights with describe
print(iris.describe())
print('\n')

# show correlation between each of the variables;
# positive means if one increases, then the other increases as well;
# the closer to 1 or -1, the stronger the relationship;
print(iris.corr(numeric_only=True))
print('\n')

iris.corr(numeric_only=True).style.background_gradient(cmap='RdY1Gn', axis=None)


plt.show()
