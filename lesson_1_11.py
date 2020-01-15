# -*- coding: UTF-8 -*-


import pandas as pd

data = {'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon', 'pastrami', 'honey ham',
                 'nova lox'],
        'ounces': [4.0, 3.0, None, 6.0, 7.5, 8.0, -3.0, 5.0, 6.0],
        'animal': ['pig', 'pig', 'pig', 'cow', 'cow', 'pig', 'cow', 'pig', 'salmon']}
df = pd.DataFrame(data)
df['food'] = df['food'].apply(str.lower)
df['animal'] = df['animal'].apply(str.lower)
df.drop_duplicates(['food', 'animal'], inplace=True)
print(df)
