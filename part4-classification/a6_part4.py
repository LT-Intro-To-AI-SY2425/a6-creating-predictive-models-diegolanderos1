import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("part4-classification/suv_data.csv")
print(data)
data['Gender'].replace(['Male','Female'],[0,1],inplace=True)
print(data)
x = data[["Age", "EstimatedSalary", "Gender"]].values
y = data["Purchased"].values

# Step 1: Print the values for x and y
print(x)
print(y)
# Step 2: Standardize the data using StandardScaler, 
scaler = StandardScaler().fit(x)
# Step 3: Transform the data
x = scaler.transform(x)
# Step 4: Split the data into training and testing data
xTraining, xTest, yTraining, yTest = train_test_split(x,y)
# Step 5: Fit the data
# Step 6: Create a LogsiticRegression object and fit the data
model = linear_model.LogisticRegression().fit(xTraining,yTraining)
# Step 7: Print the score to see the accuracy of the model
print("Model Accuracy Score:", model.score(xTest,yTest))
# Step 8: Print out the actual ytest values and predicted y values
print("\nTesting Results:\n")
correct_cases = 0
for index in range(len(xTest)):
    x = xTest[index]
    x = x.reshape(-1,3)
    print("Personal Information:", x)
    yPred = int(model.predict(x))        

    if yPred == 1:
        pred = True
    else:
        pred = False
    if pred:
        print("Prediction: Purchased")
    else:
        print("Prediction: Not Purchased")

    if yTest[index] == 1:
        acc = True
    else:
        acc = False
    if acc:
        print("Actual: Purchased")
    else:
        print("Actual: Not Purchased")
    
    if pred == acc:
        print("The Model is Correct")
        correct_cases += 1
    else:
        print("The Model is not Correct")
    print(f"Predicted: {pred} Actual: {acc}")
    print("-------------------------------------------------------------")
pcorrect = 100*(correct_cases / len(yTest))
print("Percentage of Cases Correct:", pcorrect,"%")

#special point
c = [["34", "56000", "1"]]
c = scaler.transform(c)
spred = model.predict(c)
if spred == 1:
    print("Special Prediction: Purchased")
else: 
    print("Special Prediction: Not Purchased")
# based on the xtest data
