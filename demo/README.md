# Age Detection ML application
==============================

- Please make sure when you use this model in your environment, please download at least two weights from somewhere such as follows:
  - - 転移学習済みXception(年齢推定用)
  - https://www.dropbox.com/s/5s9tkbgqr557vmc/transfer_Xception_29.h5?dl=0
  - - 学習済みweight(顔検出用)
  - https://www.dropbox.com/s/cjjolgk5h0rc1bk/weights.05-3.15.hdf5?dl=0



# Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    ├── detection.py       <- python to make Flask web page
    ├── env
    │   ├── bin
    │   ├── include       
    │   └── lib
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    ├── model.py           <- python to use model SSD300
    ├── models             <- SSD300 model that can detect face
    │   ├── ssd_layers.py
    │   ├── ssd_utils.py       
    │   └── ssd.py
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    ├── static             <- Flask website placeholder
    │   ├── image          <- image output files
    ├── test_images        <- input images holder
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
