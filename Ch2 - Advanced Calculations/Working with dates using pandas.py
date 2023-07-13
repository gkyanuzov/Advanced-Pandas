import pandas as pd

daterange = pd.period_range('1/1/2020', freq='30d', periods=4)

date_df = pd.DataFrame(data=daterange, columns=['sample_date'])
print(date_df)

#find date differnce
date_df['date difference'] = date_df['sample_date'].diff(periods=1)
print(date_df)

#find first day of the month
date_df['first of month'] = date_df['sample_date'].values.astype('datetime64[M]')
print(date_df)

#date types
print(date_df.dtypes)
date_df['sample_date'] = date_df['sample_date'].dt.to_timestamp()
print(date_df.dtypes)

#date subtraction
print(date_df['sample_date'] - date_df['first of month'])
#30 days ago
print(date_df['sample_date'] - pd.Timedelta('30 d'))

#see day name
print(date_df['sample_date'].dt.day_name())