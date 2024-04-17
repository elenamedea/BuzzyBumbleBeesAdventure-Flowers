import streamlit as st

from utils import csv_to_df, trim_whitespace_inplace

from utils import generate_pie_chart, generate_species_treemap

from utils import generate_landscape_barplot, generate_four_features_parcats_plot, generate_two_features_icicle_plot, generate_three_features_parcats_plot

from utils import generate_blossoming_time_barplot, generate_horizontal_boxplot, generate_height_range_barplot, generate_melted_treemap, generate_two_features_parcats_plot

from utils import months, seasons, heights, usages, landscapes

from utils import heights_color_dict, families_color_dict, cycles_color_dict, n_landscapes_color_dict, bool_color_dict, true_color_dict, usages_color_dict, landscapes_color_dict

from utils.pages_menu import pages_menu, pages


pages_menu()

# Title and App summary

st.title("Exploring the Project Scope :honeybee:")

app_summary = """

The current page enables the exploration of the dataset, under the scope of the BuzzyBumbleBeesAdventure computer game. The page consists of two sections, 
one regarding the universal exploration of project-oriented features and the other one regarding the exploration of several features for each of the predefined 
groups refering as landscapes.

In the section of universal exploration, you can inspect the :violet[**_Landscapes_**] of the plant species, the :violet[**_Number of Landscapes, where the plants are present_**], 
and the :violet[**_Bordering/Transition Plants_**].

In the Landscapes section, you can inspect the :violet[**_Blossoming time_**], :violet[**_Height_**], :violet[**_Plant Families_**], :violet[**_Threatened Status_**], 
:violet[**_Usages_**], :violet[**_Edibility_**], :violet[**_Toxicity_**], and :violet[**_Bordering/Transition Plants_**] of the plant species, as well as 
parallel :violet[**_Plant Families and Number of Landscapes_**], :violet[**_Life Cycles, Edibility, and Toxicity_**], :violet[**_Life Cycles, and Edibility_**], and 
:violet[**_Life Cycles, and Toxicity_**].

For any clarification, you can refer to the pages :gray[**_Metadata_**] :bookmark_tabs: and :gray[**_Bibliography_**] :books:, 
regarding the basic information on the data and the literature used for the data collection, respectively.

:eyes: It is recommended to use :violet[**_Google Chrome_**] web browser for the app and a :violet[**_24" display_**], in order to get the optimum fit-in of the diagrams. 
For better observation in case of a smaller display, you can expand the diagrams to full screen or zoom out.
            
"""

st.markdown(app_summary, unsafe_allow_html = True)

# Set sidebar markdown for summary
st.sidebar.title("**:bulb: Navigation guidelines**")
    
st.sidebar.markdown(''' 

The :violet[**.csv**] file to be analysed is loaded in the page and you can look into the data under the respective table. :scroll:
                    
A plethora of diagrams is generated, encapsulating the data through project-oriented features (:violet[**_Landscapes_**], 
                    :violet[**_Number of Landscapes, where the plants are present_**], and :violet[**_Bordering/Transition Plants_**]) and several features 
                    for each of the landscapes (:violet[**_Blossoming time_**], :violet[**_Height_**], :violet[**_Plant Families_**], :violet[**_Threatened Status_**], 
                    :violet[**_Usages_**], :violet[**_Edibility_**],:violet[**_Toxicity_**], :violet[**_Bordering/Transition Plants_**], :violet[**_Plant Families and Number of Landscapes_**],  
                    :violet[**_Life Cycles, Edibility, and Toxicity_**], :violet[**_Life Cycles, and Edibility_**], and :violet[**_Life Cycles, and Toxicity_**]). 
                    :chart_with_upwards_trend::chart_with_downwards_trend::bar_chart:

For each project-oriented feature there are at least two diagrams developed, while for the per Landscape exploration there are so many diagrams (6) developed as the number 
of landscapes. You can monitor them by changing tabs. :three_button_mouse::point_up_2:
                    
After diving into the current exploration and you may have outlined the scope of the BuzzyBumbleBeesAdventure project. :blossom::honeybee: 
                    
You can move to the :gray[**_DIY Exploration_**] :wrench: page and get the chance to explore yourself the dataset, even beyond the project scope. :test_tube::safety_pin::mechanical_arm::screwdriver:

For any clarification on the dataset, you can refer to the :gray[**_Metadata_**] :bookmark_tabs: and :gray[**_Bibliography_**] :books: pages.
                                                                    
''')

           
# eda_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
# input_directory_path = os.path.join(eda_dir, "input")
# output_directory_path = os.path.join(eda_dir, "output")

file_path = "input/bbba_eda_eng.csv"

df = csv_to_df(file_path = file_path)

trim_whitespace_inplace(df)

st.header("Table of data")
st.write(df)

##################################################################### Summaries #####################################################################################################################################
st.header("Universal exploration of project-oriented features")


st.subheader("Landscapes")
tab_l1, tab_l2, tab_l3, tab_l4, tab_l5, tab_l6 = st.tabs(landscapes)

# Pie chart for fields level
fig_fields = generate_pie_chart(df, "Field-meadow", "Field-meadow", "Plants of the 'Field-meadow Landscape'", bool_color_dict, "'Field-meadow Landscape'", height = 1400, width = 1600)
# Pie chart for urban level
fig_urban = generate_pie_chart(df, "Urban", "Urban",  "Plants of the 'Urban Landscape'", bool_color_dict, "'Urban Landscape'", height = 1400, width = 1600)
# Pie chart for forest level
fig_forest = generate_pie_chart(df, "Forest", "Forest", "Plants of the 'Forest Landscape'", bool_color_dict, "'Forest Landscape'", height = 1400, width = 1600)
# Pie chart for mountain level
fig_mountain = generate_pie_chart(df, "Foothills", "Foothills", "Plants of the 'Foothills Landscape'", bool_color_dict, "'Foothills Landscape'", height = 1400, width = 1600)
# Pie chart for lakes level
fig_lakes = generate_pie_chart(df, "Rivers and Lakes", "Rivers and Lakes",  "Plants of the 'Rivers and Lakes Landscape'",  bool_color_dict, "'Rivers and Lakes Landscape'", height = 1400, width = 1600)
# Pie chart for alpine level
fig_alpine = generate_pie_chart(df, "Alpine", "Alpine", "Plants of the 'Alpine Landscape'", bool_color_dict, "'Alpine Landscape'", height = 1400, width = 1600)

