import os
import subprocess
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STAGING_DIR = os.path.join(BASE_DIR, "staging")

DATASETS = {
    #"credit_card": "mlg-ulb/creditcardfraud",
    #"banksim": "ealaxi/banksim1"
    "fraud_detection": "goyaladi/fraud-detection-dataset",
}

def download_dataset(name, kaggle_id):
    target_dir = os.path.join(STAGING_DIR, name)
    os.makedirs(target_dir, exist_ok=True)

    print(f"Downloading {name}...")
    subprocess.run(
        [
            "kaggle", "datasets", "download",
            "-d", kaggle_id,
            "-p", target_dir,
            "--unzip"
        ],
        check=True
    )

if __name__ == "__main__":
    for name, kaggle_id in DATASETS.items():
        download_dataset(name, kaggle_id)

    print("All datasets downloaded successfully.")
