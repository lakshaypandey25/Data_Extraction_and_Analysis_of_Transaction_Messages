This repository contains Python scripts designed to parse transaction messages, classify companies, and predict monthly expenses based on transaction data. 
Key components include:
1. entity_extraction.py, which extracts details such as transaction type, bank name, account number, and company name from transaction messages
2. training_dataset.py, which reads companies_sorted.csv containing over 7 million companies and their categories
3. train_classify_company.py, which trains a machine learning model for company classification
4. company_classification.py, which tests the trained model
5. inference.py, which outputs extracted transaction details
6. data_analytics.py, which generates visualizations like line graphs and pie charts for transaction data
7. transaction_prediction.py, which employs linear regression to predict the next month's expenses based on current transaction data.

NOTE: Ensure that the correct path to companies_sorted.csv is specified in training_dataset.py. The CSV file can be downloaded from the link provided in the text file training_dataset_download.
