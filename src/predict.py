    with open(path, "r") as f:
        model = f.read()
    return model

def make_predictions(df):
    predictions = ["ok"] * len(df)
    return predictions

def main():
    input_path = "data/processed/NPRI_2000-2022-cleaned.csv"
    model_path = "models/model.txt"
    output_path = "data/processed/predictions.csv"
    df = load_data(input_path)
    model = load_model(model_path)
    print("Loaded model:", model)
    predictions = make_predictions(df)
    result = pd.DataFrame({"prediction": predictions})
    result.to_csv(output_path, index=False)

    print("Prediction complete. File saved.")

if __name__ == "__main__":
    main()
