import pandas as pd

emissions = pd.DataFrame({"country":['China','United States','India'],
          "year":['2018','2018','2018'],
          "co2_emissions":[10060000000.0,5410000000.0,2650000000.0]})

print(emissions)

#shows max 2 rows
pd.set_option('max_rows', 2)
print(emissions)

#shows max 2 rows
pd.set_option('max_columns', 2)
print(emissions)

#modify float format
pd.options.display.float_format = '{:,.2f}'.format()
print(emissions)