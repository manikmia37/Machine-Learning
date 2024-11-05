import matplotlib.pyplot as plt
import pandas as pd

# Sample data
x=[1,2,3,4,5]
y=[2,4,1,3,7]

# Create Line Plot
""" plt.plot(x,y)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Simple Line Plot") """
#plt.show()

# Create Scatter Plot
""" plt.scatter(x,y)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Scatter Plot") """
#plt.show()

# Create a bar chart
""" categories=['A','B','C','D']
values=[15,28,12,20]
plt.bar(categories,values)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Bar Chart")
plt.show() """

# Create a histogram
""" Data=[1,2,2,3,3,3,4,4,5]
plt.hist(Data,bins=7)
plt.xlabel("Data")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show() """

# line plot in time series data

# Sample of time Series Data
dates=pd.date_range(start='2024-01-01', periods=10, freq='D')
#print(dates)
values=[10,12,15,13,16,18,17,20,22,21]

# Create a time series plot
""" plt.plot(dates,values)
plt.xlabel('Dates')
plt.ylabel('Values')
plt.title('Time Series Line Plot')
plt.xticks(rotation=45) # rotation x label for better readability
plt.tight_layout() # adjust layout for better spacing
plt.show() """

# Sinusoidal plots using matplotlib
import numpy as np
""""x=np.arange(0,10,0.1)
#print(x)
# calculate the value of sine and cosine
y_sin=np.sin(x)
y_cos=np.cos(x)
#print(y_sin)
#print(y_cos)

# plot sine and cosine curves
plt.plot(x, y_sin, label='sin(x)')
plt.plot(x, y_cos, label="cos(x)")

# Add labels and tittles
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Sine And Cosine Curve")
plt.legend()
plt.show()
 """


""" # prompt: grid wise sinusoidal plot like above sine and cosine curve using  matplotlib
# Sinusoidal plots using matplotlib in a grid
x = np.arange(0, 10, 0.1)
# Calculate the value of sine and cosine
y_sin = np.sin(x)
y_cos = np.cos(x)
# Create a figure and axes objects
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# Plot sine curve in the first subplot
axs[0].plot(x, y_sin, label='sin(x)')
axs[0].set_xlabel('X')
axs[0].set_ylabel('Y')
axs[0].set_title('Sine Curve')
axs[0].legend()
# Plot cosine curve in the second subplot
axs[1].plot(x, y_cos, label='cos(x)')
axs[1].set_xlabel('X')
axs[1].set_ylabel('Y')
axs[1].set_title('Cosine Curve')
axs[1].legend()

# Adjust the layout and display the plot
plt.tight_layout()
plt.show() """

# prompt: Generate four Sinusoidal curves gridwise

# Sinusoidal plots using matplotlib in a grid
x = np.arange(0, 10, 0.1)

# Calculate the value of sine and cosine
y_sin1 = np.sin(x)
y_cos1 = np.cos(x)
y_sin2 = np.sin(x + np.pi/2)  # Phase shift by pi/2
y_cos2 = np.cos(x + np.pi/2)

# Create a figure and axes objects
fig, axs = plt.subplots(2, 2, figsize=(8, 6))

# Plot sine curve in the first subplot
axs[0, 0].plot(x, y_sin1, label='sin(x)')
axs[0, 0].set_xlabel('X')
axs[0, 0].set_ylabel('Y')
axs[0, 0].set_title('Sine Curve 1')
axs[0, 0].legend()

# Plot cosine curve in the second subplot
axs[0, 1].plot(x, y_cos1, label='cos(x)')
axs[0, 1].set_xlabel('X')
axs[0, 1].set_ylabel('Y')
axs[0, 1].set_title('Cosine Curve 1')
axs[0, 1].legend()

# Plot sine curve with phase shift in the third subplot
axs[1, 0].plot(x, y_sin2, label='sin(x + pi/2)')
axs[1, 0].set_xlabel('X')
axs[1, 0].set_ylabel('Y')
axs[1, 0].set_title('Sine Curve 2')
axs[1, 0].legend()

# Plot cosine curve with phase shift in the fourth subplot
axs[1, 1].plot(x, y_cos2, label='cos(x + pi/2)')
axs[1, 1].set_xlabel('X')
axs[1, 1].set_ylabel('Y')
axs[1, 1].set_title('Cosine Curve 2')
axs[1, 1].legend()
# Adjust the layout and display the plot
plt.tight_layout()
plt.show()

