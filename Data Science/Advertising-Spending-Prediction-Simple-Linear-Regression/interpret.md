## Accessing the results of Linear Regression Model

Explanation:-

- Dep. Variable: This is the dependent variable of the model, in this case, Sales.
- R-squared:

  - The value of R-squared is a measure of how well the regression line fits the data. It ranges from 0 to 1, where 0 means that the model explains none of the variability of the response data around its mean, and 1 means that the model explains all the variability of the response data around its mean. A good R-squared value is typically greater than 0.5, but it depends on the specific context of the problem. A higher R-squared value indicates that the model is a better fit for the data, while a lower R-squared value means that the model is not as good of a fit for the data.

  - This is the coefficient of determination, which measures the proportion of variance in the dependent variable that is explained by the independent variable(s). In this case, the R-squared value is 0.812, which means that 81.2% of the variation in Sales can be explained by the independent variable in the model.

- Adj. R-squared:

  - Adjusted R-squared is a modified version of R-squared that adjusts for the number of predictors in the model. It is a measure of the goodness of fit of a linear regression model that adjusts for the number of predictors in the model. The adjusted R-squared increases only if the new term improves the model more than would be expected by chance.

  - For example, consider a simple linear regression model that predicts the sales of a product based on the amount spent on advertising (TV). The R-squared value of this model would give us an idea of how well the model fits the data. Let's say that the R-squared value of this model is 0.8. This means that 80% of the variability in the sales data is explained by the advertising spending.

  - Now, let's consider another model that includes an additional predictor, such as radio spending. The R-squared value of this model will increase if the radio spending improves the model. However, the increase in R-squared might not be significant if the number of predictors is large. In such cases, the adjusted R-squared gives a better estimate of the goodness of fit of the model, as it adjusts for the number of predictors. The adjusted R-squared will only increase if the new predictor significantly improves the model.

  - The adjusted R-squared provides a more accurate measure of the goodness of fit of a linear regression model, especially when the number of predictors is large.

  - In this case, the adjusted R-squared is 0.811, which is similar to the R-squared value.

- Method: This is the method used to fit the regression model, in this case, "Least Squares".

- F-statistic: This is the F-statistic, which tests the overall significance of the regression model. In this case, the F-statistic is 856.2 and the Prob (F-statistic) is 7.93e-74, which means that the model is highly significant.

  - The "7.93e-74" value in the summary represents the p-value of the F-statistic. The p-value is a measure of the strength of the evidence against the null hypothesis. In the case of linear regression, the null hypothesis is that the model coefficients are equal to zero. A low p-value (typically less than 0.05) indicates strong evidence against the null hypothesis and suggests that the model is significant.

  - There is no strict threshold for the p-value, but a commonly used threshold for statistical significance is 0.05, which means that there is only a 5% chance that the results are due to random chance. If the p-value is less than 0.05, we reject the null hypothesis and conclude that the model is significant. The p-value is much lower than 0.05, so we can conclude that the model is highly significant.

- No. Observations: This is the number of observations in the dataset. In this case, there are 200 observations.

- Df Residuals: This is the number of residual degrees of freedom, which is the number of observations minus the number of parameters estimated in the model. In this case, there are 198 residual degrees of freedom.

  - Degrees of freedom (df) is a statistical term that represents the number of independent values in a set of data. In the context of regression analysis, the degrees of freedom of the residuals is the number of residuals that are free to vary, given the constraints imposed by the model.

  - In a linear regression model with n observations, the residuals have n-k degrees of freedom, where k is the number of parameters (i.e., the number of independent variables) in the model. In this case, since there is only one independent variable (TV), the number of parameters is 1 and the degrees of freedom of the residuals is n-1, which is equal to the number of observations minus the number of parameters.

  - The Df Residuals is an important factor in determining the reliability of the statistical inferences made from the model. For example, the t-statistic and the F-statistic are calculated using the degrees of freedom of the residuals, and a larger number of degrees of freedom generally leads to more reliable statistical inferences.

- Covariance Type: This is the covariance type used to compute the standard errors of the coefficients. In this case, the covariance type is "nonrobust".

**Note about the Standard Errors:-**
Standard errors are a measure of the variability of the sampling distribution of a statistic. In other words, they represent the amount of uncertainty around the estimate of a population parameter based on a sample. For example, if we want to estimate the mean height of all adult males in the United States, we can take a sample of adult males and calculate the mean height of that sample. However, because the sample is only a small portion of the entire population, the mean height of the sample will not exactly match the mean height of the population. The standard error of the mean is a measure of the variability of the mean height of the sample, and provides an estimate of the uncertainty of the estimate of the population mean. The smaller the standard error, the more precise the estimate of the population mean.

    - Covariance type is typically nonrobust which means there is no elimination of data to calculate the covariance between features. Covariance shows how two variables move with respect to each other. If this value is greater than 0, both move in same direction and if this is less than 0, the variables mode in opposite direction. Covariance is difference from correlation. Covariance does not provide the strength of the relationship, only the direction of movement whereas, correlation value is normalized and ranges between -1 to +1 and correlation provides the strength of relationship.

