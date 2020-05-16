import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')


# fig = plt.figure()
# ax1 = plt.subplot2grid((1,1), (0,0))

# data = pd.read_pickle('example3.pickle')
# ######## data.index = pd.to_datetime(data.index, unit='N')
# # pm1year =data['pm'].resample('A')# Annual
# # pm1year =data['pm'].resample('D')# Daily
# # pm1year =data['Value'].resample('H')# Hour
# # pm1year =data['pm'].resample('A', how='mean')
# # pm1year =data['pm'].resample('A', how='ohlc')#### open, high, low, close

# print(data.head())
# # print(pm1year.head())

# # data.plot(ax=ax1)
# data['pm'].plot(ax=ax1, label="Monthly pm")
# # pm1year.plot(ax=ax1, label = 'yearly pm')
# # plt.legend().remove()
# # plt.legend(loc= 4)
# plt.legend()


# plt.show()


################################################################################################
################################################################################################
################################################################################################
################################################################################################

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
bars = data.Price.resample('10min').sum() # OR
# bars = data['Price'].resample('10min').sum()
volumes = data.Volume.resample('10min').sum() # OR
# volumes = data['Volume'].resample('10min').sum()
##############################################################################
##############################################################################

# data.plot(ax=ax1)
# data.Price.plot(ax=ax1, label='Price')
data['Price'].plot(ax=ax1, label='Price')
# data.Volume.plot(ax=ax1, label='Volume')
# data['Volume'].plot(ax=ax1, label='Volume')
bars.plot(ax=ax1, label='Resample Price')
# volumes.plot(ax=ax1, label='Resample Volume')
plt.legend(loc=4)
plt.show()
