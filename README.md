# ConserVision-CameraTrap-Animal-Classification

Welcome to the **Image Classification Project**, using deep learning techniques for camera trap images analysis. The motivation for undertaking the topic of wildlife species classification was to develop an intelligent tool that would assist researchers in the rapid and accurate identification of animal species in camera trap images. The images were collected in Taï National Park by the Wild Chimpanzee Foundation and the Max Planck Institute for Evolutionary Anthropology, and were gathered and published as part of a competition by the organizers on the [DrivenData](https://www.drivendata.org/competitions/87/competition-image-classification-wildlife-conservation/) platform. Camera traps are one of the best tools available for monitoring wildlife populations, but the vast amount of data they generate requires advanced processing. By applying deep learning techniques, the aim was to support conservation efforts by automating the analysis of this data. The classification involved eight categories seven animal species (birds, civets, duikers, hogs, leopards, other monkeys, rodents) and additional class for images with no animals. The goal was to build a model that could predict whether an image contains one of these species or belongs to the empty class.

## Environment Setup

This guide provides all necessary steps to configure local development environment, including setting up a Python virtual environment (venv), installing dependencies, and running the application.

This project was developed on Windows 11, utilizing an NVIDIA RTX 3060 GPU with 6GB VRAM for faster model training and inference. The system also includes a i7-10750h CPU processor with 6 cores, 32 GB of RAM ensuring smooth processing of datasets.

To leverage the GPU for deep learning tasks, I installed **CUDA** (Compute Unified Device Architecture) and **cuDNN** (CUDA Deep Neural Network library) from NVIDIA, which are essential for accelerating deep learning operations. Here's how the installation process was completed:

### 1. Install Visual Studio Code

If you haven't already, download and install **Visual Studio Code** from the official website: [Download Visual Studio Code](https://code.visualstudio.com/)

### 2. Install CUDA and cuDNN (for GPU Acceleration)

Before setting up the Python environment, make sure to install **CUDA 11.2.2** and **cuDNN 8.1.1** to enable GPU acceleration for deep learning tasks. Follow these steps:

1. Download **CUDA 11.2.2** from the official [NVIDIA website](https://developer.nvidia.com/cuda-11.2.2-download-archive).
2. Install **CUDA** and ensure it is installed in the default path: `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\`.
3. Download **cuDNN 8.1.1** from the official [NVIDIA cuDNN page](https://developer.nvidia.com/cudnn).
4. After downloading **cuDNN**, extract the contents and copy the files to the respective directories within the **CUDA Toolkit** installation (e.g., `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\`).
5. Add the following paths to your system **Environment Variables** under `Path` to ensure that your system can locate the CUDA and cuDNN libraries:
   - `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\bin`
   - `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\libnvvp`

### 3. Create a new workspace and virtual environment

Open **Visual Studio Code** and create a new working folder for project. You can create a Python virtual environment using one of the following methods:

#### Method 1: Using the Command Palette
1. Open the **Command Palette**:
   - Shortcut: `Ctrl+Shift+P` (Windows/Linux)
2. Type and select **Python: Select Interpreter**.
3. Choose **Create New Virtual Environment**.
4. Follow the prompts:
   - Select **Venv** as the type of virtual environment.
   - Choose your Python installation (e.g., Python 3.10).
5. After the virtual environment is created, VS Code will automatically switch to it.
6. If VS Code does not automatically detect the environment, use the **Command Palette** (shortcut `Shift + Ctrl + P`), type `Python: Select Interpreter`, and choose the interpreter associated with your newly created environment.

#### Method 2: Using the Terminal
1. In VS Code, open the **PowerShell** terminal (shortcut `Ctrl + ~`). Use the following commands to install python virtual environment:

   ```bash
   python -m pip install virtualenv
   ```

   After create a new Python virtual environment using:

   ```bash
   python -m virtualenv venv -p="C:\Program Files\Python310\python.exe"
   ```

   You may also want to update `pip`:

   ```bash
   python.exe -m pip install --upgrade pip
   ```

2. To activate the virtual environment on Windows, use the following command:

   ```bash
   .\venv\Scripts\activate.ps1
   ```

### 4. Install required packages

Once the interpreter is selected, install all required dependencies (for example by running file `requirements.txt` created before with package versions):

   ```bash
   pip install -r requirements.txt
   ```

To save the current list of dependencies, run the following command:

   ```bash
   pip freeze > requirements.txt
   ```

### 5. Install `ipykernel` when plan to use Jupyter Notebooks

In your virtual environment, you'll need to install the `ipykernel` package. Run the following command inside your virtual environment:

   ```bash
   pip install ipykernel
   ```

## Track experiments and visualize results with [Weights & Biases](https://wandb.ai/site)

### Set up the wandb library

Install the CLI and Python library for interacting with the Weights and Biases API.

```bash
pip install wandb
```

---

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

#### Additional Resources

- [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments)
- [Visual Studio Code - Python Documentation](https://code.visualstudio.com/docs/python/python-tutorial)
- [Conser-vision Practice Area: Image Classification](https://www.drivendata.org/competitions/87/competition-image-classification-wildlife-conservation/)