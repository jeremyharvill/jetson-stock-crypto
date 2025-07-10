# evaluator.py
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

def evaluate_regression(model, X_test, y_test):
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print(f"[evaluator.py] Regression MSE: {mse:.4f}")
    print(f"[evaluator.py] R² Score: {r2:.4f}")
    return {"mse": mse, "r2": r2}

def evaluate_classification(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = (predictions == y_test).mean()

    print(f"[evaluator.py] Classification Accuracy: {accuracy:.2%}")
    return {"accuracy": accuracy}

def show_feature_importance(model, feature_names):
    if hasattr(model, "feature_importances_"):
        importance = model.feature_importances_
        importance_df = pd.DataFrame({
            "Feature": feature_names,
            "Importance": importance
        }).sort_values(by="Importance", ascending=False)

        print("[evaluator.py] Feature Importance:")
        print(importance_df.to_string(index=False))
        return importance_df
    else:
        print("[evaluator.py] Model does not support feature importance.")
        return None
