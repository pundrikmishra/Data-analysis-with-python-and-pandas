import pandas as pd


df = pd.read_csv('ZILLOW-Z77006_ZTTY.csv')
print(df.head())
print('-'*114)

df.set_index('Date', inplace=True)
df.to_csv('pm.csv')
# print('-'*114)

df1= pd.read_csv('pm.csv')
print(df1.head())
print('-'*114)

df1= pd.read_csv('pm.csv', index_col=0)
print(df1.head())
print('-'*114)


df1.columns= ['pm']################## column name chenges from value to pm
print(df1.head())

df1.to_csv('pm2.csv') #
df1.to_csv('pm3.csv', header= False)################### just data, no header


print('-'*114)
print('-'*114)

df2 = pd.read_csv('pm3.csv', names=['Date','Value'], index_col=0)## set column name
print(df2.head())
df2.to_csv('pm4.csv')

################ convert to html from csv
df2.to_html('pm5.html')

#############################
df = pd.read_csv('pm3.csv', names= ['Date','am'])
print(df.head())
df.rename(columns={'am':'km'}, inplace=True)
print(df.head())