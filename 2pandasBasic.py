import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np


web_stats = {'Day':[1,2,3,4,5,6],
            'Visitors':[43,44,53,23,64,34],
            'Bounce_rate':[61,62,63,74,65,66]}

# print(web_stats)
df = pd.DataFrame(web_stats)
print(df)
print('-'*114)
print(df.head())
print('-'*114)
print(df.tail())
print('-'*114)
print(df.tail(2))
print('-'*114)



print(df.set_index('Day'))
print(df.head())
print('-'*114)


# df = df.set_index('Day')
# print(df.head())
# print('-'*114)

# df.set_index('Day', inplace=True)
# print(df.head())
# print('-'*114)


#individual column
print(df['Visitors'])
print(df.Visitors)
print('-'*114)

#multiple columnn
print(df[['Visitors','Bounce_rate']])
print('-'*114)

# To list
print(df.Visitors.tolist())
# print(df[['Visitors','Bounce_rate']].tolist())    ## ############# Wrong method for many column, import numpy and then
print(np.array(df[['Visitors','Bounce_rate']]))
print('-'*114)
df2 = pd.DataFrame(np.array(df[['Visitors','Bounce_rate']]))
print(df2)