from pathlib import Path

# Define the base directory
base_dir = Path("fraud-audit-elt")

# List of all directories to create
directories = [
    "datasets",
    "ingestion",
    "infrastructure/adf",
    "infrastructure/datalake",
    "transformations/silver",
    "transformations/gold",
    "powerbi",
    "docs",
]

# Create all directories
for directory in directories:
    (base_dir / directory).mkdir(parents=True, exist_ok=True)
    print(f"Created: {base_dir / directory}")

print(f"\nFolder structure created successfully in '{base_dir}/'")
