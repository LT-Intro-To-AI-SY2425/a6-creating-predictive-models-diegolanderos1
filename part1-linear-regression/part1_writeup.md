# Part 1 - Linear Regression Writeup

After completing `a6_part1.py` answer the following questions

## Questions to answer

1. What is the r squared value?  What does this say about this linear regression model?
    The model's r squared value is 0.626. This shows that age has a strong correlation with blood pressure.

2. According to your model, what is the predicted systolic blood pressure for a person who is 42 years old?
    The linear regression model predicts that a person who is 42 years old would have a systolic blood pressure of 136.52.

3. How accurate do you think this model's predictions are?  Do you think this model is accurate enough to reliably predict someone's blood pressure based on their age?  Why or why not?  And if not, what could improve the model?
    I believe that this model's predictions are fairly accurate and do a good job demonstrating the correlation between age and blood pressure, but it suffers from a small data set, which results in several "outlier" data points. In order to fix this, training the model with a larger data set could be used.