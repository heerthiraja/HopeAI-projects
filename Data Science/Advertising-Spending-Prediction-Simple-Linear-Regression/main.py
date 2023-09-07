from src.assumptions_test import LinearRegressionAssumptions
from src.build_model import SimpleLinearRegression
from src.data_ingest import DataIngestion
from src.data_preprocess import DataProcessing

if __name__ == "__main__":
    # Initialize the DataIngestion class with the file path
    data_ingest = DataIngestion("./data/advertising.csv")

    # Load the data and get the features and target variables
    X, y, df = data_ingest.get_X_y()
    df.to_csv("./data/simple_df.csv", index=False)
    print(df)
    # Print the data to check if it was loaded correctly

    # Initialize the DataProcessing class with the data
    data_process = DataProcessing(df)
    # data_process.identify_outliers(df["TV"])
    outliers = data_process.identify_outliers_zscore(df["TV"])
    print(outliers)
    # # build the model
    lr_model = SimpleLinearRegression(X, y)
    model = lr_model.summary()

    # # assumptions test
    # assumptions_test = LinearRegressionAssumptions(model, X, y)
    # assumptions_test.run_all()