with tab_l1:
    st.plotly_chart(fig_fields)

with tab_l2:
    st.plotly_chart(fig_urban)

with tab_l3:
    st.plotly_chart(fig_forest)

with tab_l4:
    st.plotly_chart(fig_mountain)

with tab_l5:
    st.plotly_chart(fig_lakes)

with tab_l6:
    st.plotly_chart(fig_alpine)

landscapes_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
Regarding the different landscapes and how they are defined in current project, you can consult the <b><i>Metadata</i></b> page.</p>"""
st.markdown(landscapes_summary, unsafe_allow_html = True)


st.subheader("Number of Landscapes, where the plants are present")
tab_nl1, tab_nl2 = st.tabs(["Pie chart", "Parallelizing with Plant Families"])

# Pie chart for N_present_landscapes
fig_n_landscapes = generate_pie_chart(df, "N. present landscapes", "N. present landscapes", "Number of Landscapes, where the plants are present", n_landscapes_color_dict, "Number of Landscapes", height = 1400, width = 1600)
# Parallel categories plot for number of landscapes and plant family
fig_n_landscapes_family = generate_two_features_parcats_plot(df, "N. present landscapes", "Number of Landscapes", "Family", "Plant Family", "", families_color_dict, height = 1400, width = 1600)

with tab_nl1:
    st.plotly_chart(fig_n_landscapes)

with tab_nl2:
    st.plotly_chart(fig_n_landscapes_family)

n_landscapes_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
The color mapping of the pie chart refers to the number of landscapes, where the plants are present, while the one of the parallel categories plot refers to 
the 46 different plant families of the dataset.</p>"""
st.markdown(n_landscapes_summary, unsafe_allow_html = True)


st.subheader("Bordering/Transition Plants")
tab_bp1, tab_bp2, tab_bp3, tab_bp4 = st.tabs(["Pie chart", "Species treemap", "Parallelizing with Plant Families", "Parallelizing with Number of Landscapes and Plant Families"])

# Pie chart for Bordering/Transition Plants
fig_transition = generate_pie_chart(df, "Bordering/Transition plants", "Bordering/Transition plants", "Bordering/Transition Plants", bool_color_dict, "Bordering/Transition Plants", height = 1400, width = 1600)
# bordering/transition_plants
transition_treemap = generate_species_treemap(df, "Bordering/Transition plants", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)
# Parallel categories plot for bordering/transition_plants and plant family
transition_plants_data = df[df["Bordering/Transition plants"] == True]
fig_transition_plants_families = generate_two_features_parcats_plot(transition_plants_data, "Bordering/Transition plants", "Bordering/Transition Plants", "Family", "Plant Family", "",  families_color_dict, height = 900, width = 1600)
# Parallel categories plot for bordering/transition_plants, number of landscapes and plant family
fig_transition_n_landscapes_family = generate_three_features_parcats_plot(df, "Bordering/Transition plants", "Bordering/Transition Plants", "N. present landscapes", "Number of Landscapes", "Family", "Plant Family", "", n_landscapes_color_dict, height = 900, width = 1600)


with tab_bp1:
    st.plotly_chart(fig_transition)

with tab_bp2:
    st.plotly_chart(transition_treemap)

with tab_bp3:
    st.plotly_chart(fig_transition_plants_families)

with tab_bp4:
    st.plotly_chart(fig_transition_n_landscapes_family)

bordering_transition_plants_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
Regarding the bordering/transition plants and how they are defined in current project, you can consult the <b><i>Metadata</i></b> page. The color mapping of the 
species treemap and the parallelizing with plant families refers to the 46 different plant families of the dataset, while the one of parallelizing with number 
of landscapes & plant families refers to the number of landscapes, where the plants are present.</p>"""
st.markdown(bordering_transition_plants_summary, unsafe_allow_html = True)

##################################################################### per Landscape #####################################################################################################################################
st.header("Per Landscape Exploration")


st.subheader("Blossoming time (months) of the plants")
tab_f, tab_u, tab_fo, tab_fh, tab_l, tab_a = st.tabs(landscapes)

# Barplot for fields landscape
# Filter data for the current landscape
fields_data = df[df["Field-meadow"] == True]
fig_months_f = generate_blossoming_time_barplot(fields_data, "Scientific name", months, "Months", "Count", "", true_color_dict)
# Barplot for urban landscape
# Filter data for the current landscape
urban_data = df[df["Urban"] == True]
fig_months_u = generate_blossoming_time_barplot(urban_data, "Scientific name", months, "Months", "Count", "", true_color_dict)
# Barplot for forest landscape
# Filter data for the current landscape
forest_data = df[df["Forest"] == True]
fig_months_fo = generate_blossoming_time_barplot(forest_data, "Scientific name", months, "Months", "Count", "", true_color_dict)
# Barplot for foothills landscape
# Filter data for the current landscape
foothills_data = df[df["Foothills"] == True]
fig_months_fh = generate_blossoming_time_barplot(foothills_data, "Scientific name", months, "Months", "Count", "", true_color_dict)
# Barplot for lakes landscape
# Filter data for the current landscape
lakes_data = df[df["Rivers and Lakes"] == True]
fig_months_l = generate_blossoming_time_barplot(lakes_data, "Scientific name", months, "Months", "Count", "", true_color_dict)
# Barplot for alpine landscape
# Filter data for the current landscape
alpine_data = df[df["Alpine"] == True]
fig_months_a = generate_blossoming_time_barplot(alpine_data, "Scientific name", months, "Months", "Count", "", true_color_dict)

with tab_f:
    st.plotly_chart(fig_months_f)

with tab_u:
    st.plotly_chart(fig_months_u)

with tab_fo:
    st.plotly_chart(fig_months_fo)

with tab_fh:
    st.plotly_chart(fig_months_fh)

with tab_l:
    st.plotly_chart(fig_months_l)

with tab_a:
    st.plotly_chart(fig_months_a)

months_per_landscape_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
Regarding the different landscapes and how they are defined in current project, you can consult the <b><i>Metadata</i></b> page. The 
blossoming time refers to the time a plant species occurs and is not coincided with the flowering time of the species.</p>"""
st.markdown(months_per_landscape_summary, unsafe_allow_html = True)


