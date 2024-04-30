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

🌼🌿🌷🍀 **Hello Plant Lovers!** 🌸🌱🌹🌾

The current repository is an implementation of a Streamlit multipage app, containing data regarding 131 plants belonging to Flora of Bavaria. 
This data is collected under the scope of the BuzzyBumbleBeesAdventure computer game, as a flowering plants' pool for modelling.

The .csv file with the list of plants can be found [here](https://github.com/elenamedea/BuzzyBumbleBeesAdventure-Flowers/blob/main/input/bbba_eda_eng.csv). 🔗

These plants were selected after the revision of flora lists from the Universities of Regensburg and Munich and the addition of 31 plants, which were chosen based on their peculiarity and importance in bavarian economy and tradition.


📌 This GitHub repository is syncing with a Hugging Face Space, hosting the Streamlit multipage app. For this process, you can check the original source [here](https://huggingface.co/docs/hub/en/spaces-github-actions). 🔗

👀 This README.md is used also in the Hugging Face Spaces. The table at the beginning sets up the required configurations for Hugging Face Spaces.

---

## Hugging Face Spaces

You can visit the app in the Hugging Face Spaces, by clicking on [here](https://huggingface.co/spaces/elenamedea/BBBA-flowers). 🔗

If the Hugging Face Space is paused, click on the *Restart this Space* button (may take a couple of minutes ⏲️).

---

Except for Hugging Face Spaces, Docker is utilized for containerization and app deployment.

## How to setup the bbba-flowers environment with Conda and VsCode

### Prerequisites

- Install [miniconda](https://docs.conda.io/projects/miniconda/en/latest/) 🔗
- `conda init --all`
- `conda env create -f environment.yml`
- `conda activate bbba-flowers` (on OSX you need to `conda deactivate` before this command)
- Set python interpreter for the VsCode Workspace
    - Open VsCode View Menu > Command Palette (Cmd/Ctrl + Shift + P)
    - Search and select `Python: Select Interpreter`
    - Select the options that contains `bbba-flowers`
- Add [Jupyter extention](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) 🔗 to VsCode

### Common tasks

When working in the terminal, use `conda activate bbba-flowers` (on OSX you need to `conda deactivate` before this command).

When working in a Jupyter Notebook, do the following once per Notebook (in case you don't, possibly you will be asked about it on the first attempt to run any code block in that Nodebook)
- Open VsCode View Menu > Command Palette (Cmd/Ctrl + Shift + P)
- Search and select `Notebook: Select Notebook Kernel`
- Select the options that contains `bbba-flowers`

When [adding](https://anaconda.org/search?q=jupyter) 🔗 or removing a package
- Modify `environment.yml` accordingly (don't forget to update channels as needed)
- `conda env update --file environment.yml --prune`
- Also `conda env export --from-history` can be used to get a partially incorrect `environment.yml` of the current environment 
    - Beware that this command does not include `channels` in the generated `environment.yml`
    - Beware that this command includes `prefix` which should not be stored in `environment.yml`, as it changes from one machine to another
    - [Here is the related issue](https://github.com/conda/conda/issues/12842) 🔗 on the official repo

---

### Running with local services

- Code execution in Jupyter Notebooks should work as expected
- Start Streamlit with `python -m streamlit run ./app.py` (don't forget to deactivate conda base env before activating conda `bbba-flowers`)

---

### Deploying Streamlit using Docker

####  Docker Prerequisites

- [Install Docker Engine](https://docs.streamlit.io/deploy/tutorials/docker#install-docker-engine) 🔗
- [Check network port accessibility](https://docs.streamlit.io/deploy/tutorials/docker#check-network-port-accessibility) 🔗

#### Running with docker compose

- `docker compose build`
- `docker compose up -d`
- Visit https://localhost for Streamlit multipage app

