import streamlit as st

from utils.pages_menu import pages_menu, pages

st.set_page_config(layout = "wide", initial_sidebar_state = "expanded")

pages_menu()

# Title and App summary

st.title(":seedling::evergreen_tree::blossom::tulip::herb::strawberry::grapes: Welcome plant lovers! :leaves::deciduous_tree::cherry_blossom::rose::four_leaf_clover::leafy_green::blueberries:")

app_summary = """

The current application consists of multiple pages, which are related to the exploratory analysis of data regarding 131 plants belonging to
the Flora of Bavaria. 

This data is collected and stored in a database aiming to be applied as a pool for modelling for the purpose of BuzzyBumbleBeesAdventure computer game, 
simulating the plant pollination.

The plants were selected after the revision of flora lists from Botany undergraduate lectures of the Universities of Regensburg and Munich, and the addition 
of 31 plants, which were chosen based on their peculiarity and importance in bavarian economy and tradition. 

The data collection was conducted based on the literature outlined in the Bibliography page.

Here you can inspect: 

**a)** a general exploratory analysis on the data collection, 

**b)** an exploratory analysis on the scope of the BuzzyBumbleBeesAdventure computer game project, and 

**c)** a Do It Yourself expolation, with customised diagrams and an intergration of PyGWalker, which allows the visualisation, cleaning,
and annotation of the data with simple drag-and-drop operations and even natural language queries.

In addition, under the page Metadata you can find information on data used for the analyses, in order to make tracking and working with it easier.

"""

st.markdown(app_summary, unsafe_allow_html = True)

# Set sidebar markdown for summary
st.sidebar.title("**:bulb: Navigation guidelines**")
    
st.sidebar.markdown(''' 

1. Start with the page :gray[**_Exploratory Data Analysis_**] :face_with_monocle: 
2. You can consult the :gray[**_Metadata_**] :bookmark_tabs: page, which summarizes basic information about data, at any time
3. Similarly, you can refer to the :gray[**_Bibliography_**] :books: page at any time, regarding the literature used for the data collection                 
4. At the bottom of the :gray[**_Exploratory Data Analysis_**] :face_with_monocle: page, you can navigate to the :gray[**_Exploratory Data Analysis: Project scope_**] :honeybee: 
                    page, by pressing the :violet[**_go to Exploratory Data Analysis: Project scope_**] button                    
5. On this page you can dive in the BuzzyBumbleBeesAdventure computer game project, by inspecting several visualisations on this scope                  
6. At the bottom of the :gray[**_Exploratory Data Analysis: Project scope_**] :honeybee: page, you can navigate to the :gray[**_DIY Exploration_**] :wrench: 
                    page, by pressing the :violet[**_go to DIY Exploration_**] button
7. On this page you can explore the data further, via customised plots, and PyGWalker, as well as propose any further exploration of the data
                    
:eyes: It is recommended to use :violet[**_Google Chrome_**] web browser for the app and a :violet[**_24" display_**], in order to get the optimum fit-in of the diagrams. 
For better observation in case of a smaller display, you can expand the diagrams to full screen or zoom out.
                                    
''')

