from utils.config import load_config
import pandas as pd
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config/default.yaml")
    args = parser.parse_args()

    cfg = load_config(args.config)

    processed_path = cfg["data"]["processed_path"]

    df = pd.read_csv(processed_path)

    print("Prediction data loaded:", df.shape)

if __name__ == "__main__":
    main()
