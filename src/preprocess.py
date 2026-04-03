import os
import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def preprocess_data(df):
    df = df.drop_duplicates()
    return df
def save_data(df, path):
    df.to_csv(path, index=False)
def main():
    input_path = "data/raw/NPRI_2000-2022.csv"
    output_path = "data/processed/NPRI_2000-2022-cleaned.csv"
    df = load_data(input_path)
    df = preprocess_data(df)
    os.makedirs("data/processed", exist_ok=True)
    save_data(df, output_path)
    print("Preprocessing complete. Cleaned file saved.")

if __name__ == "__main__":
    main()
