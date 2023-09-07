import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class DataProcessing:
    def __init__(self, df):
        self.df = df

    def identify_outliers(self, data: pd.DataFrame):
        """
        Function to identify outliers in the data using a box plot visualization.

        Parameters:
        data (pd.Series): The data to be visualized.

        Returns:
        None
        """
        fig, ax = plt.subplots()
        ax.boxplot(data)
        ax.set_title("Box Plot of Data")
        ax.set_ylabel("Value")
        plt.show()

    def identify_outliers_zscore(self, data: pd.Series, threshold: float = 3):
        """
        Function to identify outliers in the data using the Z-Score method.

        Parameters:
        data (pd.Series): The data to be analyzed.
        threshold (float): The Z-Score threshold used to identify outliers.
                        Outliers are data points with a Z-Score greater than this threshold.
                        Default value is 3.

        Returns:
        outliers (pd.Series): A series of outliers in the data.
        """
        mean = np.mean(data)
        std = np.std(data)
        z_scores = (data - mean) / std
        outliers = data[np.abs(z_scores) > threshold]
        return outliers
