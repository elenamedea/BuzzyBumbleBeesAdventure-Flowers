import streamlit as st

from utils import csv_to_df, trim_whitespace_inplace

from utils import generate_pie_chart, generate_melted_pie_chart, generate_stacked_barplot, generate_treemap, generate_species_treemap, generate_scatterplot

from utils import generate_blossoming_time_barplot, generate_horizontal_boxplot, generate_height_range_barplot, generate_melted_treemap

from utils import months, seasons, heights, usages

from utils import heights_color_dict, families_color_dict, cycles_color_dict, bool_color_dict, true_color_dict, usages_color_dict

from utils.pages_menu import pages_menu, pages


pages_menu()

# Title and App summary
 
st.title("Exploratory Data Analysis (EDA) for 131 plants belonging to the Flora of Bavaria :face_with_monocle:")

app_summary = """

The current page enables the universal exploration of plants' dataset. 

In particular, you can inspect the :violet[**_Plant Families_**], :violet[**_Life Cycles_**], :violet[**_Blossoming time_**], :violet[**_Height_**] of the plant species,
as well as their :violet[**_Edibility_**], :violet[**_Toxicity_**], :violet[**_Threatened Status_**], and :violet[**_Usages_**].

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

A plethora of diagrams is generated, encapsulating the universal profile of the data through the features :violet[**_Plant Families_**], 
                    :violet[**_Life Cycles_**], :violet[**_Blossoming time_**], :violet[**_Height_**],:violet[**_Edibility_**], :violet[**_Toxicity_**], 
                    :violet[**_Threatened Status_**], and :violet[**_Usages_**]. :chart_with_upwards_trend::chart_with_downwards_trend::bar_chart:

For each feature there are at least two diagrams developed. You can monitor them by changing tabs. :three_button_mouse::point_up_2:
                    
After getting a general idea of the plants' dataset, you can move to the :gray[**_Exploratory Data Analysis: Project scope_**] :honeybee: page and go deeper in the 
                    data exploration by getting familiar with the scope of the present project. :blossom::honeybee:

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

st.header("Universal exploratory analysis on the data collection")

st.subheader("Plant Families")
tab_fam1, tab_fam2 = st.tabs(["Pie chart", "Barplot"])


# Pie chart for Family
fig_families = generate_pie_chart(df, "Family", "Family", "Plant Families", families_color_dict, "Plant Families", height = 1400, width = 1600)
# Barplot for Family
family_stacked_bar_chart = generate_stacked_barplot(df, "Family", "Plant Families", families_color_dict, "Plant Families", height = 900, width = 1600)

with tab_fam1:
    st.plotly_chart(fig_families)

with tab_fam2:
    st.plotly_chart(family_stacked_bar_chart)

families_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
The color mapping refers to the 46 different plant families of the dataset.</p>"""
st.markdown(families_summary, unsafe_allow_html = True)


st.subheader("Life Cycles of the plants")
tab_lc1, tab_lc2 = st.tabs(["Pie chart", "Treemap"])

# Pie chart for Life Cycle
fig_cycles = generate_pie_chart(df, "Life cycle", "Life cycle", "Life Cycles of the Plants", cycles_color_dict, "Life Cycles", height = 1400, width = 1600)
fig_cycles.update_layout(margin = dict(l = 150, r = 0, b = 0, t = 0))
# Treemap for Life Cycle
cycles_treemap = generate_treemap(df, "Life cycle", cycles_color_dict, "Life Cycles of the Plants", height = 900, width = 1600)

with tab_lc1:
    st.plotly_chart(fig_cycles)

with tab_lc2:
    st.plotly_chart(cycles_treemap)

life_cycles_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
The color mapping refers to the 7 different plants' life cycles of the dataset. Regarding terminology of the life cycles, you can consult 
the <b><i>Metadata</i></b> page.</p>"""
st.markdown(life_cycles_summary, unsafe_allow_html = True)


st.subheader("Blossoming time of the plants")
tab_bt1, tab_bt2 = st.tabs(["Months", "Seasons"])

# Months
fig_months = generate_blossoming_time_barplot(df, "Scientific name", months, "Months", "Count", "Monthly Occurrences", true_color_dict)
# Seasons
fig_seasons = generate_blossoming_time_barplot(df, "Scientific name", seasons, "Seasons", "Count","Seasonal Occurrences", true_color_dict)

with tab_bt1:
    st.plotly_chart(fig_months)

with tab_bt2:
    st.plotly_chart(fig_seasons)

blossoming_time_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>The 
blossoming time refers to the time a plant species occurs and is not coincided with the flowering time of the species. Seasons refer to the 
meteorological seasons in Northen Hemisphere. <b><i>Spring</i></b> months are March, April, and May, <b><i>Summer</i></b> months are June, July, and August, 
<b><i>Autumn</i></b> months are September, October, and November, and <b><i>Winter</i></b> months are December, January, and February.</p>"""
st.markdown(blossoming_time_summary, unsafe_allow_html = True)


st.subheader("Height of the plants")
tab_h1, tab_h2, tab_h3, tab_h4 = st.tabs(["Boxplot", "Scatterplot", "Height range barplot", "Height range(lower than 500 cm) barplot"])

