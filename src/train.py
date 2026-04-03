# Training script
from utils.config import load_config
import pandas as pd

def main():
    cfg = load_config("config/default.yaml")

    processed_path = cfg["data"]["processed_path"]

    df = pd.read_csv(processed_path)

    print("Training data loaded:", df.shape)

if __name__ == "__main__":
    main()
