## Building the machine learning model for predicting the house prices

Steps involved in preparing the model - 

[Jupyter notebook link](House_price_prediction.ipynb)

1. **Data cleaning and exploring**:
- Handling null values
- standardizing the values in each columns
- removing outliers


2. **Data Preprocessing**:
- one hot encoding for categorial columns followed by dimentionality reduction 
- splitting the dataset into train and validation datasets

3. **Modelling**:
- Several models were trained on the processed data and validated with the test dataset
- Hyperparameter tuning for different models and with different parameters 
- Grid search CV was used to find the best model with low r-square value  
- out of all the models, Linear Regression model was giving the best results

4. **Exporting the model**
- Exporting the best model as python pickle file.
- Exporting the data structure (column names of the dataset) as json file.
 
