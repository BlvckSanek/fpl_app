"""Predictive model for estimating player points in FPL.

This model trains and loads an XGBoost regression model to predict player
player points for the next gameweek.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import mean_absolute_error
import joblib

def train_model():
    """Train an XGBoost regression model using historical FPL data.

    The model predicts player points for the next gameweek based on
    features like form, fixture difficulty and player statistics.

    Returns:
        None
    """
    # Load historical FPL data
    data = pd.read_csv('data/fpl_data.csv')

    # Define features and target variable
    features = ["form", "fixture_difficulty", "opponent_strength", "minutes",
                "goals_scored", "assists", "clean_sheets", "goals_conceded",
                "xg", "xa", "bps", "influence"]
    target = "next_gameweek_points"

    X = data[features]
    y = data[target]

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                        random_state=42)
    
    # Train XGBoost regression model
    model = xgb.XGBRegressor(objective="reg:squarederror", n_estimators=100,
                             max_depth=5, learning_rate=0.1)
    model.fit(X_train, y_train)

    # Evaluate model
    predictions = model.predict(X_test)
    print("MAE:", mean_absolute_error(y_test, predictions))

    # Save model
    joblib.dump(model, "model/xgboost_model.pkl")
    