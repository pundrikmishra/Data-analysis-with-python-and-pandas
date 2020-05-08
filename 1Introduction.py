import pandas as pd
import datetime
import pandas_datareader as web

from matplotlib import pyplot as plt
# from matplotlib import style


start = datetime.datetime(2010, 1, 1)
end = datetime.datetime.now()

df = web.DataReader("BSE", "yahoo", start, end)
print(df)
print(df.head())
df['Adj Close'].plot()
plt.show()