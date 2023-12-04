# Stroke Susceptibility Prediction Using Five Machine Learning Models - StrokeWatch

The StrokeWatch app employs various machine learning models, such as random forest and logistic regression, to analyze individual health data and provide personalized risk assessments for stroke occurrence based on factors like age, medical history, and lifestyle.

## Important Links

| [Timesheet](https://1sfu-my.sharepoint.com/:x:/g/personal/kabhishe_sfu_ca/ERc0Vdpa4d9JsOf2QhltWxoBg9t34Slpekk71h27oCd2Yw?e=xaOhcR) | [Slack channel](https://app.slack.com/client/T05JYJAF22G/C05TGPB8D1A/docs/Qp:F05TE8BJEMR/1701591119214) | [Project report](https://www.overleaf.com/project/650c9edaf58339ecbee4649d) |
|-----------|---------------|-------------------------|

## Video/demo/GIF

Record a short video (1:40 - 2 minutes maximum) or gif or a simple screen recording or even using PowerPoint with audio or with text, showcasing your work.


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

Explain briefly what files are found where

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

Provide sufficient instructions to reproduce and install your project. 
Provide _exact_ versions, test on CSIL or reference workstations.

```bash
git clone $THISREPO
cd $THISREPO
pip install -r requirements.txt // TODO: update in the end with app
```

<a name="repro"></a>
## 3. Reproduction
Demonstrate how your work can be reproduced, e.g. the results in your report.
```bash
mkdir tmp && cd tmp
wget https://yourstorageisourbusiness.com/dataset.zip
unzip dataset.zip
conda activate amazing
python evaluate.py --epochs=10 --data=/in/put/dir

mkdir raw_data // maybe not needed
cd src
python src/run.py
python src/app.py
```
Data can be found at ...
Output will be saved in ...

<a name="guide"></a>
## 4. Guidance

- Use [git](https://git-scm.com/book/en/v2)
    - Do NOT use history re-editing (rebase)
    - Commit messages should be informative:
        - No: 'this should fix it', 'bump' commit messages
        - Yes: 'Resolve invalid API call in updating X'
    - Do NOT include IDE folders (.idea), or hidden files. Update your .gitignore where needed.
    - Do NOT use the repository to upload data
- Use [VSCode](https://code.visualstudio.com/) or a similarly powerful IDE
- Use [Copilot for free](https://dev.to/twizelissa/how-to-enable-github-copilot-for-free-as-student-4kal)
- Sign up for [GitHub Education](https://education.github.com/) 
