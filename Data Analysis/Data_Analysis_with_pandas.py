import pandas as pd

# creating a series from a list 

data=[10,20,30,40,50]
series=pd.Series(data)
print(series)
# Access first element of Series
print(series[0])


# creating series with custom index

index=['a','b','c','d','e']
series_with_index=pd.Series(data, index)
print(series_with_index)

# performing some operation in series
print(series*2)  # multiply each element of series
print(series+5)  # adding 5 with each element of series

# Filtering Series
print(series[series>30])    # Series elements greater than 30

# Statiscal operation on series
print(series.mean())  # calculating the mean of series
print(series.std())  # calculating the standard deviation of series

# other useful methods and attributes
print(series.index)  # accessing the index labels
print(series.values) # accessing the values as a numpy array
print(series.describe()) # Generating descriptive statistics of the series


# sample data

DataSet={
    'Name': ['Alice','Bob','Charlie','David','Tom Lathan'],
    'Age': [25,30,28,35,45],
    'City': ['New York','Los Angles','Chicago','San Francisco','New York']
    
}

# create a Pandas DataFrame
df=pd.DataFrame(DataSet)
print(df)

# Basic Statistics
print("\nSummary Statistic: ")
print(df.describe())

# Accessing Specific Columns
print("\nName: ")
print(df['Name'])

# Filtering Data
print(df[df['Age']>25])

# Groping Data
print('\n Average Age By City')
print(df.groupby('City')['Age'].mean())

# Sorting Data
print('\nSorting Data By Name')
print(df.sort_values('City'))