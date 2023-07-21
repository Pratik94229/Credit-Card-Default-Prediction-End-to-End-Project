
# Credit Card Default Prediction End-to-End Project

This is an end-to-end project that focuses on predicting credit card default using machine learning techniques. The project includes data validation,data preprocessing, model training, evaluation, and deployment.

## Project Overview

The goal of this project is to build a predictive model that can accurately classify whether a credit card holder is likely to default on their payment. This can help financial institutions and credit card companies identify potential defaulters and take appropriate actions to mitigate risk.

## Folder Structure
```
└───creditCardDefaulters
    ├───application_logging
    ├───best_model_finder
    ├───data
    ├───DataTransformation_Prediction
    ├───DataTransform_Training
    ├───DataTypeValidation_Insertion_Prediction
    ├───DataTypeValidation_Insertion_Training
    ├───data_ingestion
    ├───data_preprocessing
    ├───dist
    ├───documentation
    ├───EDA
    ├───file_operations
    ├───models
    │   ├───KMeans
    │   ├───NaiveBayes1
    │   ├───NaiveBayes2
    │   └───XGBoost0
    ├───PredictionArchivedBadData
    │   ├───BadData_2023-06-19_165637
    ├───Prediction_Batch_files
    ├───Prediction_Database
    ├───Prediction_FileFromDB
    ├───Prediction_Logs
    ├───Prediction_Output_File
    ├───Prediction_Raw_Data_Validation
    ├───Prediction_Raw_Files_Validated
    ├───preprocessing_data
    ├───templates
    ├───TrainingArchiveBadData
    │   ├───BadData_2023-06-19_162402
    ├───Training_Batch_Files
    ├───Training_Database
    ├───Training_FileFromDB
    ├───Training_Logs
    ├───Training_Raw_data_validation
    ├───Training_Raw_files_validated
```

## Dataset Information

This dataset contains information on default payments, demographic factors, credit data, history of payment, and bill statements of credit card clients in Taiwan from April 2005 to September 2005.
Content

There are 25 variables:

- ID: ID of each client
- LIMIT_BAL: Amount of given credit in NT dollars (includes individual and family/supplementary credit
- SEX: Gender (1=male, 2=female)
- EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)
- MARRIAGE: Marital status (1=married, 2=single, 3=others)
- AGE: Age in years
-  PAY_0: Repayment status in September, 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months, 9=payment delay for nine months and above)
- PAY_2: Repayment status in August, 2005 (scale same as above)
-    PAY_3: Repayment status in July, 2005 (scale same as above)
-    PAY_4: Repayment status in June, 2005 (scale same as above)
-    PAY_5: Repayment status in May, 2005 (scale same as above)
-    PAY_6: Repayment status in April, 2005 (scale same as above)
-    BILL_AMT1: Amount of bill statement in September, 2005 (NT dollar)
-    BILL_AMT2: Amount of bill statement in August, 2005 (NT dollar)
-    BILL_AMT3: Amount of bill statement in July, 2005 (NT dollar)
-    BILL_AMT4: Amount of bill statement in June, 2005 (NT dollar)
-    BILL_AMT5: Amount of bill statement in May, 2005 (NT dollar)
-    BILL_AMT6: Amount of bill statement in April, 2005 (NT dollar)
-    PAY_AMT1: Amount of previous payment in September, 2005 (NT dollar)
-    PAY_AMT2: Amount of previous payment in August, 2005 (NT dollar)
-    PAY_AMT3: Amount of previous payment in July, 2005 (NT dollar)
-    PAY_AMT4: Amount of previous payment in June, 2005 (NT dollar)
-    PAY_AMT5: Amount of previous payment in May, 2005 (NT dollar)
-    PAY_AMT6: Amount of previous payment in April, 2005 (NT dollar)
-    default.payment.next.month: Default payment (1=yes, 0=no)


## Dependencies

The project's dependencies are listed in the `requirements.txt` file. You can install them using the following command:

```
1. conda create -p venv python==3.8
2. conda activate venv/ 
3. pip install -r requirements.txt

```
To run the project locally, please ensure you have the following dependencies installed:

- Python 3.7 or higher
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Jupyter Notebook 
- ipykernel
- streamlit

Once you have the dependencies, follow these steps to set up the project:

## Getting Started

To get started with this project, you can follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/Pratik94229/Credit-Card-Default-Prediction---End-to-End-Project.git
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Explore the collab notebooks in the `EDA/` directory to understand the data and the steps involved in preprocessing and training the regression model.

4. Run the script to preprocess,tranform the dataset along with training the model:

```
   python main.py
  ```


5. Tune the model by changing parameters in tuner.py:

 

Feel free to modify the code and experiment with different models and techniques to improve the prediction accuracy.



## Acknowledgments

- The dataset used in this project is obtained from https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset.