st.subheader("Blossoming time (seasons) of the plants")
tab_f, tab_u, tab_fo, tab_fh, tab_l, tab_a = st.tabs(landscapes)

# Barplot for fields landscape
# Filter data for the current landscape
fields_data = df[df["Field-meadow"] == True]
fig_seasons_f = generate_blossoming_time_barplot(fields_data, "Scientific name", seasons, "Seasons", "Count", "", true_color_dict)
# Barplot for urban landscape
# Filter data for the current landscape
urban_data = df[df["Urban"] == True]
fig_seasons_u = generate_blossoming_time_barplot(urban_data, "Scientific name", seasons, "Seasons", "Count", "", true_color_dict)
# Barplot for forest landscape
# Filter data for the current landscape
forest_data = df[df["Forest"] == True]
fig_seasons_fo = generate_blossoming_time_barplot(forest_data, "Scientific name", seasons, "Seasons", "Count", "", true_color_dict)
# Barplot for foothills landscape
# Filter data for the current landscape
foothills_data = df[df["Foothills"] == True]
fig_seasons_fh = generate_blossoming_time_barplot(foothills_data, "Scientific name", seasons, "Seasons", "Count", "", true_color_dict)
# Barplot for lakes landscape
# Filter data for the current landscape
lakes_data = df[df["Rivers and Lakes"] == True]
fig_seasons_l = generate_blossoming_time_barplot(lakes_data, "Scientific name", seasons, "Seasons", "Count", "", true_color_dict)
# Barplot for alpine landscape
# Filter data for the current landscape
alpine_data = df[df["Alpine"] == True]
fig_seasons_a = generate_blossoming_time_barplot(alpine_data, "Scientific name", seasons, "Seasons", "Count", "", true_color_dict)

with tab_f:
    st.plotly_chart(fig_seasons_f)

with tab_u:
    st.plotly_chart(fig_seasons_u)

with tab_fo:
    st.plotly_chart(fig_seasons_fo)

with tab_fh:
    st.plotly_chart(fig_seasons_fh)

with tab_l:
    st.plotly_chart(fig_seasons_l)

with tab_a:
    st.plotly_chart(fig_seasons_a)

