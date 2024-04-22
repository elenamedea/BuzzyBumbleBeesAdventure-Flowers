import os
import streamlit as st
from utils.pages_menu import pages_menu
from utils import csv_to_df, trim_whitespace_inplace

docs_dir = os.path.abspath(os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "docs"))


pages_menu()

# Title and App summary
st.title("Metadata of the dataset")

app_summary = """

<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>The 
current page provides all the information on the columns of the dataset, as well as the lists of habitats 
of the predefined groups refering as landscapes. The concept of landscapes is formed in the BuzzyBumbleBeesAdventure computer game 
project by its developers, in order to outline the different environments that the plants can be answered. In terms of designing, 
such landscapes could be translated to different game levels. Similarly, the concept of Bordering/Transition plants refers to the
plant species, which are present in a predifined list of habitats and can be used for the transition from one landscape to another.</p>

"""

st.markdown(app_summary, unsafe_allow_html = True)


st.header("Table's metadata")

with open(os.path.join(docs_dir, "metadata.md"), 'r') as f:
    st.markdown(f.read(), unsafe_allow_html=True)


st.header("Tables of habitats referring to the different landscapes")

tables_summary = """

<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>The 
following tables refer to the german and english translation of the habitats.</p> 

"""

st.markdown(tables_summary, unsafe_allow_html = True)

disclaimer_summary = """

:eyes: **_Disclaimer:_** The landscapes are predefined groups of habitats and the bias of the people involved in the 
project can not be eliminated.

"""

st.markdown(disclaimer_summary, unsafe_allow_html = True)

# Fields landscape
st.subheader("Field-meadow landscape")

file_path = "input/fields.csv"

fields = csv_to_df(file_path = file_path)

trim_whitespace_inplace(fields)
st.write(fields)

# Urban landscape
st.subheader("Urban landscape")

file_path = "input/urban.csv"

urban = csv_to_df(file_path = file_path)

trim_whitespace_inplace(urban)
st.write(urban)

# Forest landscape
st.subheader("Forest landscape")

file_path = "input/forest.csv"

forest = csv_to_df(file_path = file_path)

trim_whitespace_inplace(forest)
st.write(forest)

# Foothills landscape
st.subheader("Foothills landscape")

file_path = "input/foothills.csv"

foothills = csv_to_df(file_path = file_path)

trim_whitespace_inplace(foothills)
st.write(foothills)

# Rivers and Lakes landscape
st.subheader("Rivers and Lakes landscape")

file_path = "input/lakes.csv"

lakes = csv_to_df(file_path = file_path)

trim_whitespace_inplace(lakes)
st.write(lakes)

# Alpine landscape
st.subheader("Alpine landscape")

file_path = "input/alpine.csv"

alpine = csv_to_df(file_path = file_path)

trim_whitespace_inplace(alpine)
st.write(alpine)


st.header("Tables of habitats referring to the Bordering/Transition plants")

tables_summary = """

<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>The 
following table refers to the german and english translation of the habitats.</p> 

"""

st.markdown(tables_summary, unsafe_allow_html = True)

disclaimer_summary = """

:eyes: **_Disclaimer:_** The Bordering/Transition plants is a predefined groups of plant species and the bias of the people involved in the 
project can not be eliminated.

"""

st.markdown(disclaimer_summary, unsafe_allow_html = True)

file_path = "input/transition_plants.csv"

transition_plants = csv_to_df(file_path = file_path)

trim_whitespace_inplace(transition_plants)
st.write(transition_plants)
