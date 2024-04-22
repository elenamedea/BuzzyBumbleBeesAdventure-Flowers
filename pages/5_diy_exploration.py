import pygwalker as pyg
from pygwalker.api.streamlit import init_streamlit_comm
import streamlit.components.v1 as components
import streamlit as st

from utils import csv_to_df, trim_whitespace_inplace

from utils import generate_unique_presence_parcats_plot, generate_n_landscapes_min_3_n_months_min_5_parcats_plot

from utils import landscapes

from utils import  n_landscapes_color_dict, landscapes_color_dict

from utils.pages_menu import pages_menu

pages_menu()

# Title and App summary

st.title(":test_tube::safety_pin: Do It Yourself Exploration :mechanical_arm::screwdriver:")


# Establish communication between pygwalker and streamlit
init_streamlit_comm()

app_summary = """

The current page provides customized diagrams of the data, exploring further the project scope. 

Furthermore, it allows the user to interact with the data, produce their own plots, and propose any 
further exploration by following the github's issue link and leaving a respective comment.

:eyes: It is recommended to use :violet[**_Google Chrome_**] web browser for the app and a :violet[**_24" display_**], in order to get the optimum fit-in of the diagrams. 
For better observation in case of a smaller display, you can expand the diagrams to full screen or zoom out.

"""
st.markdown(app_summary, unsafe_allow_html=True)

#Set sidebar markdown for summary
st.sidebar.title("**:bulb: Navigation guidelines**")
    
st.sidebar.markdown('''

Firstly, you can check the two customised diagrams uploaded to the page. :chart_with_upwards_trend::chart_with_downwards_trend::bar_chart:
                    
Subsequently, you can move forward to PyGWalker implementation and explore the data by yourself. :test_tube::safety_pin::mechanical_arm::screwdriver:
                    
The table of the data has already been loaded into the PyGWalker worksheet and can be explored by selecting the :violet[**Data**] tab in the pop-up 
                    PyGWalker window. :three_button_mouse::point_up_2::scroll:	

Selecting the :violet[**Visualization**] tab takes you to a Tableau-style UI interactive interface for data
                    visual exploration. :three_button_mouse::point_up_2::magic_wand: 
            
By simply dragging and dropping the columns on the left to :violet[**_X-axis_**], :violet[**_Y-axis_**], :violet[**_Filters_**], 
                    :violet[**_Colors_**], :violet[**_Opacity_**], :violet[**_Size_**], :violet[**_Shape_**], and :violet[**_Details_**] 
                    you can produce a plethora of diagrams to explore and understand deeper the data. :thought_balloon::bulb::abacus::label::art::pushpin:

For more information on PyGWalker, you can check its[documentation](https://docs.kanaries.net/pygwalker), and its 
                    [demo video](https://www.youtube.com/watch?v=u0A-bcQHfmA). :link::books::open_book::clapper::vhs:

All PyGWalker docs are also available by clicking on the exotic bird icon, which is located in the end of the 
                    toolbar (far right). :parrot::peacock::bird::dodo::flamingo:

Finally, by clicking on the github's issue link, you can submit your recommendations on custom diagrams to be produced and added at
                    the respective session of the current page. :three_button_mouse::point_up_2::memo:	
''')

# multipage_app_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
# input_directory_path = os.path.join(multipage_app_dir, "input")

# output_directory_path = os.path.join(multipage_app_dir, "output")

file_path = "input/bbba_eda_eng.csv"

df = csv_to_df(file_path = file_path)

trim_whitespace_inplace(df)

# st.header("Table of data")
# st.write(df)

st.header("Custom diagrams")


st.subheader("Unique plants per Landscape")

# Unique plants per landscape
fig_unique_species = generate_unique_presence_parcats_plot(df, "N. present landscapes", "Scientific name", "Plant species", landscapes, "Landscape",  "Landscape",  " ", landscapes_color_dict, 
                                                           height = 900, width = 1600)
# Show the plot
st.plotly_chart(fig_unique_species)

unique_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
This diagram is generated in order to check which plants are answered only in one landscape, being therefore unique for that landscape. 
Regarding the different landscapes and how they are defined in current project, you can consult the <b><i>Metadata</i></b> page. The color mapping refers to the 6 different 
landscapes of the dataset.</p>"""
st.markdown(unique_summary, unsafe_allow_html = True)


st.subheader("Plants which are present in minimum three landscapes and minimum five months")

# N_present_landscapes >= 3 & months >=5
fig_n_landscapes_min_3_n_moths_min_5 = generate_n_landscapes_min_3_n_months_min_5_parcats_plot(df, "N. present landscapes", "Number of Landscapes", "N. months", "Number of months", "Scientific name", "Plant species", "Family", "Plant Family", 
            " ", n_landscapes_color_dict, height = 900, width = 1600)

# Show the plot
st.plotly_chart(fig_n_landscapes_min_3_n_moths_min_5)                                                                             

n_landscapes_min_3_n_moths_min_5_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
This diagram is generated in order to check which plants are answered in at least three landscapes and for at least five months, being therefore the first candidates for modelling. 
Regarding the different landscapes and how they are defined in current project, you can consult the <b><i>Metadata</i></b> page. The color mapping of refers to the number of 
landscapes, where the plants are present.</p>"""
st.markdown(n_landscapes_min_3_n_moths_min_5_summary, unsafe_allow_html = True)


st.header("PyGWalker")
# Generate the HTML using Pygwalker
pyg_html = pyg.to_html(df)
 
# Embed the HTML into the Streamlit app
components.html(pyg_html, height = 1000, scrolling = True)


st.header("Ideas on custom diagrams")

ideas_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
You have reached the end of the <b><i>Do It Yourself Exploration</i></b>. We hope you had a great time playing around with <b><i>PyGWalker</i></b> and being immersed in the 
amazing world of plants, so far it is covered from the current dataset. In case there are diagrams that you missed from this exploration and/or you have ideas on 
custom diagram please click on the <b><i>following button</i></b> to redirect to the respective github isuue. There you can submit your idea(s) and mention also the page of the app, where 
the diagram(s) should be added.</p>"""
st.markdown(ideas_summary, unsafe_allow_html = True)

st.link_button(":sparkles: Your idea(s) :sparkles:", "https://github.com/elenamedea", type = "primary")

with st.sidebar:
    st.success("Thank you for your contribution! :bouquet:")
    
