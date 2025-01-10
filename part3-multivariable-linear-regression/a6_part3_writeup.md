# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?
    The R squared coefficient for the model is 0.86. This shows that there is a very strong correlation between the dependent and independent variables, and this is a good model to represent this data.

2. Is your model accurate? Why or why not?
    This model is fairly accurate. Although some predictions are very close to the actual prices of cars, other predictions have variations of several thousand dollars, which could be significant for the purpose of this model. 

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?
    The predicted price for a car that is 
    10 years old with 89000 miles is about $10,656.21.
    20 years old with 150000 miles is about $3508.16.


4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?
    I believe this is happening because the model was not programmed with a limit to how low the price could go. Therefore, given high mileage and age, the model goes under what we know to be possible.