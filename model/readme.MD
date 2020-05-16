## Building the machine learning model for predicting the house prices

Steps involved in preparing the model - 

[Jupyter notebook link](House_price_prediction.ipynb)

1. **[Data cleaning and exploring](https://render.githubusercontent.com/view/ipynb?commit=5e65f63db804d7f3f6d75e4e6005f473b73091a6&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6b617679616a656574626f72612f486f7573655f50726963655f50726564696374696f6e5f42656e67616c7572752f356536356636336462383034643766336636643735653465363030356634373362373330393161362f6d6f64656c2f486f7573655f70726963655f70726564696374696f6e2e6970796e62&nwo=kavyajeetbora%2FHouse_Price_Prediction_Bengaluru&path=model%2FHouse_price_prediction.ipynb&repository_id=264215777&repository_type=Repository#2.-Data-Cleaning-and-Exploring)**:
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
 
