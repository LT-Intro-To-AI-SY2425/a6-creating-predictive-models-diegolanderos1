# Part 2 - Training and Testing Data Writeup

After completing `a6_part2.py` answer the following questions

## Questions to answer

1. What makes this model more effective than the model you created in the previous lesson?
    This model is more effective than the previous model because it is trained on non-outlier data. This creates a linear regression that is more accurate.

2. What does the R squared coefficient tell you about the model?
    The R squared coefficient informs on the strength of correlation between the dependent and independent variables. In this case, the R squared value is 0.533, demonstrating that this model does not show an incredibly strong correlation between the variables.


3. Would you say that your model is accurate? What evidence supports your conclusion? Consider the meaning of the predicted and actual values in the context of the chart below from the American Heart Association’s website on understanding blood pressure.
    I would not say that this model is accurate. There with the predicted vs. actual y values, there is too much variation for the application of this model in the real world. For instance, the predicted y value for the x-value of 34.0 is 130.79 while the actual y value was 110. According to the American Heart Association, a systolic blood pressure of 130 is indicative of hypertension/high blood pressure, while a measure of 110 is healthy/normal. This demonstrates that there is too high variability and error for the real-world application of this model.