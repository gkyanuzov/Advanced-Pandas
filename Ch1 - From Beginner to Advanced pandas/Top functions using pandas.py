import pandas as pd

iris = pd.read_csv('D:\\Docs\\Uni\\Online Courses\\Advanced Pandas - LinkedInLearning\\Ex_Files_Adv_Pandas\\Exercise Files\\iris.csv')

print(iris.shape)
print(iris.head(3))
print(iris.tail()) #prints bottom rows

print(iris.dtypes)

#subsetting with loc & iloc

print(iris.loc[3:5])

print(iris.iloc[3,0])
#same as
print(iris.loc[3, 'sepal_length'])

#export data as csv
iris.to_csv('iris-output1.csv', index= False)