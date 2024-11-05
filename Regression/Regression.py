import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#import readymade dataset
dataset=pd.read_csv(r'C:\Machine Learning\MODULE\Module-3\Salary_dataset.csv');

""" print(dataset.columns)
#named the first column as "Index"
dataset.columns=['Index','YearsExperience','Salary']
print(dataset.columns) """

""" #Drop the first column if you dont need it
dataset=dataset[['YearsExperience', 'Salary']]
print(dataset.columns) """

dataset.columns=['Index','YearsExperience','Salary']
x=dataset[['YearsExperience']]
y=dataset[['Salary']]

#Spliting the dataset into Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=1/3, random_state=0)

#Fitting Simple Linear Regression to the Training set or Create Predictor Model
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)

y_prediction=regressor.predict(X_test)
print(y_prediction)
# Match prediction value with y_test
print(y_test)  
#match korle dekhbo je Y_prediction and y_test er moddhe difference ace---atake Error Margin bole [Absolute Value Nite Hobe]

""" #Drawing CureFitting with Taining Set
plt.scatter(X_train,y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title("Salary VS Experience (with Training Set)")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show() """

""" #Drawing CurveFitting with Testing Set
plt.scatter(X_test,y_test,color='red')
plt.plot(X_test, regressor.predict(X_test), color='blue')
plt.title('Salary VS Experience (with Test Set)')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()
 """
# akhon Data gulo valovave Training Holo kina amra Evaluation korbo nicher process e
# model Evaluatio For Testing Set
from sklearn import metrics
mae=metrics.mean_absolute_error(y_test,y_prediction)
mse=metrics.mean_squared_error(y_test,y_prediction)
r2=metrics.r2_score(y_test,y_prediction)
print('Mean Absolute Error: %.2f'% mae)
print('Mean Squared Error: %.2f'% mse)
print('R2 Score: %.2f'% r2)
#if the r2 score is getting above 60 percent then it indicates better fit
