import os
import streamlit as st
from utils.pages_menu import pages_menu


docs_dir = os.path.abspath(os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "docs"))


pages_menu()

# Title and App summary

with open(os.path.join(docs_dir, "bibliography.md"), 'r') as f:
    st.markdown(f.read(), unsafe_allow_html=True)
