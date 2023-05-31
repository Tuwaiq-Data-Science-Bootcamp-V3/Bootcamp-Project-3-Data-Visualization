import pandas as pd
import seaborn as sns 



############################
df = pd.read_csv(r'C:/Users/20his/Desktop/RiyadhVillasAqar.csv')
df2=df.copy()

#############################
df2.columns
df2.drop(['Unnamed: 0'],inplace=True,axis=1)
df2.info()
#############################
df2['lounges'].fillna(0,inplace=True)
df2['square price'].fillna(0,inplace=True)
df2['price'].fillna(0,inplace=True)
#############################
df2.at[6800,'lounges']=7
df2.at[8569,'lounges']=7
df2.at[8978,'lounges']=7
df2.at[2206,'apartments']=30
df2.at[6851,'apartments']=30
#############################
df2['lounges'].replace('7+',7,inplace=True)
df2['apartments'].replace('30+',30,inplace=True)
#############################
df2[['rooms', 'lounges', 'streetWidth', 'stairs',
       'propertyAge', 'driverRoom', 'tent', 'patio', 'kitchen', 'outdoorRoom',
       'garage', 'duplex', 'space', 'apartments', 'maidRoom', 'elevator',
       'furnihsed', 'pool', 'basement']] = df2[['rooms', 'lounges', 'streetWidth', 'stairs',
              'propertyAge', 'driverRoom', 'tent', 'patio', 'kitchen', 'outdoorRoom',
              'garage', 'duplex', 'space', 'apartments', 'maidRoom', 'elevator',
              'furnihsed', 'pool', 'basement']].apply(pd.to_numeric)
#############################
df2.info()
df2.describe()
df2.head()
df2.tail()
#############################

sns.scatterplot(data=df2, x="price", y="space", hue="price", size="price",sizes=(20, 100))
#############################


