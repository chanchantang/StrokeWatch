# Download the data: leave argument empty if already manually downloaded data 
def download(automatic_download = False):
    if automatic_download:
        exec(open('data_fetching.py').read())
    else:
        return

# Preprocess the data
def preprocess():
    exec(open('data_preprocessing.py').read())

# Create models: leave argument empty to create all models
def model_building(model=None):
    models = ['decision_tree', 'logistic_regression', 'naive_bayes', 'random_forest', 'voting_classifier']

    if model is None:
        for model in models:
            print(f'{model}')
            exec(open(f'models/{model}.py').read())
    else:
        exec(open(f'models/{model}.py').read())

# Run the app    
def app():
    exec(open('app.py').read(), globals())

def main():
    download(True)
    preprocess()
    model_building('logistic_regression')
    app()

if __name__ == "__main__":
    main()