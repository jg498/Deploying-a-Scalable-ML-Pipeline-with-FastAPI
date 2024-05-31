# Model Card

## Model Details
The model used here is a Random Forest created by Joel Garcia. It was created for the Udacity Deploying a Machine Learning Model with FastAPI project of the Machine Learning DevOps program. The details about the model can be found below.
The model.py file contains the following functions:
- train_model: Trains a machine learning model and returns it. It is training a RandomForestClassifier model
- compute_model_metrics: Validates the trained machine learning model using precision, recall, and F1
- inference: Run model inferences and return the predictions
- save_model: Serializes model to a file

## Intended Use
The intended use of the model is to predict whether income exceeds $50K/yr based of the census.csv file located in the data folder. Also known as Adult dataset. An investigation into the attributes, columns, datatypes, sample of data are provided in the data folder under the Data_investigation.ipynb file. 

## Training Data
80% was used.


## Evaluation Data
20% was used as noted in the train_model.py file under test_size.

## Metrics
The following Metric were produced after running train_model.py:
Precision: 0.7457 | Recall: 0.6327 | F1: 0.6846

## Ethical Considerations
The dataset is from 1994 and is also small, so it can be used for historical purposes but should not be indicative of the current population and the changes it has undergone in three decades. A deeper investigation into biases should be conducted.

## Caveats and Recommendations
The records was extracted using the following conditions: ((AAGE>16) && (AGI>100) && (AFNLWGT>1)&& (HRSWK>0)) in 1994. A deeper dive into the way it was cleaned should be investigated to account for proper data cleaning procedures. Extraction was done by Barry Becker from the 1994 Census database.

Link: https://archive.ics.uci.edu/dataset/20/census+income