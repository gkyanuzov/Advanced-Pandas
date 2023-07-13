import pandas as pd

names = pd.Series(['Pomeray, CODY ',' Wagner; Jarry','smith, Ray'])

names = names.str.replace(';', ',')
print(names)

#returns length of row
print(names.str.len())

#strip
names = names.str.strip()
print(names.str.len())

#lower, upper
names = names.str.lower()
print(names)


#split and swap first and last name
names = names.str.split(', ')
print(names)
names = pd.Series([i[:: -1] for i in names])
print(names)
names = [' '.join(i) for i in names]
print(names)