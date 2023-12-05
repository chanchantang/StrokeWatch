import opendatasets as od
import os
import shutil
import sys

# Disable printing to output
sys.stdout = open(os.devnull, 'w')

# Set environment variables
os.environ['KAGGLE_USERNAME'] = 'lunasang'
os.environ['KAGGLE_KEY'] = 'cd00b4abf36b9f1068cfa5818e35c73e'

# Kaggle dataset URL
dataset_url = "https://www.kaggle.com/fedesoriano/stroke-prediction-dataset"

# Output directory and file name
output_directory = "./../raw_data"
output_filename = "raw_data.csv"
output_path = os.path.join(output_directory, output_filename)

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Download the dataset using opendatasets
od.download(dataset_url, data_dir=output_directory)

# Rename the downloaded file to raw_data.csv
downloaded_files = os.listdir(output_directory)

for file in downloaded_files:
    if file == "stroke-prediction-dataset":

        for subfile in os.listdir(os.path.join(output_directory, file)):
            if subfile.endswith(".csv"):
                os.rename(os.path.join(output_directory, file, subfile), output_path)
                break

        shutil.rmtree(os.path.join(output_directory, file))

    if file == "raw_data.csv":
        break

sys.stdout = sys.__stdout__
# print(f"Data downloaded and saved to: {output_path}")

