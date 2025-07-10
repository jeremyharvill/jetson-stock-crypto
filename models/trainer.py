# trainer.py
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_model(features, target, model_type="regression"):
    # Prepare the data
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, shuffle=False
    )

    if model_type == "regression":
        from sklearn.ensemble import RandomForestRegressor
        model = RandomForestRegressor(n_estimators=100, random_state=42)
    elif model_type == "classification":
        from sklearn.ensemble import RandomForestClassifier
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        # Convert target to binary class
        y_train = (y_train.shift(-1) > y_train).astype(int)
        y_test = (y_test.shift(-1) > y_test).astype(int)

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    if model_type == "regression":
        mse = mean_squared_error(y_test, predictions)
        print(f"[trainer.py] Model MSE: {mse:.4f}")
    else:
        accuracy = (predictions == y_test).mean()
        print(f"[trainer.py] Classification Accuracy: {accuracy:.2%}")

    return model
