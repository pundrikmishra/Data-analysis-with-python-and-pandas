import quandl
import pandas as pd

# api_key = open('apikey.txt','r').read()
# df = quandl.get('ZILLOW/M1300_MPPRSF',authtoken=api_key)
# print(df.head())


state_name = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population')
#
print(state_name[0])
# state_name.to_html('us_states.html')