seasons_per_landscape_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
Regarding the different landscapes and how they are defined in current project, you can consult the <b><i>Metadata</i></b> page. The 
blossoming time refers to the time a plant species occurs and is not coincided with the flowering time of the species. Seasons refer to the meteorological seasons in 
Northen Hemisphere. <b><i>Spring</i></b> months are March, April, and May, <b><i>Summer</i></b> months are June, July, and August, <b><i>Autumn</i></b> months are September, 
October, and November, and <b><i>Winter</i></b> months are December, January, and February.</p>"""
st.markdown(seasons_per_landscape_summary, unsafe_allow_html = True)


st.subheader("Height of the plants (boxplots)")
tab_f, tab_u, tab_fo, tab_fh, tab_l, tab_a = st.tabs(landscapes)

# Boxplot for fields landscape
# Filter data for the current landscape
fields_data = df[df["Field-meadow"] == True]
height_boxplot_f = generate_horizontal_boxplot(fields_data, "Scientific name", heights, heights_color_dict, "", "", "Height in cm", height = 900, width = 1600)
# Boxplot for urban landscape
# Filter data for the current landscape
urban_data = df[df["Urban"] == True]
height_boxplot_u = generate_horizontal_boxplot(urban_data, "Scientific name", heights, heights_color_dict, "", "", "Height in cm", height = 900, width = 1600)
# Boxplot for forest landscape
# Filter data for the current landscape
forest_data = df[df["Forest"] == True]
height_boxplot_fo = generate_horizontal_boxplot(forest_data, "Scientific name", heights, heights_color_dict, "", "", "Height in cm", height = 900, width = 1600)
# Boxplot for foothills landscape
# Filter data for the current landscape
foothills_data = df[df["Foothills"] == True]
height_boxplot_fh = generate_horizontal_boxplot(foothills_data, "Scientific name", heights, heights_color_dict, "", "", "Height in cm", height = 900, width = 1600)
# Boxplot for lakes landscape
# Filter data for the current landscape
lakes_data = df[df["Rivers and Lakes"] == True]
height_boxplot_l = generate_horizontal_boxplot(lakes_data, "Scientific name", heights, heights_color_dict, "", "", "Height in cm", height = 900, width = 1600)
# Boxplot for alpine landscape
# Filter data for the current landscape
alpine_data = df[df["Alpine"] == True]
height_boxplot_a = generate_horizontal_boxplot(alpine_data, "Scientific name", heights, heights_color_dict, "", "", "Height in cm", height = 900, width = 1600)

with tab_f:
    st.plotly_chart(height_boxplot_f)

with tab_u:
    st.plotly_chart(height_boxplot_u)

with tab_fo:
    st.plotly_chart(height_boxplot_fo)

with tab_fh:
    st.plotly_chart(height_boxplot_fh)

with tab_l:
    st.plotly_chart(height_boxplot_l)

with tab_a:
    st.plotly_chart(height_boxplot_a)

st.subheader("Height range of the plants (barplots)")
tab_f, tab_u, tab_fo, tab_fh, tab_l, tab_a = st.tabs(landscapes)

# Barplot per species for fields landscape
# Filter data for the current landscape
fields_data = df[df["Field-meadow"] == True]
height_barplot_f = generate_height_range_barplot(fields_data, "Scientific name", heights, heights_color_dict, "", "Plant species", "Height in cm", "Height")
# Barplot per species for urban landscape
# Filter data for the current landscape
urban_data = df[df["Urban"] == True]
height_barplot_u = generate_height_range_barplot(urban_data, "Scientific name", heights, heights_color_dict, "", "Plant species", "Height in cm", "Height")
# Barplot per species for forest landscape
# Filter data for the current landscape
forest_data = df[df["Forest"] == True]
height_barplot_fo = generate_height_range_barplot(forest_data, "Scientific name", heights, heights_color_dict, "", "Plant species", "Height in cm", "Height")
# Barplot per species for foothills landscape
# Filter data for the current landscape
foothills_data = df[df["Foothills"] == True]
height_barplot_fh = generate_height_range_barplot(foothills_data, "Scientific name", heights, heights_color_dict, "", "Plant species", "Height in cm", "Height")
# Barplot per species for lakes landscape
# Filter data for the current landscape
lakes_data = df[df["Rivers and Lakes"] == True]
height_barplot_l = generate_height_range_barplot(lakes_data, "Scientific name", heights, heights_color_dict, "", "Plant species", "Height in cm", "Height")
# Barplot per species for alpine landscape
# Filter data for the current landscape
alpine_data = df[df["Alpine"] == True]
height_barplot_a = generate_height_range_barplot(alpine_data, "Scientific name", heights, heights_color_dict, "", "Plant species", "Height in cm", "Height")

with tab_f:
    st.plotly_chart(height_barplot_f)

with tab_u:
    st.plotly_chart(height_barplot_u)

with tab_fo:
    st.plotly_chart(height_barplot_fo)

with tab_fh:
    st.plotly_chart(height_barplot_fh)

with tab_l:
    st.plotly_chart(height_barplot_l)

with tab_a:
    st.plotly_chart(height_barplot_a)

height_per_landscape_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
Regarding the different landscapes and how they are defined in current project, you can consult the <b><i>Metadata</i></b> page. These boxplots and barplots are 
generated in order to summarize the height range of the plant species. For additional information, you may refer to the <b><i>Documentation of the Plotly library</i></b> 
used for these visualisations and/or the <b><i>Wikipedia</i></b> website.</p>"""
st.markdown(height_per_landscape_summary, unsafe_allow_html = True)


st.subheader("Plant Families")
tab_f, tab_u, tab_fo, tab_fh, tab_l, tab_a = st.tabs(landscapes)

# Barplot of the families for fields landscape
fig_families_f = generate_landscape_barplot(df, "Field-meadow", "Family", "", "Plant Families", "Count", 18, 16, -45, landscapes_color_dict, height = 900, width = 1600)
# Barplot of the families for urban landscape
fig_families_u = generate_landscape_barplot(df, "Urban", "Family", "", "Plant Families", "Count", 18, 16, -45, landscapes_color_dict, height = 900, width = 1600)
# Barplot of the families for forest landscape
fig_families_fo = generate_landscape_barplot(df, "Forest", "Family", "", "Plant Families", "Count", 18, 16, -45, landscapes_color_dict, height = 900, width = 1600)
# Barplot of the families for foothills landscape
fig_families_fh = generate_landscape_barplot(df, "Foothills", "Family", "", "Plant Families", "Count", 18, 16, -45, landscapes_color_dict, height = 900, width = 1600)
# Barplot of the families for lakes landscape
fig_families_l = generate_landscape_barplot(df, "Rivers and Lakes", "Family", "", "Plant Families", "Count", 18, 16, -45, landscapes_color_dict, height = 900, width = 1600)
# Barplot of the families for alpine landscape
fig_families_a = generate_landscape_barplot(df, "Alpine", "Family", "", "Plant Families", "Count", 18, 16, -45, landscapes_color_dict, height = 900, width = 1600)

with tab_f:
    st.plotly_chart(fig_families_f)

with tab_u:
    st.plotly_chart(fig_families_u)

with tab_fo:
    st.plotly_chart(fig_families_fo)

with tab_fh:
    st.plotly_chart(fig_families_fh)

with tab_l:
    st.plotly_chart(fig_families_l)

with tab_a:
    st.plotly_chart(fig_families_a)

