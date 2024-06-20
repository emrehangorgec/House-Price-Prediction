# House Price Prediction

This project is an application for predicting house prices based on various input features such as square footage, number of bedrooms and bathrooms, neighborhood and year built. The application is built using Flask for the backend and a machine learning model for predictions.

## Overview

The House Price Prediction application allows users to input details about a house and receive an estimated price. The prediction model was trained on a dataset of house prices and includes preprocessing steps such as one-hot encoding for categorical variables.

## Dataset

The dataset used for training the model can be found on Kaggle: [Housing Price Prediction Data](https://www.kaggle.com/datasets/muhammadbinimran/housing-price-prediction-data).

### Dataset Overview

- **SquareFeet**: The total square feet of the house.
- **Bedrooms**: The number of bedrooms in the house.
- **Bathrooms**: The number of bathrooms in the house.
- **Neighborhood**: The neighborhood where the house is located.
- **YearBuilt**: The year the house was built.
- **Price**: The price of the house (target variable).

![image](https://github.com/emrehangorgec/House-Price-Prediction/assets/54534150/067c74a8-1ed7-49ce-afe8-5c1c96e0ed46)

## Usage

1. **Start the Flask application**:
    ```bash
    python main.py
    ```
2. **Open your web browser and navigate to** `http://127.0.0.1:5000` to access the application.
3. **Fill in the form** with the house details and click "Predict Price" to get the estimated price.

![image](https://github.com/emrehangorgec/House-Price-Prediction/assets/54534150/1c9d6415-31ef-4711-bd51-b7f2d75a336c)

## Contributing

If you have suggestions for improving this project, please feel free to submit a pull request or open an issue.
