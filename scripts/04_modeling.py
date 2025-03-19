import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def train_model(input_file, output_file):
    df = pd.read_csv(input_file)

    # Keep only numeric columns
    df = df[['year', 'homeschool_students']].dropna()

    # Train-test split
    X = df[['year']]
    y = df['homeschool_students']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions and evaluation
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred, squared=False)

    # Save results
    with open(output_file, 'w') as f:
        f.write(f"R-squared: {r2:.4f}\n")
        f.write(f"Root Mean Squared Error (RMSE): {rmse:.2f}\n")

if __name__ == "__main__":
    train_model("../outputs/cleaned_data.csv", "../outputs/model_results.txt")