families_barplot_per_landscape_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
Regarding the different landscapes and how they are defined in current project, you can consult the <b><i>Metadata</i></b> page. The color mapping refers to the 6 different 
landscapes of the dataset.</p>"""
st.markdown(families_barplot_per_landscape_summary, unsafe_allow_html = True)


st.subheader("Plant Families and Number of Landscapes")
tab_f, tab_u, tab_fo, tab_fh, tab_l, tab_a = st.tabs(landscapes)

# Parallel categories plot for plant families, number of landscapes and fields landscape
# Filter data for the current landscape
fields_data = df[df["Field-meadow"] == True]
fig_n_landscapes_family_f = generate_two_features_parcats_plot(fields_data, "N. present landscapes", "Number of Landscapes", "Family", "Plant Family", "", families_color_dict, height = 1300, width = 1600)
# Parallel categories plot for plant families, number of landscapes and urban landscape
# Filter data for the current landscape
urban_data = df[df["Urban"] == True]
fig_n_landscapes_family_u = generate_two_features_parcats_plot(urban_data, "N. present landscapes", "Number of Landscapes", "Family", "Plant Family", "", families_color_dict, height = 1300, width = 1600)
# Parallel categories plot for plant families, number of landscapes and forest landscape
# Filter data for the current landscape
forest_data = df[df["Forest"] == True]
fig_n_landscapes_family_fo = generate_two_features_parcats_plot(forest_data, "N. present landscapes", "Number of Landscapes", "Family", "Plant Family", "", families_color_dict, height = 1200, width = 1600)
# Parallel categories plot for plant families, number of landscapes and foothills landscape
# Filter data for the current landscape
foothills_data = df[df["Foothills"] == True]
fig_n_landscapes_family_fh = generate_two_features_parcats_plot(foothills_data, "N. present landscapes", "Number of Landscapes", "Family", "Plant Family", "", families_color_dict, height = 900, width = 1600)
# Parallel categories plot for plant families, number of landscapes and lakes landscape
# Filter data for the current landscape
lakes_data = df[df["Rivers and Lakes"] == True]
fig_n_landscapes_family_l = generate_two_features_parcats_plot(lakes_data, "N. present landscapes", "Number of Landscapes", "Family", "Plant Family", "", families_color_dict, height = 900, width = 1600)
# Parallel categories plot for plant families, number of landscapes and alpine landscape
# Filter data for the current landscape
alpine_data = df[df["Alpine"] == True]
fig_n_landscapes_family_a = generate_two_features_parcats_plot(alpine_data, "N. present landscapes", "Number of Landscapes", "Family", "Plant Family", "", families_color_dict, height = 900, width = 1600)

with tab_f:
    st.plotly_chart(fig_n_landscapes_family_f)

with tab_u:
    st.plotly_chart(fig_n_landscapes_family_u)

with tab_fo:
    st.plotly_chart(fig_n_landscapes_family_fo)

with tab_fh:
    st.plotly_chart(fig_n_landscapes_family_fh)

with tab_l:
    st.plotly_chart(fig_n_landscapes_family_l)

with tab_a:
    st.plotly_chart(fig_n_landscapes_family_a)

families_n_landscapes_per_landscape_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
Regarding the different landscapes and how they are defined in current project, you can consult the <b><i>Metadata</i></b> page. The color mapping refers to the 46 different plant 
families of the dataset.</p>"""
st.markdown(families_n_landscapes_per_landscape_summary, unsafe_allow_html = True)


st.subheader("Threatened Status (barplots)")
tab_f, tab_u, tab_fo, tab_fh, tab_l, tab_a = st.tabs(landscapes)

# Barplot of Threatened Status for fields landscape
fig_threatened_f = generate_landscape_barplot(df, "Field-meadow", "Threatened", "", "Threatened Status", "Count", 20, 18, 0, landscapes_color_dict, height = 900, width = 1600)
# Barplot of Threatened Status for urban landscape
fig_threatened_u = generate_landscape_barplot(df, "Urban", "Threatened", "", "Threatened Status", "Count", 20, 18, 0, landscapes_color_dict, height = 900, width = 1600)
# Barplot of Threatened Status for forest landscape
fig_threatened_fo = generate_landscape_barplot(df, "Forest", "Threatened", "", "Threatened Status", "Count", 20, 18, 0, landscapes_color_dict, height = 900, width = 1600)
# Barplot of Threatened Status for foothills landscape
fig_threatened_fh = generate_landscape_barplot(df, "Foothills", "Threatened", "", "Threatened Status", "Count", 20, 18, 0, landscapes_color_dict, height = 900, width = 1600)
# Barplot of Threatened Status for lakes landscape
fig_threatened_l = generate_landscape_barplot(df, "Rivers and Lakes", "Threatened", "", "Threatened Status", "Count", 20, 18, 0, landscapes_color_dict, height = 900, width = 1600)
# Barplot of Threatened Status for alpine landscape
fig_threatened_a = generate_landscape_barplot(df, "Alpine", "Threatened", "", "Threatened Status", "Count", 20, 18, 0, landscapes_color_dict, height = 900, width = 1600)

with tab_f:
    st.plotly_chart(fig_threatened_f)

with tab_u:
    st.plotly_chart(fig_threatened_u)

with tab_fo:
    st.plotly_chart(fig_threatened_fo)

with tab_fh:
    st.plotly_chart(fig_threatened_fh)

with tab_l:
    st.plotly_chart(fig_threatened_l)

with tab_a:
    st.plotly_chart(fig_threatened_a)

threatened_barplot_per_landscape_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
Regarding the different landscapes and how they are defined in current project, you can consult the <b><i>Metadata</i></b> page. The color mapping refers to the 6 different 
landscapes of the dataset.</p>"""
st.markdown(threatened_barplot_per_landscape_summary, unsafe_allow_html = True)


st.subheader("Threatened Status (species treemaps)")
tab_f, tab_u, tab_fo, tab_fh, tab_l, tab_a = st.tabs(landscapes)

# Species treemap of Threatened Status for fields landscape
# Filter data for the current landscape
fields_data = df[df["Field-meadow"] == True]
fig_threatened_f = generate_species_treemap(fields_data, "Threatened", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)
# Species treemap of Threatened Status for  urban landscape
# Filter data for the current landscape
urban_data = df[df["Urban"] == True]
fig_threatened_u = generate_species_treemap(urban_data, "Threatened", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)
# Species treemap of Threatened Status for forest landscape
# Filter data for the current landscape
forest_data = df[df["Forest"] == True]
fig_threatened_fo = generate_species_treemap(forest_data, "Threatened", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)
# Species treemap of Threatened Status for foothills landscape
# Filter data for the current landscape
foothills_data = df[df["Foothills"] == True]
fig_threatened_fh = generate_species_treemap(foothills_data, "Threatened", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)
# Species treemap of Threatened Status for lakes landscape
# Filter data for the current landscape
lakes_data = df[df["Rivers and Lakes"] == True]
fig_threatened_l = generate_species_treemap(lakes_data, "Threatened", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)
# Species treemap of Threatened Status for alpine landscape
# Filter data for the current landscape
alpine_data = df[df["Alpine"] == True]
fig_threatened_a = generate_species_treemap(alpine_data, "Threatened", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)

with tab_f:
    st.plotly_chart(fig_threatened_f)

with tab_u:
    st.plotly_chart(fig_threatened_u)

with tab_fo:
    st.plotly_chart(fig_threatened_fo)

with tab_fh:
    st.plotly_chart(fig_threatened_fh)

with tab_l:
    st.plotly_chart(fig_threatened_l)

with tab_a:
    st.plotly_chart(fig_threatened_a)

threatened_species_treemap_per_landscape_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
Regarding the different landscapes and how they are defined in current project, you can consult the <b><i>Metadata</i></b> page. The color mapping refers to the 46 different plant 
families of the dataset.</p>"""
st.markdown(threatened_species_treemap_per_landscape_summary, unsafe_allow_html = True)


