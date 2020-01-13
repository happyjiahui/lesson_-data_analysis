# -*- coding: UTF-8 -*-

import numpy as np

transcript_dtype = np.dtype([('姓名', 'U30'), ('语文', 'i'), ('英语', 'i'), ('数学', 'i')])
transcript = np.array(
    [(u'张飞', 66, 65, 30), ('关羽', 95, 85, 98), ('赵云', 93, 92, 96), ('黄忠', 90, 88, 77), ('典韦', 80, 90, 90)],
    dtype=transcript_dtype)


def show(subject):
    print('{}|{}|{}|{}|{}|{}'.format(
        subject,
        np.average(transcript[:][subject]),
        np.amin(transcript[:][subject]),
        np.amax(transcript[:][subject]),
        np.var(transcript[:][subject]),
        np.std(transcript[:][subject])
    ))


rank = np.sort(transcript, kind='mergesort', order=('语文', '英语', '数学'))


print('科目|平均成绩|最差成绩|最好成绩|成绩方差|成绩标准差')
show('语文')
show('英语')
show('数学')
print(rank)
