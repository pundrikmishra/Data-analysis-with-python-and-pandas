import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')


fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
data = pd.DataFrame(
    {'Timestamp':[1313331280, 1313334917, 1313334917, 1313340309, 1313340309], 
     'Price': [10.4]*3 + [10.5]*2, 'Volume': [0.779, 0.101, 0.316, 0.150, 1.8]})
data = data.set_index(['Timestamp'])
#             Price  Volume
# Timestamp                
# 1313331280   10.4   0.779
# 1313334917   10.4   0.101
# 1313334917   10.4   0.316
# 1313340309   10.5   0.150
# 1313340309   10.5   1.800

data.index = pd.to_datetime(data.index, unit='s')
print(data)

##############################################################################
##############################################################################
# ticks = data[['Price', 'Volume']]
# bars = ticks.Price.resample('10min').sum()
# volumes = ticks.Volume.resample('10min').sum()
#####################################  OR    #################################
# bars = data.Price.resample('10min').sum()
# volumes = data['Volume'].resample('10min').sum()
data['resamplePrice'] = data['Price'].resample('10s').sum()
data['resampleVolume'] = data.Volume.resample('10s').sum()
##############################################################################
##############################################################################
print(data[['resamplePrice','Price']])
print(data[['resampleVolume','Volume']])

# data.dropna(how='all',inplace=True)
# data.fillna(method='ffill',inplace=True)
# data.fillna(method='bfill',inplace=True)
# data.fillna(method='backfill',inplace=True)
# data.fillna(value=-9999,inplace=True)
data.fillna(value=-9999,limit=2,inplace=True)

print(data[['resamplePrice','Price']])
print(data[['resampleVolume','Volume']])
print(data.isnull().values.sum())
# print(data.isnull())

# # data.plot(ax=ax1)

# data.Price.plot(ax=ax1, label='Price')
# data['Price'].plot(ax=ax1, label='Price')
##data['resamplePrice'].plot(ax=ax1, label='Price')

# data.Volume.plot(ax=ax1, label='Volume')
# data['Volume'].plot(ax=ax1, label='Volume')
##data['resampleVolume'].plot(ax=ax1, label='Price')



data[['resamplePrice','Price',]].plot(ax=ax1)
data[['resampleVolume','Volume']].plot(ax=ax1)

# data[['resamplePrice','Price','resampleVolume','Volume']].plot(ax=ax1)
# data['Volume'].plot(ax=ax1, label='Volume')


plt.legend(loc=4)
plt.show()
