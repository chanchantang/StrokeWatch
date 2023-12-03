def preprocess():
    exec(open('data_preprocessing.py').read())

def model_building():
    models = ['decision_tree', 'logistic_regression', 'naive_bayes', 'random_forest', 'voting_classifier']
    for model in models:
        print(f'{model}')
        exec(open(f'models/{model}.py').read())

def main():
    # download data
    # preprocess()
    model_building()
    # run stats
    # run app?


if __name__ == "__main__":
    main()
