import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAGING_DIR = os.path.join(BASE_DIR, "staging")

EXPECTED_SCHEMAS = {
    "credit_card": [
        "Time", "V1", "V2", "V3", "V4", "V5",
        "V6", "V7", "V8", "V9", "V10", "V11",
        "V12", "V13", "V14", "V15", "V16",
        "V17", "V18", "V19", "V20", "V21",
        "V22", "V23", "V24", "V25", "V26",
        "V27", "V28", "Amount", "Class"
    ]
}

def validate_csv(dataset_name):
    dataset_path = os.path.join(STAGING_DIR, dataset_name)
    files = [f for f in os.listdir(dataset_path) if f.endswith(".csv")]

    if not files:
        raise FileNotFoundError(f"No CSV found for {dataset_name}")

    file_path = os.path.join(dataset_path, files[0])
    df = pd.read_csv(file_path)

    print(f"{dataset_name}: {len(df)} rows")

    expected_cols = EXPECTED_SCHEMAS.get(dataset_name)
    if expected_cols:
        missing = set(expected_cols) - set(df.columns)
        if missing:
            raise ValueError(f"Missing columns in {dataset_name}: {missing}")

    print(f"{dataset_name} validation passed.")

if __name__ == "__main__":
    for dataset in EXPECTED_SCHEMAS.keys():
        validate_csv(dataset)

    print("All validations successful.")
