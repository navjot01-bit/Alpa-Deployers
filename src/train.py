import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle


def load_data(path):
    df = pd.read_csv(path)
    return df


def train_model(df):
    df = df.select_dtypes(include=["number"]).dropna()

    X = df.drop(df.columns[-1], axis=1)
    y = df[df.columns[-1]]

    model = LinearRegression()
    model.fit(X, y)

    return model


def save_model(model, path):
    with open(path, "wb") as f:
        pickle.dump(model, f)


def main():
    input_path = "data/raw/NPRI_2000-2022-cleaned.csv"
    model_path = "model.pkl"

    df = load_data(input_path)
    model = train_model(df)
    save_model(model, model_path)

    print("Model training complete. Model saved.")


if __name__ == "__main__":
    main()