st.subheader("Usages of the plants")
tab_f, tab_u, tab_fo, tab_fh, tab_l, tab_a = st.tabs(landscapes)

# Usages for fields landscape
# Filter data for the current landscape
fields_data = df[df["Field-meadow"] == True]
usages_treemap_f = generate_melted_treemap(fields_data, "Scientific name", usages, usages_color_dict, " ", height = 1400, width = 1650)
# Usages for urban landscape
# Filter data for the current landscape
urban_data = df[df["Urban"] == True]
usages_treemap_u = generate_melted_treemap(urban_data, "Scientific name", usages, usages_color_dict, " ", height = 1400, width = 1650)
# Usages for forest landscape
# Filter data for the current landscape
forest_data = df[df["Forest"] == True]
usages_treemap_fo = generate_melted_treemap(forest_data, "Scientific name", usages, usages_color_dict, " ", height = 1400, width = 1650)
# Usages for foothills landscape
# Filter data for the current landscape
foothills_data = df[df["Foothills"] == True]
usages_treemap_fh = generate_melted_treemap(foothills_data, "Scientific name", usages, usages_color_dict, " ", height = 1400, width = 1650)
# Usages for lakes landscape
# Filter data for the current landscape
lakes_data = df[df["Rivers and Lakes"] == True]
usages_treemap_l = generate_melted_treemap(lakes_data, "Scientific name", usages, usages_color_dict, " ", height = 1400, width = 1650)
# Usages for alpine landscape
# Filter data for the current landscape
alpine_data = df[df["Alpine"] == True]
usages_treemap_a = generate_melted_treemap(alpine_data, "Scientific name", usages, usages_color_dict, " ", height = 1400, width = 1650)

with tab_f:
    st.plotly_chart(usages_treemap_f)

with tab_u:
    st.plotly_chart(usages_treemap_u)

with tab_fo:
    st.plotly_chart(usages_treemap_fo)

with tab_fh:
    st.plotly_chart(usages_treemap_fh)

with tab_l:
    st.plotly_chart(usages_treemap_l)

with tab_a:
    st.plotly_chart(usages_treemap_a)

usages_treemap_per_landscape_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
Regarding the different landscapes and how they are defined in current project, you can consult the <b><i>Metadata</i></b> page. The color mapping refers to the 27 different 
plants' usage categories of the dataset.</p>"""
st.markdown(usages_treemap_per_landscape_summary, unsafe_allow_html = True)


st.subheader("Edibility of the plants (species treemaps)")
tab_f, tab_u, tab_fo, tab_fh, tab_l, tab_a = st.tabs(landscapes)

# Edibility for fields landscape
# Filter data for the current landscape
fields_data = df[df["Field-meadow"] == True]
edible_treemap_f = generate_species_treemap(fields_data, "Edible", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)
# Edibility for urban landscape
# Filter data for the current landscape
urban_data = df[df["Urban"] == True]
edible_treemap_u = generate_species_treemap(urban_data, "Edible", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)
# Edibility for forest landscape
# Filter data for the current landscape
forest_data = df[df["Forest"] == True]
edible_treemap_fo = generate_species_treemap(forest_data, "Edible", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)
# Edibility for foothills landscape
# Filter data for the current landscape
foothills_data = df[df["Foothills"] == True]
edible_treemap_fh = generate_species_treemap(foothills_data, "Edible", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)
# Edibility for lakes landscape
# Filter data for the current landscape
lakes_data = df[df["Rivers and Lakes"] == True]
edible_treemap_l = generate_species_treemap(lakes_data, "Edible", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)
# Edibility for alpine landscape
# Filter data for the current landscape
alpine_data = df[df["Alpine"] == True]
edible_treemap_a = generate_species_treemap(alpine_data, "Edible", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)

with tab_f:
    st.plotly_chart(edible_treemap_f)

with tab_u:
    st.plotly_chart(edible_treemap_u)

with tab_fo:
    st.plotly_chart(edible_treemap_fo)

with tab_fh:
    st.plotly_chart(edible_treemap_fh)

with tab_l:
    st.plotly_chart(edible_treemap_l)

with tab_a:
    st.plotly_chart(edible_treemap_a)

