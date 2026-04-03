import pandas as pd
import pickle


def load_data(path):
    return pd.read_csv(path)


def load_model(path):
    with open(path, "rb") as f:
        return pickle.load(f)


def make_predictions(df, model):
    df = df.select_dtypes(include=["number"]).dropna()
    X = df.drop(df.columns[-1], axis=1)
    predictions = model.predict(X)
    return predictions


def main():
    input_path = "data/raw/NPRI_2000-2022-cleaned.csv"
    model_path = "model.pkl"
    output_path = "predictions.csv"

    df = load_data(input_path)
    model = load_model(model_path)

    preds = make_predictions(df, model)

    pd.DataFrame(preds, columns=["prediction"]).to_csv(output_path, index=False)

    print("Predictions saved.")


if __name__ == "__main__":
    main()
