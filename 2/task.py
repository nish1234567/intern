import pandas as pd
my_dict = { 'Time' : ['21/04/2022'],
                   'maximum price of the day' : [0],
                   'minimum price of the day': [0]}
df = pd.DataFrame(my_dict)
df
df.to_csv('create_csv', index=False)
data = pd.read_csv('create_csv.csv')
data
