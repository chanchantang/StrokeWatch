# Stroke Susceptibility Prediction Using Five Machine Learning Models - StrokeWatch

The StrokeWatch app employs various machine learning models, such as random forest and logistic regression, to analyze individual health data and provide personalized risk assessments for stroke occurrence based on factors like age, medical history, and lifestyle.

## Important Links

| [Timesheet](https://1sfu-my.sharepoint.com/:x:/g/personal/kabhishe_sfu_ca/ERc0Vdpa4d9JsOf2QhltWxoBg9t34Slpekk71h27oCd2Yw?e=xaOhcR) | [Slack channel](https://app.slack.com/client/T05JYJAF22G/C05TGPB8D1A/docs/Qp:F05TE8BJEMR/1701591119214) | [Project report](https://www.overleaf.com/project/650c9edaf58339ecbee4649d) |
|-----------|---------------|-------------------------|

## Video

[![Watch the video](https://img.youtube.com/vi/5KdVeHabZSk/maxresdefault.jpg)](https://youtu.be/5KdVeHabZSk)

## Table of Contents
1. [Demo](#demo)

2. [Installation](#installation)

3. [Reproducing this project](#repro)

4. [Guidance](#guide)


<a name="demo"></a>
## 1. Example demo

// TODO: should this be the stats or the app?

A minimal example to showcase your work

```python
from amazing import amazingexample
imgs = amazingexample.demo()
for img in imgs:
    view(img)
```

### What to find where
The repository is laid out as follows:

```bash
repository
├── src                          ## source code of the package itself
│   └── models                   ## model and stat creation
├── raw_data                     ## data imported and created
├── raw_data_old                 ## data imported and created using old encoding
├── saved_models                 ## machine learning models
├── saved_models_old             ## machine learning models using old preprocessing
├── README.md                    ## You are here
├── requirements.txt             ## requirements
```

<a name="installation"></a>

## 2. Installation

In order to install StrokeWatch, along with its associated data and machine learning models, please follow the steps given here:

```bash
git clone [$THISREPO](https://github.com/sfu-cmpt340/project_03.git)
cd $THISREPO
pip install -r requirements.txt 
```

<a name="repro"></a>
## 3. Reproduction
The StrokeWatch can be run through the run.py, all the data downloading and preprocessing will be done through this run.py.
```bash
cd src
python src/run.py
```
Data can be found at raw_data folder after running the run.py 

To reproduce the results in the report:
```bash
cd src
python src/model_stats.py
```

To show the statistics of the dataset:
```bash
cd src
python src/dataset_statistics.py
```
