import pandas as pd
import statsmodels.api as sm


class SimpleLinearRegression:
    def __init__(self, x, y):
        """
        Initialize the class with the independent and dependent variables.

        Parameters:
        x (pd.Series): The independent variable.
        y (pd.Series): The dependent variable.
        """
        self.x = x
        self.y = y
        self.x = sm.add_constant(self.x)

    def fit(self):
        """
        Fit the linear regression model using the independent and dependent variables.

        Returns:
        model (sm.OLS): The fitted linear regression model.
        """
        model = sm.OLS(self.y, self.x).fit()
        return model

    def summary(self):
        """
        Print the summary of the linear regression model.

        Returns:
        None
        """
        model = self.fit()
        print(model.summary())
        return model
