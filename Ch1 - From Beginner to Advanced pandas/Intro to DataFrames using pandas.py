import pandas as pd

scores = {"name":['Ray','Japhy','Zosa'],
          "city":['San Francisco','San Francisco','Denver'],
          "score":[75,92,94]
         }


df = pd.DataFrame(scores)
print(df)

print(df['score'])
print(df.score)

#create new col
df['name_city'] = df['name'] + '__' + df['city']
print(df)

over_90 = df[df['score'] > 90]
print(over_90)