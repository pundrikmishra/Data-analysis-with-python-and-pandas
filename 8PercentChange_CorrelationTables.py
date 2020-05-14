import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

df=pd.read_csv('pm.csv')
df1=pd.read_csv('pm2.csv')
df.set_index('Date', inplace=True)
df1.set_index('Date', inplace=True)
# df =df.pct_change()
# print(df)
# df1 =df1.pct_change()
# print(df1)
am =df.join(df1)
# print(am)


am.to_pickle('example3.pickle')
data = pd.read_pickle('example3.pickle')
# print(data)
# am.to_pickle('example4_pct_change.pickle')
# data = pd.read_pickle('example4_pct_change.pickle')
# print(data)
# #################################################################################################
# #################################################################################################
# # data['pm2'] = data['pm'] * 2
# # print(data)
# # print(data['pm2'])
# #################################################################################################
data = pd.read_pickle('example3.pickle')
# data = pd.read_pickle('example4_pct_change.pickle')

# data.plot()
# plt.legend().remove()
# plt.show()
################################################################################################
################################################################################################
################################################################################################
################################################################################################
df2=pd.read_csv('pm.csv')
df3=pd.read_csv('pm2.csv')
df2.set_index('Date', inplace=True)
df3.set_index('Date', inplace=True)
df2["Value"] = (df2["Value"]-df2["Value"][0]) / df2["Value"][0] * 100.0  ## PERCENT CHANGE FROM STARTING VALUE
df3["pm"] = (df3["pm"]-df3["pm"][0]) / df3["pm"][0] * 100.0 
am =df2.join(df3)
am.to_pickle('example5_pct_change.pickle')
data = pd.read_pickle('example5_pct_change.pickle')
# print(data)
# data.plot()
# plt.legend().remove()
# plt.show()
################################################################################################
################################################################################################
################################################################################################
################################################################################################
# def PM_Benchmark():
#     df4=pd.read_csv('pm2.csv')
#     df4.set_index('Date', inplace=True)
#     df4["pm"] = (df4["pm"]-df4["pm"][0]) / df4["pm"][0] * 100.0
#     return df4

# fig = plt.figure()
# ax1 = plt.subplot2grid((1,1), (0,0))

# data = pd.read_pickle('example3.pickle')
# benchmark = PM_Benchmark()

# data.plot(ax=ax1)
# benchmark.plot(ax= ax1 ,color='y',linewidth=10)

# plt.legend().remove()
# plt.show()
#############################################################################################################
#############################################################################################################
data = pd.read_pickle('example5_pct_change.pickle')
Data_Correlation =data.corr()
print(Data_Correlation)
print(Data_Correlation.describe())