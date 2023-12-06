# Stroke Susceptibility Prediction Using Five Machine Learning Models - StrokeWatch

The StrokeWatch app employs a logistic regression machine learning model to analyze individual health data and provide personalized risk assessments for stroke occurrence based on factors like age, medical history, and lifestyle.
This model was chosen as the best-suited for StrokeWatch after a comparison of the accuracy and statistics of five different machine learning models: logistic regression, random forest, naive bayes, decision tree and voting classifier.

## Important Links

| [Timesheet](https://1sfu-my.sharepoint.com/:x:/g/personal/kabhishe_sfu_ca/ERc0Vdpa4d9JsOf2QhltWxoBg9t34Slpekk71h27oCd2Yw?e=xaOhcR) | [Slack channel](https://app.slack.com/client/T05JYJAF22G/C05TGPB8D1A/docs/Qp:F05TE8BJEMR/1701591119214) | [Project report](https://www.overleaf.com/project/650c9edaf58339ecbee4649d) |
|-----------|---------------|-------------------------|

## Video

[![Watch the video](https://img.youtube.com/vi/5KdVeHabZSk/maxresdefault.jpg)](https://youtu.be/5KdVeHabZSk)

## Table of Contents
1. [Demo](#demo)

2. [Installation](#installation)

3. [Reproducing this project](#repro)


<a name="demo"></a>
## 1. Example demo
Once you have StrokeWatch installed and running, you're good to go - please refer to the video linked above for a demonstration of the app.

### What to find where
The repository is laid out as follows:

```bash
repository
├── src                          ## source code of the package itself
│   └── models                   ## model and stat creation
├── raw_data                     ## data imported and created
├── saved_models                 ## machine learning models
├── output                       ## the output from model_stats that we use in our report
├── README.md                    ## You are here
├── requirements.txt             ## requirements
```

<a name="installation"></a>

## 2. Installation

In order to install StrokeWatch, along with its associated data and machine learning models, please follow the steps given here:

```bash
git clone https://github.com/sfu-cmpt340/project_03.git
cd project_03
pip install -r requirements.txt 
```
Note: python version newer than installed in requirements will be fine.

<a name="repro"></a>
## 3. Reproduction
The StrokeWatch app can be run through the run.py. All the data downloading and preprocessing will be done through this run.py.
```bash
cd src
python run.py
```
Data can be found in the raw_data folder after running the run.py.

To reproduce the results in the report (must be done after running run.py):
```bash
cd src
python model_stats.py
```
Output can be found at ouput folder after running model_stats.py

To show the statistics of the dataset (must be done after running run.py):
```bash
cd src
python dataset_statistics.py
```