edible_treemap_per_landscape_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
Regarding the different landscapes and how they are defined in current project, you can consult the <b><i>Metadata</i></b> page. The color mapping refers to the 46 different plant 
families of the dataset.</p>"""
st.markdown(edible_treemap_per_landscape_summary, unsafe_allow_html = True)


st.subheader("Toxicity of the plants (species treemaps)")
tab_f, tab_u, tab_fo, tab_fh, tab_l, tab_a = st.tabs(landscapes)

# Toxicity for fields landscape
# Filter data for the current landscape
fields_data = df[df["Field-meadow"] == True]
poisonous_treemap_f = generate_species_treemap(fields_data, "Poisonous", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)
# Toxicity for urban landscape
# Filter data for the current landscape
urban_data = df[df["Urban"] == True]
poisonous_treemap_u = generate_species_treemap(urban_data, "Poisonous", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)
# Toxicity for forest landscape
# Filter data for the current landscape
forest_data = df[df["Forest"] == True]
poisonous_treemap_fo = generate_species_treemap(forest_data, "Poisonous", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)
# Toxicity for foothills landscape
# Filter data for the current landscape
foothills_data = df[df["Foothills"] == True]
poisonous_treemap_fh = generate_species_treemap(foothills_data, "Poisonous", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)
# Toxicity for lakes landscape
# Filter data for the current landscape
lakes_data = df[df["Rivers and Lakes"] == True]
poisonous_treemap_l = generate_species_treemap(lakes_data, "Poisonous", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)
# Toxicity for alpine landscape
# Filter data for the current landscape
alpine_data = df[df["Alpine"] == True]
poisonous_treemap_a = generate_species_treemap(alpine_data, "Poisonous", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)

with tab_f:
    st.plotly_chart(poisonous_treemap_f)

with tab_u:
    st.plotly_chart(poisonous_treemap_u)

with tab_fo:
    st.plotly_chart(poisonous_treemap_fo)

with tab_fh:
    st.plotly_chart(poisonous_treemap_fh)

with tab_l:
    st.plotly_chart(poisonous_treemap_l)

with tab_a:
    st.plotly_chart(poisonous_treemap_a)

poisonous_treemap_per_landscape_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
Regarding the different landscapes and how they are defined in current project, you can consult the <b><i>Metadata</i></b> page. The color mapping refers to the 46 different plant 
families of the dataset.</p>"""
st.markdown(poisonous_treemap_per_landscape_summary, unsafe_allow_html = True)


st.subheader("Life Cycles, Edibility, and Toxicity of the plants (parallel categories)")
tab_f, tab_u, tab_fo, tab_fh, tab_l, tab_a = st.tabs(landscapes)

# Life Cycles, Edibility, and Toxicity for fields landscape
cycles_edible_poisonous_f = generate_four_features_parcats_plot(df, "Field-meadow", "Life cycle", "Life cycles", "Edible", "Poisonous", "", landscapes_color_dict, height = 900, width = 1600)
# Life Cycles, Edibility, and Toxicity for urban landscape
cycles_edible_poisonous_u = generate_four_features_parcats_plot(df, "Urban", "Life cycle", "Life cycles", "Edible", "Poisonous", "", landscapes_color_dict, height = 900, width = 1600)
# Life Cycles, Edibility, and Toxicity for forest landscape
cycles_edible_poisonous_fo = generate_four_features_parcats_plot(df, "Forest", "Life cycle", "Life cycles", "Edible", "Poisonous", "", landscapes_color_dict, height = 900, width = 1600)
# Life Cycles, Edibility, and Toxicity for foothills landscape
cycles_edible_poisonous_fh = generate_four_features_parcats_plot(df, "Foothills", "Life cycle", "Life cycles", "Edible", "Poisonous", "", landscapes_color_dict, height = 900, width = 1600)
# Life Cycles, Edibility, and Toxicity for lakes landscape
cycles_edible_poisonous_l = generate_four_features_parcats_plot(df, "Rivers and Lakes", "Life cycle", "Life cycles", "Edible", "Poisonous", "", landscapes_color_dict, height = 900, width = 1600)
# Life Cycles, Edibility, and Toxicity for alpine landscape
cycles_edible_poisonous_a = generate_four_features_parcats_plot(df, "Alpine", "Life cycle", "Life cycles", "Edible", "Poisonous", "", landscapes_color_dict, height = 900, width = 1600)

with tab_f:
    st.plotly_chart(cycles_edible_poisonous_f)

with tab_u:
    st.plotly_chart(cycles_edible_poisonous_u)

with tab_fo:
    st.plotly_chart(cycles_edible_poisonous_fo)

with tab_fh:
    st.plotly_chart(cycles_edible_poisonous_fh)

with tab_l:
    st.plotly_chart(cycles_edible_poisonous_l)

with tab_a:
    st.plotly_chart(cycles_edible_poisonous_a)

