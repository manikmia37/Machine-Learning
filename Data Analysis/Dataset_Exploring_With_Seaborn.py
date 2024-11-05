import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Generate X values from 0 to 10 with increment 0.1
x=np.arange(0,10,0.1)
#print(x)
# Calculate Sin Values
y_sin=np.sin(x)
#print(y_sin)
#Create a dateframe for seaborn
df=pd.DataFrame({'x':x, 'sin(x)': y_sin})
""" print(df)
print(df.shape) """


""" # Plot sine curve using seaborn
sns.lineplot(x='x', y='sin(x)', data=df)
plt.title('Sine curve using Seaborn')
#show the plot
#plt.show() """

#Sample Data for Sea Born Plots from Seaborn

data=sns.load_dataset('iris')
#print(data)

# Scatter Plot with Hue
""" sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=data)
plt.title("Scatter Plot with Hue") """
#plt.show()

# Histogram with Karnel density estimation (KDE)
""" sns.histplot(x='sepal_length', data=data, kde=True)
plt.title('Histogram with KDE')
plt.show() """

# For anomaly detection we use Box plot
# Box Plot
""" sns.boxplot(x='species', y='sepal_length', data=data)
plt.title('Box Plot')
plt.show()
 """
 
 # Violin Plot
""" sns.violinplot(x='species', y='sepal_length', data=data)
plt.title('Violin Plot')
plt.show()
  """
  
# Pair Plot
""" sns.pairplot(data, hue='species')
plt.title('Pair Plot')
plt.show()
 """
# Joint Plot
sns.jointplot(x='sepal_length',y='sepal_width', data=data, kind='kde')
plt.title('Joint Plot')
plt.tight_layout()
plt.show()