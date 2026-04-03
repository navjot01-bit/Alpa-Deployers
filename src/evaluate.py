import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df
def evaluate_data(df):
    print("Rows:", len(df))
    print("Columns:", len(df.columns))
def main():
    input_path = "data/processed/NPRI_2000-2022-cleaned.csv"
    df = load_data(input_path)
    evaluate_data(df)
    print("Evaluation complete.")

if __name__ == "__main__":
    main()
