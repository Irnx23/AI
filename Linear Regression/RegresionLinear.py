import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df =pd.read_csv("Salary_Data.csv")
plt.figure(figsize=(12,6))
sns.pairplot(df, x_vars=['YearsExperience'], y_vars=['Salary'], size=7, kind='scatter')
plt.show()

X=df['YearsExperience']
y=df['Salary']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.7, random_state=100)
X_train = X_train[:,np.newaxis]
X_test = X_test[:,np.newaxis]

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
c = [i for i in range (1,len(y_test)+1,1)]
plt.plot(c,y_test,color='r',linestyle='-') #Valores realres
plt.plot(c,y_pred,color='b',linestyle='-') #Valores prediccion
plt.xlabel('Index')
plt.ylabel('Salary')
plt.title('Prediction')
plt.show()
