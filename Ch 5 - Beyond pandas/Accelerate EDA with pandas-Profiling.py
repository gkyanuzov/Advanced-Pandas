import pandas as pd
from pandas_profiling import ProfileReport

iris = pd.read_csv('D:\\Docs\\Uni\\Online Courses\\Advanced Pandas - LinkedInLearning\\Ex_Files_Adv_Pandas\\Exercise '
                   'Files\\iris.csv')

profile = ProfileReport(iris, title= 'Iris Data Profile')
# in jupyter notebook
profile.to_notebook_iframe()