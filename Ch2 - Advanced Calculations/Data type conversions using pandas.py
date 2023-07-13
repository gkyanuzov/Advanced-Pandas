import pandas as pd

planets = pd.read_csv('D:\\Docs\\Uni\\Online Courses\\Advanced Pandas - LinkedInLearning\\Ex_Files_Adv_Pandas\\Exercise Files\\planets.csv')
print(planets.head())
print(planets.dtypes)
print(planets.mean)

#int // float returns float
print(planets['number'][0]/planets['mass'][0])

#int to float
print(planets['number'][0].astype(float))

#float to int
print(planets['mass'][0].astype(int))

#year to str
print(planets['year'][0].astype(str))

#year to datetime
planets['year_dt'] = pd.to_datetime(planets['year'], format='%Y')
print(planets['year_dt'])

