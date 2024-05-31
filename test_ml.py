import pytest
# TODO: add necessary import
from ml.model import train_model 
from ml.data import process_data   
from ml.model import compute_model_metrics
from sklearn.ensemble import RandomForestClassifier
from train_model import X_train, y_train

# TODO: implement the first test. Change the function name and input as needed
def testing_model_algorithm():
    """
    # add description for the first test
    For this test, we will check if the model uses the RandomForestClassifier algorithm.
    #Note Change name as needed 
    """
    # Your code here
    RFC = RandomForestClassifier()
    model = RFC.fit(X_train, y_train)
    return model
    assert model == RFC, 'The model does not use the RandomForestClassifier algorithm'


# TODO: implement the second test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    # add description for the second test
    For this test, we will check if the compute_model_metrics function returns the expected value.
    """
    # Your code here
    y = [0, 1, 0, 1]
    preds = [0, 1, 0, 0]
    precision, recall, fbeta = compute_model_metrics(y, preds)
    assert precision == 1.0, 'The precision is not as expected'
    assert recall == 0.5, 'The recall is not as expected'
    assert fbeta == 0.6666666666666666, 'The fbeta is not as expected'


# TODO: implement the third test. Change the function name and input as needed
def test_process_data():
    """
    # add description for the third test
    For this test, we will check if the process_data function returns the expected size or data type.
    """
    import pandas as pd
    data = {'A': [1, 2, 3], 'B': ['a', 'b', 'c'], 'salary': [0, 1, 0]}
    df = pd.DataFrame(data)
    X, y, encoder, lb = process_data(df, categorical_features=['B'], label='salary', training=True)
    assert X.shape == (3,4 ), 'The shape of X is not as expected'
    assert y.dtype == 'int64', 'The data type of y is not as expected'
    assert encoder.__class__.__name__ == 'OneHotEncoder', 'The encoder is not as expected'
    assert lb.__class__.__name__ == 'LabelBinarizer', 'The lb is not as expected'
    
