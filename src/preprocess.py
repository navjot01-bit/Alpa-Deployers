from utils.config import load_config
import pandas as pd
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config/default.yaml")
    args = parser.parse_args()

    cfg = load_config(args.config)

    raw_path = cfg["data"]["raw_path"]
    processed_path = cfg["data"]["processed_path"]

    df = pd.read_csv(raw_path)

    print("Data loaded:", df.shape)

    df.to_csv(processed_path, index=False)

    print("Saved processed data")

if __name__ == "__main__":
    main()