cycles_edible_poisonous_per_landscape_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
Regarding the different landscapes and how they are defined in current project, you can consult the <b><i>Metadata</i></b> page. The color mapping refers to the 6 different 
landscapes of the dataset.</p>"""
st.markdown(cycles_edible_poisonous_per_landscape_summary, unsafe_allow_html = True)


st.subheader("Life Cycles, and Edibility of the plants (icicle)")
tab_f, tab_u, tab_fo, tab_fh, tab_l, tab_a = st.tabs(landscapes)

# Life Cycles, and Edibility for fields landscape
cycles_edible_f = generate_two_features_icicle_plot(df, "Field-meadow", "Life cycle", "Edible", "", cycles_color_dict, height = 1000, width = 1000)
# Life Cycles, and Edibility for urban landscape
cycles_edible_u = generate_two_features_icicle_plot(df, "Urban", "Life cycle", "Edible", "", cycles_color_dict, height = 1000, width = 1000)
# Life Cycles, and Edibility for forest landscape
cycles_edible_fo = generate_two_features_icicle_plot(df, "Forest", "Life cycle", "Edible", "", cycles_color_dict, height = 1000, width = 1000)
# Life Cycles, and Edibility for foothills landscape
cycles_edible_fh = generate_two_features_icicle_plot(df, "Foothills", "Life cycle", "Edible", "", cycles_color_dict, height = 1000, width = 1000)
# Life Cycles, and Edibility for lakes landscape
cycles_edible_l = generate_two_features_icicle_plot(df, "Rivers and Lakes", "Life cycle", "Edible", "", cycles_color_dict, height = 1000, width = 1000)
# Life Cycles, and Edibility for alpine landscape
cycles_edible_a = generate_two_features_icicle_plot(df, "Alpine", "Life cycle", "Edible", "", cycles_color_dict, height = 1000, width = 1000)


with tab_f:
    st.plotly_chart(cycles_edible_f)

with tab_u:
    st.plotly_chart(cycles_edible_u)

with tab_fo:
    st.plotly_chart(cycles_edible_fo)

with tab_fh:
    st.plotly_chart(cycles_edible_fh)

with tab_l:
    st.plotly_chart(cycles_edible_l)

with tab_a:
    st.plotly_chart(cycles_edible_a)

st.subheader("Life Cycles, and Toxicity of the plants (icicle)")
tab_f, tab_u, tab_fo, tab_fh, tab_l, tab_a = st.tabs(landscapes)

# Life Cycles, and Toxicity for fields landscape
cycles_poisonous_f = generate_two_features_icicle_plot(df, "Field-meadow", "Life cycle", "Poisonous", "", cycles_color_dict, height = 1000, width = 1000)
# Life Cycles, and Toxicity for urban landscape
cycles_poisonous_u = generate_two_features_icicle_plot(df, "Urban", "Life cycle", "Poisonous", "", cycles_color_dict, height = 1000, width = 1000)
# Life Cycles, and Toxicity for forest landscape
cycles_poisonous_fo = generate_two_features_icicle_plot(df, "Forest", "Life cycle", "Poisonous", "", cycles_color_dict, height = 1000, width = 1000)
# Life Cycles, and Toxicity for foothills landscape
cycles_poisonous_fh = generate_two_features_icicle_plot(df, "Foothills", "Life cycle", "Poisonous", "", cycles_color_dict, height = 1000, width = 1000)
# Life Cycles, and Toxicity for lakes landscape
cycles_poisonous_l = generate_two_features_icicle_plot(df, "Rivers and Lakes", "Life cycle", "Poisonous", "", cycles_color_dict, height = 1000, width = 1000)
# Life Cycles, and Toxicity for alpine landscape
cycles_poisonous_a = generate_two_features_icicle_plot(df, "Alpine", "Life cycle", "Poisonous", "", cycles_color_dict, height = 1000, width = 1000)


with tab_f:
    st.plotly_chart(cycles_poisonous_f)

with tab_u:
    st.plotly_chart(cycles_poisonous_u)

with tab_fo:
    st.plotly_chart(cycles_poisonous_fo)

with tab_fh:
    st.plotly_chart(cycles_poisonous_fh)

with tab_l:
    st.plotly_chart(cycles_poisonous_l)

with tab_a:
    st.plotly_chart(cycles_poisonous_a)

cycles_per_landscape_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
Regarding the different landscapes and how they are defined in current project as well as the terminology of the life cycles, you can consult the <b><i>Metadata</i></b> 
page. The color mapping refers to the 7 different plants' life cycles of the dataset.</p>"""
st.markdown(cycles_per_landscape_summary, unsafe_allow_html = True)


st.subheader("Bordering/Transition Plants (species treemaps)")
tab_f, tab_u, tab_fo, tab_fh, tab_l, tab_a = st.tabs(landscapes)

# Bordering/Transition Plants for fields landscape
# Filter data for the current landscape
fields_data = df[df["Field-meadow"] == True]
transition_plants_treemap_f = generate_species_treemap(fields_data, "Bordering/Transition plants", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)
# Bordering/Transition Plants for urban landscape
# Filter data for the current landscape
urban_data = df[df["Urban"] == True]
transition_plants_treemap_u = generate_species_treemap(urban_data, "Bordering/Transition plants", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)
# Bordering/Transition Plants for forest landscape
# Filter data for the current landscape
forest_data = df[df["Forest"] == True]
transition_plants_treemap_fo = generate_species_treemap(forest_data, "Bordering/Transition plants", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)
# Bordering/Transition Plants for foothills landscape
# Filter data for the current landscape
foothills_data = df[df["Foothills"] == True]
transition_plants_treemap_fh = generate_species_treemap(foothills_data, "Bordering/Transition plants", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)
# Bordering/Transition Plants for lakes landscape
# Filter data for the current landscape
lakes_data = df[df["Rivers and Lakes"] == True]
transition_plants_treemap_l = generate_species_treemap(lakes_data, "Bordering/Transition plants", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)
# Bordering/Transition Plants for alpine landscape
# Filter data for the current landscape
alpine_data = df[df["Alpine"] == True]
transition_plants_treemap_a = generate_species_treemap(alpine_data, "Bordering/Transition plants", "Scientific name", "Family", "", families_color_dict, height = 900, width = 1600)

with tab_f:
    st.plotly_chart(transition_plants_treemap_f)

with tab_u:
    st.plotly_chart(transition_plants_treemap_u)

with tab_fo:
    st.plotly_chart(transition_plants_treemap_fo)

with tab_fh:
    st.plotly_chart(transition_plants_treemap_fh)

with tab_l:
    st.plotly_chart(transition_plants_treemap_l)

with tab_a:
    st.plotly_chart(transition_plants_treemap_a)

transition_plants_treemap_per_landscape_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
Regarding the different landscapes and how they are defined in current project, you can consult the <b><i>Metadata</i></b> page. The color mapping refers to the 46 different plant 
families of the dataset.</p>"""
st.markdown(transition_plants_treemap_per_landscape_summary, unsafe_allow_html = True)


next_page_intro = """

You have reached the end of the Project Scope exploration. You can now continue to the next page by clicking the following button.

"""

st.markdown(next_page_intro, unsafe_allow_html = True)

button_go_to_diy_exploration = st.button("go to " + pages["diy_exploration"]["kwargs"]["name"])
if button_go_to_diy_exploration:
    #st.session_state["input_csv_file"] = df
    st.switch_page(pages["diy_exploration"]["path"])
