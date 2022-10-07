import numpy as np
import pandas as pd

file='/content/Social_Network_Ads.csv'

df = pd.read_csv(file)
print(df)

print(df.shape)
print(df.head())
print(df.describe())

X = df.iloc[:,:-1].values
Y = df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size = 0.25 , random_state = 0)


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)
print(X_train)


from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)
print(y_pred)


from sklearn.metrics import accuracy_score
print("Accuracy of the model: ",accuracy_score(y_test,y_pred))



Age=int(input("Enter new Customer's Age: "))
sal = int(input("Enter new Customer's sal : "))
newCust=[[Age,sal]]
result = model.predict(sc.transform(newCust))
print(result)
if result == 1:
  print("Customer will buy the product: ")
else:
  print("Customer will not buy the product: ")

