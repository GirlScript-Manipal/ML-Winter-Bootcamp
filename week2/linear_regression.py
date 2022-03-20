#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split

#basic code
df=pd.read_csv("insurance.csv")
dum1=pd.get_dummies(df.sex)
dum2=pd.get_dummies(df.smoker)
dum3=pd.get_dummies(df.region)
merge=pd.concat([df,dum1,dum2,dum3],axis='columns')
final=merge.drop(['sex','smoker','region'], axis='columns')
X=final.drop('charges', axis='columns')
y=final.charges

#splitting train set and test set
x_train,x_test,y_train,y_test=train_test_split(X,y)

#training set
reg=linear_model.LinearRegression()
reg.fit(x_train,y_train)

#predicting the results
y_pred=reg.predict(x_test)

#plotting the results
plt.figure(figsize=(20,10))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.show( )
