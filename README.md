# ConserVision-CameraTrap-Animal-Classification

Welcome to the **Image Classification Project**, using deep learning techniques for camera trap images analysis. The motivation for undertaking the topic of wildlife species classification was to develop an intelligent tool that would assist researchers in the rapid and accurate identification of animal species in camera trap images. The images were collected in Taï National Park by the Wild Chimpanzee Foundation and the Max Planck Institute for Evolutionary Anthropology, and were gathered and published as part of a competition by the organizers on the [DrivenData](https://www.drivendata.org/competitions/87/competition-image-classification-wildlife-conservation/) platform. Camera traps are one of the best tools available for monitoring wildlife populations, but the vast amount of data they generate requires advanced processing. By applying deep learning techniques, the aim was to support conservation efforts by automating the analysis of this data. The classification involved eight categories: seven animal species: birds, civets, duikers, hogs, leopards, other monkeys, and rodents—as well as an additional class for images with no animals. The goal was to build a model that could predict whether an image contains one of these species or belongs to the empty class.

The structure of the project is based on the [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/) project template, as described on [DrivenData-Labs](https://drivendata.co/blog/ccds-v2). This template provides a clear and organized framework for data science projects, ensuring consistency and best practices.

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Deep learning project focused on animal classification in camera trap images.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         src and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── src   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes src a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

---



