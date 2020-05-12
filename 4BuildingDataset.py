import quandl
import pandas as pd

# api_key = open('apikey.txt','r').read()
# df = quandl.get('ZILLOW/M1300_MPPRSF',authtoken=api_key)
# print(df.head())


# state_name = pd.read_html('https://en.wikipedia.org/wiki/States_and_union_territories_of_India')
# df= state_name[3]

# for i in state_name[3][0][1:]:
#     print(i)
fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
print(fiddy_states)
print(fiddy_states[0])
for abbv in fiddy_states[0][0][1:]:
    print(abbv)