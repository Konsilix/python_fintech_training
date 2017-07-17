#!/usr/bin/env python

from pandas import DataFrame

l1 = [1,2,3,4]
l2 = [5,6,7,8]

df = DataFrame({'Stimulus Time': l1, 'Reaction Time': l2})

print(df)

df.to_excel('test.xlsx', sheet_name='sheet1', index=False)

exit(0)

