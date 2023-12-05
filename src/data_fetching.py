import opendatasets as od
import os
from shutil import move
from os import rmdir
import sys

# Disable printing to output
sys.stdout = open(os.devnull, 'w')

# Kaggle dataset URL
dataset_url = "https://www.kaggle.com/fedesoriano/stroke-prediction-dataset"

# Output directory and file name
output_directory = "../raw_data"
output_filename = "raw_data.csv"
output_path = os.path.join(output_directory, output_filename)

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Download the dataset using opendatasets
od.download(dataset_url, data_dir=output_directory)

# Move dataset to parent folder and remove original folder
downloaded_files = os.listdir(os.path.join(output_directory, 'stroke-prediction-dataset'))
for file in downloaded_files:
    move(os.path.join('../raw_data/stroke-prediction-dataset', file), os.path.join('../raw_data', file))
rmdir(os.path.join('../raw_data/stroke-prediction-dataset'))

# Rename the downloaded file to raw_data.csv 
downloaded_files_moved = os.listdir(output_directory)
for file in downloaded_files:
    if file.endswith(".csv"):
        os.rename(os.path.join(output_directory, file), os.path.join(output_directory, output_filename))
        break
    
sys.stdout = sys.__stdout__
#print(f"Data downloaded and saved to: {output_path}")