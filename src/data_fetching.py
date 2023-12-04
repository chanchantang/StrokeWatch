import opendatasets as od
import os

# Kaggle dataset URL
dataset_url = "https://www.kaggle.com/fedesoriano/stroke-prediction-dataset"

# Output directory and file name
output_directory = "raw_data"
output_filename = "raw_data.csv"
output_path = os.path.join(output_directory, output_filename)

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Download the dataset using opendatasets
od.download(dataset_url, data_dir=output_directory)

# Rename the downloaded file to raw_data.csv
downloaded_files = os.listdir(output_directory)
for file in downloaded_files:
    if file.endswith(".csv"):
        os.rename(os.path.join(output_directory, file), output_path)
        break

print(f"Data downloaded and saved to: {output_path}")
