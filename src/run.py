import sys
import argparse

DATA_FETCHING_PATH = 'data_fetching.py'
DATA_PREPROCESSING_PATH = 'data_preprocessing.py'
APP_PATH = 'app.py'

# Download the data: leave argument empty if already manually downloaded data 
def download(automatic_download = False):
    if automatic_download:
        exec(data_fetching)
        print('Dataset downloading complete \u2713')
    else:
        return

# Preprocess the data
def preprocess():
    exec(data_preprocessing)
    print("Dataset preprocessing complete \u2713")

# Create models: leave argument empty to create all models
def model_building(model=None):
    models = ['decision_tree', 'logistic_regression', 'naive_bayes', 'random_forest', 'voting_classifier']

    if model is None:
        for model in models:
            try: 
                exec(open(f'models/{model}.py').read())
                print("Model creation complete \u2713")
            except FileNotFoundError as e:
                print(f"{e}, please ensure you are on the correct path")
                sys.exit()
    else:
        try:
            exec(open(f'models/{model}.py').read())
            print("Model creation complete \u2713")
        except FileNotFoundError as e:
            print(f'{e}, please ensure you are on the correct path')
            sys.exit()

# Run the app    
def app():
    exec(stroke_app, globals())

def main(dlData):
    download(dlData)
    preprocess()
    model_building('logistic_regression')
    app()

if __name__ == "__main__":
    try: 
        data_fetching = open(DATA_FETCHING_PATH).read()
        data_preprocessing = open(DATA_PREPROCESSING_PATH).read()
        stroke_app = open(APP_PATH).read()
    except FileNotFoundError as e:
        print(f"{e}, please ensure you are on the correct path")
        sys.exit()

    parser = argparse.ArgumentParser(description="Download data (optional), preprocess data, create models, and run app",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-d", "--download", help="Downloads the data for the model", action='store_true', default=False)
    args = parser.parse_args()
    main(args.download)