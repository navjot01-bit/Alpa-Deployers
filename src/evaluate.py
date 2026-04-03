import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
import pickle


def load_data(path):
    df = pd.read_csv(path)
    return df


def load_model(path):
    with open(path, "rb") as f:
        model = pickle.load(f)
    return model


def evaluate_model(df, model):
    df = df.select_dtypes(include=["number"]).dropna()

    X = df.drop(df.columns[-1], axis=1)
    y = df[df.columns[-1]]

    predictions = model.predict(X)

    mse = mean_squared_error(y, predictions)
    r2 = r2_score(y, predictions)

    print("Mean Squared Error:", mse)
    print("R2 Score:", r2)


def main():
    input_path = "data/raw/NPRI_2000-2022-cleaned.csv"
    model_path = "model.pkl"

    df = load_data(input_path)
    model = load_model(model_path)
    evaluate_model(df, model)


if __name__ == "__main__":
    main()
