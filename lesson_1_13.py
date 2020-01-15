# -*- coding: UTF-8 -*-


from sklearn import preprocessing

data = [5000, 16000, 58000]
data = preprocessing.minmax_scale(data)
value = data[1]
print(value)