# Height boxplot
height_boxplot = generate_horizontal_boxplot(df, "Scientific name", heights, heights_color_dict, "Min & max height in cm for the Plants", "", "Height in cm", height = 900, width = 1600)
# Height scatterplot
scatter_plot = generate_scatterplot(df, "Height min(cm)", "Height max(cm)", "Scientific name", "Min & max height in cm for the Plants")
# Height range barplot
height_barplot = generate_height_range_barplot(df, "Scientific name", heights, heights_color_dict, "Height Range for Plant Species", "Plant species", "Height in cm", "Height")
# Height range barplot lower than 500 cm
height_lower_than_500 = df[df["Height max(cm)"] < 500]
height_barplot_lower_than_500 = generate_height_range_barplot(height_lower_than_500, "Scientific name", heights, heights_color_dict, "Height Range(lower than 500 cm) for Plant Species", "Plant species", "Height in cm", "Height")

with tab_h1:
    st.plotly_chart(height_boxplot)

with tab_h2:
    st.plotly_chart(scatter_plot)

with tab_h3:
    st.plotly_chart(height_barplot)

with tab_h4:
    st.plotly_chart(height_barplot_lower_than_500)

height_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
There are several plots generated in order to summarize the height range of the plant species. For additional information, you may refer to the 
<b><i>Documentation of the Plotly library</i></b> used for these visualisations and/or the <b><i>Wikipedia</i></b> website.</p>"""
st.markdown(height_summary, unsafe_allow_html = True)


st.subheader("Edibility of the plants")
tab_ed1, tab_ed2 = st.tabs(["Pie chart", "Species treemap"])

# Pie chart for Edible plants
fig_edible = generate_pie_chart(df, "Edible", "Edible", "Edibility of the Plants", bool_color_dict, "Edibility of the Plants", height = 1400, width = 1600)
# Species treemap for Edible plants
edible_treemap = generate_species_treemap(df, "Edible", "Scientific name", "Family", "Summary of species for: Edible plants", families_color_dict, height = 900, width = 1600)

with tab_ed1:
    st.plotly_chart(fig_edible)

with tab_ed2:
    st.plotly_chart(edible_treemap)

edibility_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
The color mapping of the species treemap refers to the 46 different plant families of the dataset.</p>"""
st.markdown(edibility_summary, unsafe_allow_html = True)


st.subheader("Toxicity of the plants")
tab_pois1, tab_pois2 = st.tabs(["Pie chart", "Species treemap"])

# Pie chart for Poisonous plants
fig_poisonous = generate_pie_chart(df, "Poisonous", "Poisonous", "Poisonous Nature of the Plants", bool_color_dict, "Poisonous Nature of the Plants", height = 1400, width = 1600)
# Species treemap for Poisonous plants
poisonous_treemap = generate_species_treemap(df, "Poisonous", "Scientific name", "Family", "Summary of species for: Poisonous plants", families_color_dict, height = 900, width = 1600)

with tab_pois1:
    st.plotly_chart(fig_poisonous)

with tab_pois2:
    st.plotly_chart(poisonous_treemap)

toxicity_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
The color mapping of the species treemap refers to the 46 different plant families of the dataset.</p>"""
st.markdown(toxicity_summary, unsafe_allow_html = True)


st.subheader("Threatened Status of the plants")
tab_thr1, tab_thr2 = st.tabs(["Pie chart", "Species treemap"])

# Pie chart for Threatened Status
fig_threatened = generate_pie_chart(df, "Threatened", "Threatened", "Threatened Status of the Plants", bool_color_dict, "Threatened Status of the Plants", height = 1400, width = 1600)
# Species treemap for Threatened Status
threatened_treemap = generate_species_treemap(df, "Threatened", "Scientific name", "Family", "Summary of species for: Threatened plants", families_color_dict, height = 900, width = 1600)

with tab_thr1:
    st.plotly_chart(fig_threatened)

with tab_thr2:
    st.plotly_chart(threatened_treemap)

threatened_status_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
The color mapping of the species treemap refers to the 46 different plant families of the dataset.</p>"""
st.markdown(threatened_status_summary, unsafe_allow_html = True)


st.subheader("Usages of the plants")
tab_us1, tab_us2 = st.tabs(["Pie chart", "Treemap"])

# Pie chart for Usages of the plants
usages_pie_chart = generate_melted_pie_chart(df, "Scientific name", usages, "Usage of the Plants", usages_color_dict, "Usages", height = 1400, width = 1650)
# Treemap for Usages of the plants
usages_treemap = generate_melted_treemap(df, "Scientific name", usages, usages_color_dict, "Usages of the Plants", height = 900, width = 1600)

with tab_us1:
    st.plotly_chart(usages_pie_chart)

with tab_us2:
    st.plotly_chart(usages_treemap)

usages_summary = """<p style='text-align: left; background-color: #efe9ec; color: #0a0a0a; font-family: monospace; font-size: 16px;'>
The color mapping refers to the 27 different plants' usage categories of the dataset.</p>"""
st.markdown(usages_summary, unsafe_allow_html = True)


next_page_intro = """
    
You have reached the end of the universal exploratory analysis of the data. You can now continue to the next page by clicking the following button.
    
    """
    
st.markdown(next_page_intro, unsafe_allow_html = True)

button_go_to_project_scope = st.button("go to " + pages["eda_project_scope"]["kwargs"]["name"])
if button_go_to_project_scope:
    #st.session_state["input_csv_file"] = df
    st.switch_page(pages["eda_project_scope"]["path"])