- coef: This is the coefficient for each predictor in the model. In this case, there is only one predictor, TV, with a coefficient of 0.0555. The const coefficient represents the intercept of the model.

- std err: This is the standard error of each coefficient, which measures the uncertainty in the estimated coefficient values.

- t: This is the t-value of each coefficient, which is the coefficient divided by its standard error.

- P>|t|: This is the p-value of each coefficient, which measures the significance of each predictor in the model. In this case, both the const and TV coefficients have p-values close to 0, which indicates that both predictors are significant in the model.

- Omnibus: This is the Omnibus test, which tests the assumption of normality of the residuals. In this case, the Omnibus test statistic is 0.013 and the Prob(Omnibus) is 0.993, which suggests that the residuals are normally distributed.

  - The Omnibus test statistic is a statistical test used to assess the normality of the residuals in a linear regression model.
  - A good Omnibus test statistic would indicate that the residuals are normally distributed, which is an important assumption in linear regression analysis. The Prob(Omnibus) value is the p-value associated with the test statistic, and if this value is close to 1, it suggests that the residuals are likely normally distributed. A p-value less than a certain significance level (e.g. 0.05) would suggest that the residuals are not normally distributed, and the model may need to be revised.

- The Durbin-Watson statistic is used to test the independence of residuals in a linear regression model. It ranges between 0 and 4, with a value close to 2 indicating that residuals are uncorrelated and close to 0 indicating that there is positive serial correlation in the residuals, and a value close to 4 indicating that there is negative serial correlation in the residuals.

A value close to 2 suggests that the residuals are independent, and therefore, there is no autocorrelation in the residuals. This is important because in a linear regression model, the residuals should be independent and not show any pattern. Autocorrelation in residuals can lead to biased model estimates and incorrect inferences. So, a Durbin-Watson statistic close to 2 indicates that the residuals are uncorrelated and the linear regression model is a good fit for the data.

- Jarque-Bera (JB): This is the Jarque-Bera statistic, which tests the assumption of normality of the residuals. In this case, the Jarque-Bera statistic is 0.043 and the Prob(JB) is 0.979, which suggests that the residuals are normally distributed.

  - The Jarque-Bera test statistic is a goodness-of-fit test for checking if a sample has the skewness and kurtosis matching a normal distribution. The null hypothesis of the test is that the skewness and kurtosis of the sample match those of a normal distribution. If the p-value of the test is greater than a significance level (typically 0.05), it means that there is not enough evidence to reject the null hypothesis and we can say that the sample has skewness and kurtosis that match those of a normal distribution. This suggests that the residuals of the regression model are approximately normally distributed, which is a desirable property in a linear regression model as it assumes that the errors are normally distributed.

- Skew: This is the skew of the residuals, which measures the asymmetry of the residuals. In this case, the skew is -0.018, which indicates that the residuals are close to being normally distributed.

  - Skewness is a statistical measure of the asymmetry of a distribution about its mean. If the skewness value is close to zero, it indicates that the distribution is symmetrical and the residuals are close to being normally distributed. If the skewness value is positive, it means that the distribution is positively skewed (i.e., it has a long tail on the positive side), and if it is negative, it means that the distribution is negatively skewed (i.e., it has a long tail on the negative side).

- Kurtosis: This is the kurtosis of the residuals, which measures the peakedness of the residuals. In this case, the kurtosis is 2.938, which indicates that the residuals are close to being normally distributed.

  - Kurtosis is a statistical measure of the peakedness or flatness of a distribution compared to the normal distribution. A kurtosis value close to 0 indicates that the distribution is similar to the normal distribution, whereas a positive kurtosis value indicates a more peaked distribution and a negative kurtosis value indicates a flatter distribution. In the context of regression models, kurtosis can be used to assess the distribution of residuals, which should be close to normal for the model to be considered well-fitted. The value of kurtosis can be used in conjunction with other tests, such as the Jarque-Bera test, to assess the normality of the residuals and determine if the assumptions of the regression model are satisfied.

- Cond. No.: The condition number is a measure of the sensitivity of a function's output to small changes in its inputs. In the context of a linear regression model, it represents the sensitivity of the model's predictions to small changes in the values of the independent variables. A large condition number indicates that the model is highly sensitive to small changes in the independent variable values, which can result in unstable predictions. A small condition number indicates that the model is relatively insensitive to changes in the independent variable values, which suggests that the model's predictions are relatively stable. In this case, the condition number is 338, which suggests that the model is not sensitive to small changes in the data.

Overall, this summary provides information about the fit of the regression model, the significance of the predictors in the model, and the assumptions of the model. Based on the results, it appears that the regression model fits well and the predictors are significant in explaining the variation in Sales. The residuals also appear to be normally distributed, which supports the validity of the model.
s
