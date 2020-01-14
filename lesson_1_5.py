# -*- coding: UTF-8 -*-

import pandas as pd

d = {'姓名': ['张飞', '关羽', '赵云', '黄忠', '典韦', '典韦'], '语文': [66, 95, 95, 90, 80, 80], '英语': [65, 85, 92, 88, 90, 90],
     '数学': [None, 98, 96, 77, 90, 90]}
df = pd.DataFrame(data=d)
df.drop_duplicates('姓名', 'first', True)
df.fillna(0, inplace=True)
s = df.sum(axis=1)
df2 = s.to_frame(name='总分')
df3 = pd.merge(df, df2, left_index=True, right_index=True)
print(df3)
