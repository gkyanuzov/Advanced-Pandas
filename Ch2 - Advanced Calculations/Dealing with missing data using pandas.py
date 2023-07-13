import pandas as pd

temps = pd.DataFrame({"sequence": [1, 2, 3, 4, 5],
                      "measurement_type": ['actual', 'actual', 'actual', None, 'estimated'],
                      "temperature_f": [67.24, 84.56, 91.61, None, 49.64]
                      })
print(temps)

# identify null values in a dataframe
print(temps.isna())

# handle missing data
print(temps['temperature_f'].cumsum())  # by default skips nulls
print(temps['temperature_f'].cumsum(skipna=False))

# when grouping by default excludes null values
print(temps.groupby(by=['measurement_type']).max())
print(temps.groupby(by=['measurement_type'], dropna=False).max())

# drop rows witn null using axis = 0, use carefully
temps = temps.dropna()
print(temps)
# drop cols witn null using axis = 1
temps.dropna(axis=1)
print(temps)

# Replace null values
temps = temps.fillna(0)
print(temps)

# carries values over from previous row
temps = temps.fillna(method='pad')
print(temps)

# interpolate
temps = pd.DataFrame({"sequence": [1, 2, 3, 4, 5],
                      "measurement_type": ['actual', 'actual', 'actual', None, 'estimated'],
                      "temperature_f": [67.24, 84.56, 91.61, None, 49.64]
                      })
print(temps.interpolate())