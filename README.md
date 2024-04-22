---
title: "BuzzyBumbleBeesAdventure: flowers"
emoji: "🌸"
colorFrom: pink
colorTo: pink
sdk: streamlit
sdk_version: 1.33.0
app_file: app.py
pinned: false
---

# BuzzyBumbleBeesAdventure-Flowers multipage streamlit app

This repository contains three folders:

- **input**,
- **pages**, and 
- **utils**

two python files:

- `app.py`, and 
- `__init__.py`

two yaml files:

- `environment.yml`, and
- `docker-compose.yml`

 a `Dockerfile`, and a `requirements.txt` file .

The `__init__.py` file lets the Python interpreter know that a directory contains code for a Python module. An `__init__.py` file can be blank. Without one, you cannot import modules from another folder into your project.

---

## input

The current folder contains nine .csv files on the data collection, to be used as input to the multipage app.

## pages

The current subfolder contains one folder(**docs**) with two markdown files (`bibliography.md`, and `metadata.md`) and five python files (`1_eda_summaries.py`, `2_metadata.py`, `3_bibliography.py`, `4_eda_project_scope.py`, and `5_diy_exploration.py`). These python files together with markdowns from the **docs** folder consists the major blocks of code for the multipage app.

The`__init__.py` file lets the Python interpreter know that a directory contains code for a Python module. An `__init__.py` file can be blank. Without one, you cannot import modules from another folder into your project.

## utils

The current subfolder contains **24** python files, representing python functions used in the multipage app and a `__init__.py` file, intialising these functions.

## `app.py`

This python file contains the introduction for the multipage app and by running it with streamlit it generates the multipage app.

## `environment.yml`

This yaml file is used to set up a development environment called `bbba-flowers` for the multipage app project.

---

## How to setup the bbba-flowers environment with Conda and VsCode

### Prerequisites

- Install [miniconda](https://docs.conda.io/projects/miniconda/en/latest/)
- `conda init --all`
- `conda env create -f environment.yml`
- `conda activate bbba-flowers` (on OSX you need to `conda deactivate` before this command)
- Set python interpreter for the VsCode Workspace
    - Open VsCode View Menu > Command Palette (Cmd/Ctrl + Shift + P)
    - Search and select `Python: Select Interpreter`
    - Select the options that contains `bbba-flowers`
- Add [Jupyter extention](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) to VsCode

---

### Common tasks

When working in the terminal, use `conda activate bbba-flowers` (on OSX you need to `conda deactivate` before this command).

When working in a Jupyter Notebook, do the following once per Notebook (in case you don't, possibly you will be asked about it on the first attempt to run any code block in that Nodebook)
- Open VsCode View Menu > Command Palette (Cmd/Ctrl + Shift + P)
- Search and select `Notebook: Select Notebook Kernel`
- Select the options that contains `bbba-flowers`

When [adding](https://anaconda.org/search?q=jupyter) or removing a package
- Modify `environment.yml` accordingly (don't forget to update channels as needed)
- `conda env update --file environment.yml --prune`
- Also `conda env export --from-history` can be used to get a partially incorrect `environment.yml` of the current environment 
    - Beware that this command does not include `channels` in the generated `environment.yml`
    - Beware that this command includes `prefix` which should not be stored in `environment.yml`, as it changes from one machine to another
    - [Here is the related issue](https://github.com/conda/conda/issues/12842) on the official repo

---

### Running with docker compose

- Create `.env` file by running `cp .example.env .env` and editing its contents if needed
- `docker compose build`
- `docker compose up -d`
- Visit https://localhost for Streamlit

---

### Running with local services

- Code execution in Jupyter Notebooks should work as expected
- Start Streamlit with `python -m streamlit run ./multipage_app/app.py` (don't forget to deactivate conda base env before activating conda `bbba-flowers`)

