# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
    When StandardScaler is removed, the model is less accurate than the model with StandardScaler. This is because the independent variables have different scales, so they must be standardized to avoid the data over-favoring variation in such a variable.
2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
    With the StandardScaler, this model is very accurate, with 86.0% of predictions being correct. This is good enough for this use case because this model would be utilized for its delineation of a strong correlation, not necessarilly specific data points that are significant for someone's health, like with the blood pressure model.

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
    The model was accurate, as shown in its 86.0% accuracy. However, the model was often incorrect with inputs where the salary was very negative (low) or very positive (high).

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.
    According to the model, a 34 year old female making 56,000 a year wouldn't buy an SUV.