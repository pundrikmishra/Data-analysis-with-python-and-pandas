import pickle
import pandas as pd
a = ['test value','test value 2','test value 3']
print(a)


pickle_out = open('example.pickle','wb') #wb = write bytes
pickle.dump(a,pickle_out)#this writes the object a to the  file named 'example.pickle'
pickle_out.close()


pickle_in = open('example.pickle','rb')  # we open the file for reading#### rb= read bytes
b = pickle.load(pickle_in)  # load the object from the file into var b
print(b)
if a==b:
    print('a and b are same')
else:
    print('a and b are not same')

#############################################################################################################
###############################  PANDAS HAVE IT'S OWN PICKLE METHOD  ########################################
#############################################################################################################
df=pd.read_csv('pm3.csv')
print(df)
df.to_pickle('example2.pickle')
c=pd.read_pickle('example2.pickle')
print('--'*130)
print(c)