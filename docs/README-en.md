# Python Examples

## Overview

Doing some interesting things with Python with various libraries, with the aim of demonstrating
how different libraries built for different purposes can be interconnected
to build something useful.

- Manipulating excel files using openpyxl
- Creating a simple web server with Flask
- Scraping the web using Selenium and Beautiful Soup
- Using numpy, pandas, sklearn, seaborn, matplotlib to perform machine learning and create a machine learning model
- Browser automation using Selenium

## Installation (Windows)

Install Python, version 3.9 onwards.

```
powershell
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```

## Tutorial

Before going into the demonstration, it is recommended to view the python files in the `tutorial` folder to understand some concepts used in the demonstration.

Please view them in the following sequence: listcomp -> dict_comp -> slicing -> name

## Demonstration

The following instructions assume that your shell's current working directory is the project root.

### Reading excel files
```powershell
cd web_server/modules
python excel.py
```

### Creating a web server

```powershell
cd web_server
python -m flask --debug run
```

### Static web scraping

Make sure the web server is running before running the following command. See [Creating a web server](#creating-a-web-server)

```powershell
python scrape_static.py
```

### Dynamic web scraping

Make sure the web server is running before running the following command. See [Creating a web server](#creating-a-web-server)

```powershell
python scrape_dynamic.py
```

### Creating a machine learning model
Open `machine_learning/train_diabetes.ipynb`, preferably using Visual Studio Code, as the jupyter notebook on the browser will not provide code completion functionality.

If you would like to open the notebook in the browser, run the following command:
```powershell
python -m notebook machine_learning/train_diabetes.ipynb
```

The training dataset `diabetes.csv` is located in `machine_learning/datasets`. It is recommended to read up on the dataset [here](https://www.kaggle.com/datasets/mathchi/diabetes-data-set).


### Browser automation

Make sure the web server is running before running the following command. See [Creating a web server](#creating-a-web-server)

```powershell
python automate.py
```