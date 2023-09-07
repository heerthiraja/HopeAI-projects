# Understanding and Explaining the Results of a Linear Regression Model

The report provides an explanation of the linear regression model that was built using statistical techniques. The purpose of this report is to help understand the underlying patterns and relationships between the dependent and independent variables in the model. The report provides a detailed analysis of the model's performance, including its goodness of fit, accuracy, and interpretability, using various statistical measures and tests. The report is intended for individuals with some prior knowledge of linear regression and statistical analysis, but also provides explanations and examples to help clarify key concepts for those who are new to these topics.

### Introduction

This report is about the linear regression model that was built to predict the sales of a product based on the investment in TV advertising. The model was built using the OLS (Ordinary Least Squares) method, which is a commonly used method for fitting linear regression models.

The summary of the linear regression model is provided below. The data used in the model consisted of 200 observations. The dependent variable in the model is "Sales", and the independent variable is "TV".

### Model Summary

The R-squared value of the model is 0.812, which indicates that 81.2% of the variation in the sales can be explained by the investment in TV advertising. The adjusted R-squared value of the model is 0.811, which is slightly lower than the R-squared value, but still indicates a strong fit.

The F-statistic of the model is 856.2, with a corresponding p-value of 7.93e-74. This p-value is extremely small, which indicates that the model is highly significant.

The model has 198 degrees of freedom for residuals and 1 degree of freedom for the model. The covariance type used in the model is "nonrobust".

The coefficients of the model are:

const: 6.9748
TV: 0.0555
The standard errors of the coefficients are:

const: 0.323
TV: 0.002
The Omnibus test statistic is 0.013, with a p-value of 0.993. This suggests that the residuals are normally distributed. The Durbin-Watson statistic is 2.029, which indicates that the residuals are independent.

The Jarque-Bera statistic is 0.043, with a p-value of 0.979. This suggests that the residuals are normally distributed.

The skewness of the residuals is -0.018, which indicates that the residuals are close to being normally distributed. The kurtosis of the residuals is 2.938.

The condition number of the model is 338, which suggests that the model is not sensitive to small changes in the data.

### Assumptions of Linear Regression

Linear regression is a popular and powerful tool for modeling relationships between variables, but it makes several key assumptions that must be satisfied in order for the model to be reliable. In this section, we will examine the assumptions of linear regression and how they can be tested using the summary of the OLS Regression Results.

1. Linearity: Linear regression assumes that the relationship between the independent and dependent variables is linear. In other words, the change in the dependent variable is proportional to the change in the independent variable.

Following graph depicts the relationship between the independent and dependent variables in the model. The graph shows that the relationship between the variables is linear.

![Linearity](./images/Figure_1.png)

2. Homoscedasticity: Linear regression assumes that the variance of the errors (residuals) is constant across all levels of the independent variable. In other words, the spread of the residuals should be similar for all levels of the independent variable.

Following picture shows the residuals of the model. The residuals are plotted against the fitted values of the model. The graph shows that the residuals are randomly scattered around the horizontal axis, which indicates that the observations are independent of each other.

![Independence](./images/Figure_2.png)

3. Normality: Linear regression assumes that the errors (residuals) are normally distributed.

Following picture shows the histogram of the residuals. The graph shows that the residuals are normally distributed.

![Normality](./images/Figure_3.png)

The OLS Regression Results provide some useful information for testing these assumptions.

- The Durbin-Watson statistic of 2.029 suggests that the residuals are independent, which supports the independence assumption.
- The Jarque-Bera statistic of 0.043, with a high Prob(JB) of 0.979, suggests that the residuals are close to being normally distributed, which supports the normality assumption.
- The skewness of -0.018 further supports this conclusion.
- The Omnibus statistic of 0.013, with a high Prob(Omnibus) of 0.993, suggests that the residuals are close to being normally distributed.

### Interpretation of the Model Equation

The equation of the linear regression model is given by:

`Sales = 6.9748 + 0.0555 * TV`

where,

- Sales is the dependent variable
- TV is the independent variable
- 6.9748 is the constant term or the y-intercept
- 0.0555 is the coefficient of TV, which represents the change in the dependent variable (Sales) for a unit change in the independent variable (TV) while all other variables are kept constant.

The interpretation of the coefficients is as follows:

- The constant term (6.9748) represents the expected value of Sales when TV = 0. This means that even when no money is spent on TV advertising, the expected value of Sales is 6.9748 units.

- The coefficient of TV (0.0555) represents the change in Sales for a unit increase in TV advertising spending. It means that for every additional unit of TV advertising spending, the Sales is expected to increase by 0.0555 units.

The coefficients in the linear regression equation capture the relationship between the independent variable TV and the dependent variable Sales. The constant term captures the baseline value of Sales when TV = 0, while the coefficient of TV captures the effect of TV advertising spending on Sales.

### Model's Performance

The Model Performance section provides an assessment of how well the linear regression model fits the data. The model performance is measured using the R-squared value, which is a statistical measure of how close the data are to the fitted regression line.

In the ols summary, the R-squared value is reported as 0.812, which indicates that 81.2% of the variance in the dependent variable (Sales) is explained by the independent variable (TV). This indicates that the model is able to capture a large portion of the variation in the Sales data. The adjusted R-squared value, which takes into account the number of variables in the model, is also reported as 0.811, which is close to the R-squared value.

Overall, the high R-squared value suggests that the linear regression model is a good fit for the data and provides a strong explanation for the relationship between TV advertising and Sales.

### Limitations and Further Improvements

The model developed in this analysis is meant for learning purposes and has room for improvement in various aspects. One of the limitations of this model is that it was trained and evaluated using the entire data, without splitting it into training and testing sets. This can lead to overfitting, where the model becomes too specific to the training data and does not generalize well to new data.

Another limitation of this model is that it does not have many features to explain the variation in the dependent variable. More features could be added to the model to capture more complex relationships between the independent and dependent variables.

Finally, it is important to note that this model was developed based on a limited data set and may not be representative of the underlying relationship between the independent and dependent variables in the population. Further analysis, including feature selection and regularization, may be required to increase the robustness of the model.
