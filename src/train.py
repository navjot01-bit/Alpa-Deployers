import os
import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df
def train_model(df):
    print("Training model on data:", df.shape)
    return {"status": "trained"}
def save_model(model, path):
    with open(path, "w") as f:
        f.write(str(model))
def main():
    input_path = "data/processed/NPRI_2000-2022-cleaned.csv"
    model_path = "models/model.txt"
    df = load_data(input_path)
    os.makedirs("models", exist_ok=True)
    model = train_model(df)
    save_model(model, model_path)
    print("Training complete. Model saved.")

if __name__ == "__main__":
    main()
