import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r'C:\Machine Learning\Module-2\Custom_Weather_Forcast_Dataset_1.csv')
print(df)

# First 5 records
print('\n See First Five records')
print(df.head())

# Last 5 records
print('\n See Last five records')
print(df.tail())

# Description of the data set
print('\n Description of Dataset')
print(df.describe())

# Shape of the data set
print('\n Shape of Dataset')
print(df.shape)

# Data type of each indivual columns or attributes
print('\nData type of Each column')
print(df.dtypes)

# Change Attributes or columns Name

df.columns=['outlook','temperature','humidity','windy','play']
print(df)

# Series
t=df['temperature']
print(type(t))
print(t)

# Create new dataframe from df
df1=df[['temperature','humidity']]
print(df1)

# Again create new dataframe from df
df3=df.iloc[0:10,[0,2]]
print(df3)

# for all odd numbered index display outlook, temperature, windy
print(df.iloc[1:14:2,[0,1,3]])

# Alternate process of display outlook, tempareture, windy for all odd numbered index
df4=df.loc[1:len(df):2,['outlook','temperature','windy']]
print(df4)


print(df['temperature'])
# All Statistical measure over temperature column

# create series object from df dataframe
Temperature=df[['temperature']]
print(type(Temperature))
print(Temperature)

print('Mean: ',Temperature.mean())
print('Standard Deviation',Temperature.std())
print('Variance',Temperature.var())
print('Lower Queartile',Temperature.quantile(0.25))
print('Median',Temperature.quantile(0.5))
print('Median',Temperature.median())
print('Upper Quartile',Temperature.quantile(0.75))
print('Skewness',Temperature.skew())
print('kurtosis',Temperature.kurt())
print('Min',Temperature.min())
print('Max',Temperature.max())


df.hist(column=['temperature'], bins=5)
plt.show()
df.hist(column='humidity', bins=5)
plt.show()