import os
import sys
import streamlit as st
from st_pages import Page, show_pages, hide_pages

#st.set_page_config(layout = "wide", initial_sidebar_state = "expanded")

main_script_dir = os.path.dirname(sys.argv[0])

pages = {
    "intro": {
        "path": "app.py",
        "kwargs": {
            "name": "Introduction",
            "icon": ":card_file_box:"
        }
    },
    "eda_summaries": {
        "path": "pages/1_eda_summaries.py",
        "kwargs": {
            "name": "Exploratory Data Analysis",
            "icon": ":face_with_monocle:"
        }
    },
    "metadata": {
        "path": "pages/2_metadata.py",
        "kwargs": {
            "name": "Metadata",
            "icon": ":bookmark_tabs:"
        }
    },
    "bibliography": {
        "path": "pages/3_bibliography.py",
        "kwargs": {
            "name": "Bibliography",
            "icon": ":books:"
        }
    },
    "eda_project_scope": {
        "path": "pages/4_eda_project_scope.py",
        "kwargs": {
            "name": "Exploratory Data Analysis: Project scope",
            "icon": ":honeybee:"
        }
    },
    "diy_exploration": {
        "path": "pages/5_diy_exploration.py",
        "kwargs": {
            "name": "DIY Exploration",
            "icon": ":wrench:"
        }
    }   
}

show_pages_config = []
for key in pages.keys():
    # The path arg of `st_pages.Page` requires the paths to be relative to the
    # currently running script (ie. main), but `streamlit.switch_page` does not
    # like it, thus we append the "eda path prefix" here while creating the
    # Pages, and not in the pages config variable above as it's used by
    # `streamlit.switch_page`
    page_path_with_eda_prefix = os.path.join(
        main_script_dir, pages[key]["path"])
    page = Page(page_path_with_eda_prefix, **pages[key]["kwargs"])
    show_pages_config.append(page)


def pages_menu():
    show_pages(show_pages_config)

    hide_pages([
        pages["eda_project_scope"]["kwargs"]["name"],
        pages["diy_exploration"]["kwargs"]["name"]
    ])
